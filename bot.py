# ─────────────────────────────────────────────
#  main_bot.py — Zorro Trading Bot (Full Version)
#  • Private channel support (numeric chat ID)
#  • Welcome thumbnail image
#  • All markets: Gold, Forex, Crypto
#  • Daily promo at 23:59 UTC
#  • 4 buttons only: TG Channel, TG Admin, WA Channel, WA Admin
# ─────────────────────────────────────────────

import logging
import sqlite3
import asyncio
import json        # ← yeh line hai ya nahi check karo
from datetime import time as dtime
import os
import pytz

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ChatMemberUpdated,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ChatMemberHandler,
    CallbackQueryHandler,   # ← yeh add karo
    filters,
    ContextTypes,
)
from telegram.error import TelegramError

from faq import faq_handler


# ─────────────────────────────────────────────
#  ⚙️  CONFIG
# ─────────────────────────────────────────────

BOT_TOKEN = "8538490992:AAEH6YNNBGvxDTqMF0MJN2uYu2UcQfMuSM8"

# ⚠️ PRIVATE CHANNEL: numeric ID daalo (e.g. -1001234567890)
# Kaise nikalen: bot chalao, channel mein koi msg karo,
# terminal mein "🆔 Chat ID:" print hoga — wahi number yahan daalo
MAIN_CHANNEL_ID = -1001980427873     # ← REPLACE WITH REAL NUMERIC ID

# Invite link (sirf buttons ke liye — API calls mein nahi)
TG_CHANNEL_LINK = "https://t.me/+1GeEbtebtz81NjU8"
TG_ADMIN_LINK   = "https://t.me/zorrofxadmin"
WA_CHANNEL_LINK = "https://whatsapp.com/channel/0029VbConbY6hENjNS8Ak51S"
WA_ADMIN_LINK   = "https://wa.me/+447848142501"
# ═══════════════════════════════════════════════════════════════



ADMIN_USER_ID   = 6284049852              # ← /myid command se nikalo, yahan daalo




ASSETS_DIR    = "assets"
WELCOME_IMAGE = os.path.join(ASSETS_DIR, "welcome.jpg")
PROMO_IMAGE   = os.path.join(ASSETS_DIR, "promo.jpg")
CONFIG_FILE   = "config.json"

PROMO_HOUR   = 23   # 23:59 UTC
PROMO_MINUTE = 59
TIMEZONE     = pytz.UTC


# ═══════════════════════════════════════════════════════════════
#  📝  CONFIG  (promo text config.json mein save hota hai)
# ═══════════════════════════════════════════════════════════════

DEFAULT_PROMO_TEXT = (
    "🌐 *ZORRO TRADING — FREE SIGNALS FOR ALL MARKETS*\n\n"
    "We cover EVERYTHING in one place:\n\n"
    "🥇 *Gold (XAUUSD)* — Daily signals\n"
    "💱 *Forex* — EUR/USD · GBP/USD · USD/JPY & more\n"
    "₿ *Crypto* — BTC · ETH · XRP · SOL\n"
    "📊 *Indices* — US30 · SPX500 · NAS100\n\n"
    "✅ 85%+ Win Rate | FREE to join\n"
    "✅ Entry · SL · TP on every signal\n"
    "✅ 10,000+ active traders worldwide\n"
    "✅ Live updates 24/7\n\n"
    "👇 *Join FREE — Tap below:*"
)


def load_config() -> dict:
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"promo_text": DEFAULT_PROMO_TEXT}


def save_config(data: dict):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_promo_text() -> str:
    return load_config().get("promo_text", DEFAULT_PROMO_TEXT)


def set_promo_text(text: str):
    cfg = load_config()
    cfg["promo_text"] = text
    save_config(cfg)


# ═══════════════════════════════════════════════════════════════
#  🗄️  DATABASE  (auto-create hogi)
# ═══════════════════════════════════════════════════════════════

DB_FILE = "zorro_users.db"


def db_connect():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id     INTEGER PRIMARY KEY,
            username    TEXT,
            first_name  TEXT,
            is_active   INTEGER DEFAULT 1,
            joined_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    return conn


def db_save_user(user_id: int, username: str, first_name: str):
    conn = db_connect()
    conn.execute(
        """INSERT INTO users (user_id, username, first_name, is_active)
           VALUES (?, ?, ?, 1)
           ON CONFLICT(user_id) DO UPDATE SET
               username   = excluded.username,
               first_name = excluded.first_name,
               is_active  = 1""",
        (user_id, username or "", first_name or ""),
    )
    conn.commit()
    conn.close()
    logging.info(f"✅ User saved: {user_id} (@{username})")


def db_mark_left(user_id: int):
    conn = db_connect()
    conn.execute("UPDATE users SET is_active = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()
    logging.info(f"👋 User left: {user_id}")


def db_get_active_users() -> list[int]:
    conn = db_connect()
    rows = conn.execute(
        "SELECT user_id FROM users WHERE is_active = 1"
    ).fetchall()
    conn.close()
    return [r[0] for r in rows]


def db_get_stats() -> dict:
    conn = db_connect()
    total  = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    active = conn.execute(
        "SELECT COUNT(*) FROM users WHERE is_active = 1"
    ).fetchone()[0]
    conn.close()
    return {"total": total, "active": active, "inactive": total - active}


# ═══════════════════════════════════════════════════════════════
#  🔘  KEYBOARDS
# ═══════════════════════════════════════════════════════════════

def main_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 Free Telegram Channel", url=TG_CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Telegram Admin",        url=TG_ADMIN_LINK)],
        [InlineKeyboardButton("🟢 Free WhatsApp Channel", url=WA_CHANNEL_LINK)],
        [InlineKeyboardButton("📱 WhatsApp Admin",        url=WA_ADMIN_LINK)],
    ])


def promo_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("✅ Join FREE Now!", url=TG_CHANNEL_LINK)],
        [InlineKeyboardButton("💬 Telegram Admin", url=TG_ADMIN_LINK),
         InlineKeyboardButton("📱 WhatsApp Admin", url=WA_ADMIN_LINK)],
    ])


def admin_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📸 Welcome Image", callback_data="admin_welcome_img"),
         InlineKeyboardButton("🖼 Promo Image",   callback_data="admin_promo_img")],
        [InlineKeyboardButton("✏️ Promo Text",    callback_data="admin_promo_text")],
        [InlineKeyboardButton("👁 Preview Promo", callback_data="admin_preview"),
         InlineKeyboardButton("📊 Stats",         callback_data="admin_stats")],
        [InlineKeyboardButton("❌ Close",          callback_data="admin_close")],
    ])


# ═══════════════════════════════════════════════════════════════
#  🔐  ADMIN STATE
# ═══════════════════════════════════════════════════════════════

_admin_pending: dict = {}


def is_admin(user_id: int) -> bool:
    return ADMIN_USER_ID != 0 and user_id == ADMIN_USER_ID


# ═══════════════════════════════════════════════════════════════
#  /myid COMMAND
# ═══════════════════════════════════════════════════════════════

async def myid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = update.effective_user.id
    await update.message.reply_text(
        f"🆔 *Your Telegram User ID:*\n`{uid}`\n\n"
        "Yeh number `ADMIN_USER_ID` mein daalo `bot.py` mein.",
        parse_mode="Markdown",
    )


# ═══════════════════════════════════════════════════════════════
#  /admin COMMAND
# ═══════════════════════════════════════════════════════════════

async def admin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    if not is_admin(user.id):
        await update.message.reply_text("⛔ Not authorized.")
        return

    _admin_pending.pop(user.id, None)

    stats              = db_get_stats()
    welcome_status     = "✅ Set" if os.path.exists(WELCOME_IMAGE) else "❌ Not set"
    promo_img_status   = "✅ Set" if os.path.exists(PROMO_IMAGE)   else "❌ Not set"
    promo_text_preview = get_promo_text()[:80] + "..."

    await update.message.reply_text(
        "🎛 *Admin Panel — Zorro Trading Bot*\n\n"
        f"👥 Users: *{stats['active']} active* / {stats['total']} total\n"
        f"📸 Welcome Image: {welcome_status}\n"
        f"🖼 Promo Image:   {promo_img_status}\n"
        f"✏️ Promo Text:   _{promo_text_preview}_\n"
        f"⏰ Promo Time:   23:59 UTC daily\n\n"
        "Select an option:",
        parse_mode="Markdown",
        reply_markup=admin_menu_keyboard(),
    )


# ═══════════════════════════════════════════════════════════════
#  ADMIN CALLBACK HANDLER
# ═══════════════════════════════════════════════════════════════

async def admin_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user  = query.from_user

    if not is_admin(user.id):
        await query.answer("⛔ Not authorized.", show_alert=True)
        return

    await query.answer()
    data = query.data

    if data == "admin_welcome_img":
        _admin_pending[user.id] = "welcome_img"
        await query.edit_message_text(
            "📸 *Update Welcome Image*\n\n"
            "Ab apni *welcome thumbnail* image send karo.\n"
            "_(JPG/PNG — recommended: 1280×720)_\n\n"
            "❌ Cancel: /admin",
            parse_mode="Markdown",
        )

    elif data == "admin_promo_img":
        _admin_pending[user.id] = "promo_img"
        await query.edit_message_text(
            "🖼 *Update Promo Image*\n\n"
            "Ab apni *daily promo image* send karo.\n"
            "_(JPG/PNG — recommended: 1280×720)_\n\n"
            "❌ Cancel: /admin",
            parse_mode="Markdown",
        )

    elif data == "admin_promo_text":
        _admin_pending[user.id] = "promo_text"
        current = get_promo_text()
        await query.edit_message_text(
            "✏️ *Update Promo Text*\n\n"
            "Ab *naya promo text* type karke send karo.\n"
            "Markdown: \\*bold\\*, \\_italic\\_\n\n"
            f"*Current text:*\n`{current[:250]}`\n\n"
            "❌ Cancel: /admin",
            parse_mode="Markdown",
        )

    elif data == "admin_preview":
        promo_text = get_promo_text()
        await query.message.reply_text(
            "👁 *Preview — exactly how users will see it:*",
            parse_mode="Markdown",
        )
        try:
            with open(PROMO_IMAGE, "rb") as img:
                await query.message.reply_photo(
                    photo=img,
                    caption=promo_text,
                    parse_mode="Markdown",
                    reply_markup=promo_keyboard(),
                )
        except FileNotFoundError:
            await query.message.reply_text(
                f"⚠️ Promo image missing! Text-only preview:\n\n{promo_text}",
                parse_mode="Markdown",
                reply_markup=promo_keyboard(),
            )

    elif data == "admin_stats":
        stats = db_get_stats()
        await query.edit_message_text(
            "📊 *Bot Statistics*\n\n"
            f"👥 Total users ever:    *{stats['total']}*\n"
            f"✅ Active (in channel): *{stats['active']}*\n"
            f"👋 Inactive (left):    *{stats['inactive']}*\n\n"
            f"📸 Welcome image: {'✅ Ready' if os.path.exists(WELCOME_IMAGE) else '❌ Missing'}\n"
            f"🖼 Promo image:   {'✅ Ready' if os.path.exists(PROMO_IMAGE)   else '❌ Missing'}\n"
            f"⏰ Promo: 23:59 UTC daily\n"
            f"📁 Folder: `{os.path.abspath(ASSETS_DIR)}`",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔙 Back", callback_data="admin_back")]
            ]),
        )

    elif data == "admin_close":
        _admin_pending.pop(user.id, None)
        await query.edit_message_text("✅ Admin panel closed.")

    elif data == "admin_back":
        _admin_pending.pop(user.id, None)
        stats              = db_get_stats()
        welcome_status     = "✅ Set" if os.path.exists(WELCOME_IMAGE) else "❌ Not set"
        promo_img_status   = "✅ Set" if os.path.exists(PROMO_IMAGE)   else "❌ Not set"
        promo_text_preview = get_promo_text()[:80] + "..."
        await query.edit_message_text(
            "🎛 *Admin Panel — Zorro Trading Bot*\n\n"
            f"👥 Users: *{stats['active']} active* / {stats['total']} total\n"
            f"📸 Welcome Image: {welcome_status}\n"
            f"🖼 Promo Image:   {promo_img_status}\n"
            f"✏️ Promo Text:   _{promo_text_preview}_\n"
            f"⏰ Promo Time:   23:59 UTC daily\n\n"
            "Select an option:",
            parse_mode="Markdown",
            reply_markup=admin_menu_keyboard(),
        )


# ═══════════════════════════════════════════════════════════════
#  📨  UNIVERSAL MESSAGE HANDLER
#  Admin state → image/text save | Regular user → FAQ
# ═══════════════════════════════════════════════════════════════

async def universal_message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    msg  = update.message
    if not msg:
        return

    pending = _admin_pending.get(user.id)

    if is_admin(user.id) and pending:

        if pending == "welcome_img":
            if msg.photo:
                os.makedirs(ASSETS_DIR, exist_ok=True)
                file = await msg.photo[-1].get_file()
                await file.download_to_drive(WELCOME_IMAGE)
                _admin_pending.pop(user.id, None)
                await msg.reply_text(
                    f"✅ *Welcome image saved!*\n"
                    f"📁 `{os.path.abspath(WELCOME_IMAGE)}`\n\n"
                    "Test: /start\nMore: /admin",
                    parse_mode="Markdown",
                )
            else:
                await msg.reply_text("⚠️ Photo/image send karo. Cancel: /admin")
            return

        elif pending == "promo_img":
            if msg.photo:
                os.makedirs(ASSETS_DIR, exist_ok=True)
                file = await msg.photo[-1].get_file()
                await file.download_to_drive(PROMO_IMAGE)
                _admin_pending.pop(user.id, None)
                await msg.reply_text(
                    f"✅ *Promo image saved!*\n"
                    f"📁 `{os.path.abspath(PROMO_IMAGE)}`\n\n"
                    "Preview: /admin → 👁 Preview\nMore: /admin",
                    parse_mode="Markdown",
                )
            else:
                await msg.reply_text("⚠️ Photo/image send karo. Cancel: /admin")
            return

        elif pending == "promo_text":
            if msg.text:
                set_promo_text(msg.text)
                _admin_pending.pop(user.id, None)
                await msg.reply_text(
                    "✅ *Promo text updated & saved!*\n\n"
                    "Preview: /admin → 👁 Preview\nMore: /admin",
                    parse_mode="Markdown",
                )
            else:
                await msg.reply_text("⚠️ Text message bhejo. Cancel: /admin")
            return

    if msg.text:
        await faq_handler(update, context)


# ═══════════════════════════════════════════════════════════════
#  📡  CHANNEL AUTO-TRACKER
# ═══════════════════════════════════════════════════════════════

def _extract_status_change(cmu: ChatMemberUpdated):
    old = cmu.old_chat_member.status
    new = cmu.new_chat_member.status
    ACTIVE   = {"member", "administrator", "creator"}
    INACTIVE = {"left", "kicked", "banned", "restricted"}
    if old in INACTIVE and new in ACTIVE:
        return True
    if old in ACTIVE and new in INACTIVE:
        return False
    return None


async def track_channel_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result is None:
        return
    logging.info(f"🆔 Chat ID: {result.chat.id} | Title: {result.chat.title}")
    if result.chat.id != MAIN_CHANNEL_ID:
        return
    user   = result.new_chat_member.user
    change = _extract_status_change(result)
    if change is True:
        db_save_user(user.id, user.username, user.first_name)
        logging.info(f"🆕 Joined: {user.first_name} (ID:{user.id})")
    elif change is False:
        db_mark_left(user.id)
        logging.info(f"❌ Left: {user.first_name} (ID:{user.id})")


# ═══════════════════════════════════════════════════════════════
#  🔍  MEMBERSHIP CHECK
# ═══════════════════════════════════════════════════════════════

async def is_channel_member(bot, user_id: int) -> bool:
    try:
        member = await bot.get_chat_member(
            chat_id=MAIN_CHANNEL_ID, user_id=user_id
        )
        return member.status in ("member", "administrator", "creator")
    except TelegramError:
        return False


# ═══════════════════════════════════════════════════════════════
#  🎉  /start
# ═══════════════════════════════════════════════════════════════

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    db_save_user(user.id, user.username, user.first_name)

    caption = (
        f"👋 Welcome, *{user.first_name}*!\n\n"
        "You've joined *Zorro Trading Community*! 🎉\n\n"
        "FREE daily signals for:\n"
        "🥇 Gold (XAUUSD)\n"
        "💱 Forex — EUR/USD, GBP/USD & more\n"
        "₿ Crypto — BTC, ETH, XRP, SOL\n"
        "📊 Indices — US30, SPX, NAS100\n\n"
        "📈 *85%+ Win Rate | FREE | 10,000+ Traders*\n\n"
        "💡 *Ask me anything:*\n"
        "_'Win rate?'_ | _'Is this free?'_ | _'Which broker?'_\n\n"
        "📌 *Connect with us:*"
    )

    try:
        with open(WELCOME_IMAGE, "rb") as img:
            await update.message.reply_photo(
                photo=img,
                caption=caption,
                parse_mode="Markdown",
                reply_markup=main_keyboard(),
            )
    except FileNotFoundError:
        await update.message.reply_text(
            caption,
            parse_mode="Markdown",
            reply_markup=main_keyboard(),
        )


# ═══════════════════════════════════════════════════════════════
#  📣  DAILY PROMO JOB  (23:59 UTC)
# ═══════════════════════════════════════════════════════════════

async def daily_promo_job(context: ContextTypes.DEFAULT_TYPE):
    bot        = context.bot
    all_users  = db_get_active_users()
    promo_text = get_promo_text()

    sent = skipped = failed = 0
    logging.info(f"📣 Daily promo — {len(all_users)} users")

    for user_id in all_users:
        if await is_channel_member(bot, user_id):
            skipped += 1
            continue
        try:
            try:
                with open(PROMO_IMAGE, "rb") as img:
                    await bot.send_photo(
                        chat_id=user_id,
                        photo=img,
                        caption=promo_text,
                        parse_mode="Markdown",
                        reply_markup=promo_keyboard(),
                    )
            except FileNotFoundError:
                await bot.send_message(
                    chat_id=user_id,
                    text=promo_text,
                    parse_mode="Markdown",
                    reply_markup=promo_keyboard(),
                )
            sent += 1
            await asyncio.sleep(0.05)
        except TelegramError as e:
            failed += 1
            logging.warning(f"Could not send to {user_id}: {e}")

    logging.info(f"✅ Done — sent:{sent} skipped:{skipped} failed:{failed}")


# ═══════════════════════════════════════════════════════════════
#  🚀  MAIN
# ═══════════════════════════════════════════════════════════════

def main():
    from keep_alive import keep_alive
    keep_alive()              # ← yeh add karo
    logging.basicConfig(
        format="%(asctime)s | %(levelname)s | %(message)s",
        level=logging.INFO,
    )

    os.makedirs(ASSETS_DIR, exist_ok=True)

    if not os.path.exists(CONFIG_FILE):
        save_config({"promo_text": DEFAULT_PROMO_TEXT})
        logging.info("✅ config.json created")

    if ADMIN_USER_ID == 0:
        logging.warning(
            "⚠️  ADMIN_USER_ID = 0 — /myid command bhejo apna ID daalne ke liye"
        )

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("admin", admin_command))
    app.add_handler(CommandHandler("myid",  myid_command))
    app.add_handler(CallbackQueryHandler(admin_callback, pattern="^admin_"))
    app.add_handler(ChatMemberHandler(
        track_channel_member, ChatMemberHandler.CHAT_MEMBER
    ))
    app.add_handler(MessageHandler(
        filters.ALL & ~filters.COMMAND,
        universal_message_handler
    ))

    app.job_queue.run_daily(
        daily_promo_job,
        time=dtime(hour=PROMO_HOUR, minute=PROMO_MINUTE, tzinfo=TIMEZONE),
        name="daily_promo",
    )

    logging.info("✅ Zorro Trading Bot is running!")
    logging.info("⏰ Daily promo: 23:59 UTC")
    logging.info(f"📁 Assets: {os.path.abspath(ASSETS_DIR)}")

    app.run_polling(
        allowed_updates=["message", "chat_member", "callback_query"],
        stop_signals=(),
    )


if __name__ == "__main__":
    main()