# ═══════════════════════════════════════════════════════════════
#  faq.py — Zorro Trading Bot FAQ Engine
#  ✅ Telegram Ads Policy Compliant
#  ✅ No WhatsApp links
#  ✅ No exaggerated claims
#  ✅ Risk disclaimer added
#  ✅ 4 Telegram channels: Support, Main, Tools, Education
# ═══════════════════════════════════════════════════════════════

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes


# ─────────────────────────────────────────────
#  ⚙️  CONFIG — main_bot.py se match karo
# ─────────────────────────────────────────────

# ── Invite / Profile Links ─────────────────────────────────────
TG_SUPPORT_LINK  = "https://t.me/zorrofxadmin"
TG_CHANNEL_LINK  = "https://t.me/+1GeEbtebtz81NjU8"
TG_TOOLS_LINK    = "https://t.me/zorroforextools"  # ← Replace karo
TG_EDU_LINK      = "https://t.me/ZORROEDUCATION"    # ← Replace karo

RISK_DISCLAIMER = (
    "\n\n⚠️ _Trading involves risk. Past performance does not "
    "guarantee future results. Always manage your risk responsibly._"
)


# ─────────────────────────────────────────────
#  🔘  CONTACT KEYBOARD
# ─────────────────────────────────────────────

def contact_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Telegram Support",  url=TG_SUPPORT_LINK)],
        [InlineKeyboardButton("📢 Zorro AI Channel",  url=TG_CHANNEL_LINK)],
        [InlineKeyboardButton("🛠 Zorro Forex Tools", url=TG_TOOLS_LINK)],
        [InlineKeyboardButton("📚 Zorro Education",   url=TG_EDU_LINK)],
    ])


# ─────────────────────────────────────────────
#  📚  FAQ DATABASE
# ─────────────────────────────────────────────

FAQ_DATA = [

    # ── Signals ───────────────────────────────
    {
        "keywords": ["signal", "signals", "trade signal", "free signal", "daily signal",
                     "trading signal", "gold signal", "xauusd signal", "forex signal"],
        "answer": (
            "📊 *About Our Trading Signals*\n\n"
            "We provide *FREE daily signals* for Forex, Gold, Crypto & Indices every trading day!\n\n"
            "✅ Entry price\n"
            "✅ Stop Loss (SL)\n"
            "✅ Take Profit 1 & 2 (TP)\n"
            "✅ Signal reasoning & analysis\n\n"
            "🔔 *Join our free channel* to receive signals directly on your phone!"
            + RISK_DISCLAIMER
        ),
    },
    {
        "keywords": ["how many signals", "signals per day", "daily how many",
                     "kitne signal", "per day signals"],
        "answer": (
            "📊 *How Many Signals Per Day?*\n\n"
            "We typically send *2–4 signals per day* depending on market conditions.\n\n"
            "📅 Active days: *Monday to Friday*\n"
            "🕐 Signal timing: *Morning & Afternoon sessions (IST)*\n\n"
            "💡 On high-volatility days (NFP, CPI, FOMC), we may send extra alerts!"
            + RISK_DISCLAIMER
        ),
    },
    {
        "keywords": ["missed signal", "miss signal", "old signal", "past signal",
                     "signal history", "previous signal"],
        "answer": (
            "📜 *Missed a Signal?*\n\n"
            "Don't worry! You can view all *past signals & results* in our Telegram channel history.\n\n"
            "📌 All signals are *pinned* in the channel for easy access.\n"
            "📊 Monthly performance reports are posted every 1st of the month.\n\n"
            "💡 Tip: Enable notifications so you never miss one!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Win Rate & Results ─────────────────────
    {
        "keywords": ["win rate", "winrate", "accuracy", "success rate", "hit rate",
                     "how accurate", "kitna accurate", "profit"],
        "answer": (
            "🎯 *Our Signal Accuracy*\n\n"
            "We provide structured, risk-managed setups with defined entry, SL and TP on every signal.\n\n"
            "📊 *What we track:*\n"
            "• Average Risk:Reward Ratio: 1:2 to 1:3\n"
            "• Average SL: 20–35 pips\n"
            "• Average TP: 50–120 pips\n\n"
            "✅ Full monthly results are posted on our channel with screenshots."
            + RISK_DISCLAIMER
        ),
    },
    {
        "keywords": ["result", "results", "performance", "track record",
                     "proof", "screenshot", "verified"],
        "answer": (
            "📊 *Our Track Record & Proof*\n\n"
            "We believe in *full transparency!* 🔍\n\n"
            "✅ Every signal result posted with broker screenshots\n"
            "✅ Monthly P&L reports shared publicly\n"
            "✅ Live trade updates in real-time\n\n"
            "📢 Check our channel history for all past results!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Membership & Cost ──────────────────────
    {
        "keywords": ["free", "cost", "price", "paid", "charge", "fee", "subscription",
                     "membership", "kitna paisa", "free hai", "payment"],
        "answer": (
            "💰 *Is It Free?*\n\n"
            "YES! Our *basic signal service is 100% FREE* 🎉\n\n"
            "✅ Free daily signals — No cost\n"
            "✅ Free market analysis — No cost\n"
            "✅ Free community access — No cost\n\n"
            "👑 *Premium VIP Plan* (Optional):\n"
            "• More signals per day\n"
            "• Early entry alerts\n"
            "• 1-on-1 mentoring\n"
            "• Personal portfolio review\n\n"
            "💬 For VIP pricing, contact our support directly!"
            + RISK_DISCLAIMER
        ),
    },
    {
        "keywords": ["vip", "premium", "paid plan", "pro plan", "upgrade",
                     "vip plan", "vip signals", "paid signals"],
        "answer": (
            "👑 *VIP / Premium Membership*\n\n"
            "Our VIP plan gives you access to more structured setups:\n\n"
            "🔥 *VIP Benefits:*\n"
            "• 5–8 signals per day (vs 2–4 free)\n"
            "• Early entry alerts\n"
            "• Exclusive analysis\n"
            "• Personal 1-on-1 mentoring\n"
            "• Weekly live trading sessions\n"
            "• Risk management review\n\n"
            "💬 Contact support for current pricing!"
            + RISK_DISCLAIMER
        ),
    },

    # ── How to Join ────────────────────────────
    {
        "keywords": ["join", "how to join", "kaise join", "register", "sign up",
                     "subscribe", "kaise subscribe", "channel join"],
        "answer": (
            "✅ *How to Join Zorro Trading Community*\n\n"
            "Joining is *super easy & free!* Here's how:\n\n"
            "1️⃣ Click the *'Zorro AI Channel'* button below\n"
            "2️⃣ Press *'Join'* on the Telegram channel\n"
            "3️⃣ Enable notifications 🔔\n"
            "4️⃣ Start receiving free daily signals!\n\n"
            "📚 Also join *Zorro Education* for chart studies & market material.\n"
            "🛠 Join *Zorro Forex Tools* for EAs & MT5 indicators."
            + RISK_DISCLAIMER
        ),
    },

    # ── Markets Covered ────────────────────────
    {
        "keywords": ["forex", "currency", "eurusd", "gbpusd", "usdjpy", "other pairs",
                     "bitcoin", "crypto", "btc", "stock", "indices", "xauusd", "gold",
                     "what markets", "which pairs", "nas100", "us30"],
        "answer": (
            "💹 *Markets We Cover*\n\n"
            "We provide signals across *ALL major markets:*\n\n"
            "💱 *Forex:* EUR/USD · GBP/USD · USD/JPY · AUD/USD · USD/CAD & more\n"
            "🥇 *Gold:* XAU/USD — Daily setups\n"
            "₿  *Crypto:* BTC · ETH · XRP · SOL\n"
            "📊 *Indices:* US30 · SPX500 · NAS100\n\n"
            "✅ Entry · SL · TP on every signal"
            + RISK_DISCLAIMER
        ),
    },

    # ── Broker ─────────────────────────────────
    {
        "keywords": ["broker", "which broker", "best broker", "recommended broker",
                     "broker suggest", "which platform", "mt4", "mt5", "metatrader"],
        "answer": (
            "🏦 *Which Broker Should I Use?*\n\n"
            "We are *broker-independent* — our signals work on any broker! ✅\n\n"
            "📌 *Look for brokers with:*\n"
            "• Low spread on major pairs\n"
            "• Fast execution (no requotes)\n"
            "• MT4 or MT5 platform support\n"
            "• Regulated (FCA, CySEC, ASIC)\n\n"
            "💡 *Popular choices among members:*\n"
            "XM, Exness, IC Markets, Pepperstone, FBS\n\n"
            "⚠️ Always verify regulation before depositing!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Risk Management ────────────────────────
    {
        "keywords": ["risk", "risk management", "lot size", "lot", "how much invest",
                     "kitna invest", "safe", "money management", "capital"],
        "answer": (
            "⚖️ *Risk Management Guide*\n\n"
            "Proper risk management is *more important than signals!* 🔑\n\n"
            "📌 *Golden Rules:*\n"
            "• Risk only *1–2% per trade* of your account\n"
            "• Always use Stop Loss — no exceptions\n"
            "• Never risk more than 5% on open trades total\n"
            "• Don't overtrade — quality over quantity\n\n"
            "📊 *Lot size formula:*\n"
            "`Lot = (Account × Risk%) ÷ (SL pips × pip value)`\n\n"
            "💡 Example: $1000 account, 1% risk, 30-pip SL = *0.03 lots*"
            + RISK_DISCLAIMER
        ),
    },

    # ── Beginner ───────────────────────────────
    {
        "keywords": ["beginner", "new", "newbie", "start trading", "learning",
                     "how to trade", "trading sikhna", "kaise trade kare", "basic"],
        "answer": (
            "🎓 *Are You a Beginner?*\n\n"
            "Welcome! Everyone starts somewhere. ❤️\n\n"
            "📚 *For Beginners — Start Here:*\n"
            "1️⃣ Learn basics: Candlesticks, Support & Resistance\n"
            "2️⃣ Understand Forex/Gold charts on MT4/MT5\n"
            "3️⃣ Open a *free demo account* (no real money)\n"
            "4️⃣ Follow our signals on demo for 2–4 weeks\n"
            "5️⃣ Start live trading with small amount ($100–$200)\n\n"
            "📚 Join *Zorro Education* for in-depth chart studies!"
            + RISK_DISCLAIMER
        ),
    },
    {
        "keywords": ["demo", "demo account", "practice", "paper trading",
                     "demo trade", "virtual money"],
        "answer": (
            "🧪 *Demo Account Trading*\n\n"
            "We *strongly recommend* starting with a demo account! ✅\n\n"
            "📌 *Benefits of Demo First:*\n"
            "• Zero risk — virtual money only\n"
            "• Learn to execute signals correctly\n"
            "• Build confidence before going live\n"
            "• Test your broker's platform\n\n"
            "💡 Demo trade for minimum 2–4 weeks before going live.\n\n"
            "⚠️ Don't rush — patience is key in trading!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Platform & App ─────────────────────────
    {
        "keywords": ["app", "platform", "which app", "download", "metatrader",
                     "trading app", "mobile app", "kaunsa app"],
        "answer": (
            "📱 *Which Trading App to Use?*\n\n"
            "We recommend *MetaTrader 4 (MT4)* or *MetaTrader 5 (MT5)*:\n\n"
            "✅ *MT4* — Classic, simple, widely supported\n"
            "✅ *MT5* — Advanced, more timeframes, better charts\n\n"
            "📥 *Download:*\n"
            "Search 'MetaTrader 4' or 'MetaTrader 5' on Google Play / App Store\n\n"
            "🛠 Also check *Zorro Forex Tools* for custom MT5 indicators & EAs!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Withdrawal ─────────────────────────────
    {
        "keywords": ["withdraw", "withdrawal", "payout", "money out", "profit nikalo",
                     "how to withdraw", "payment method", "bank transfer"],
        "answer": (
            "💳 *Withdrawal Questions*\n\n"
            "Withdrawal depends on your *broker's policies* — "
            "we are a signal provider, not a broker.\n\n"
            "📌 *General Tips:*\n"
            "• Most brokers process in 1–5 business days\n"
            "• Methods: Bank transfer, Skrill, Neteller, Crypto, UPI\n"
            "• Always complete KYC before withdrawing\n\n"
            "⚠️ *We NEVER ask you to deposit money with us directly.*\n"
            "All trading is done on your own broker account."
            + RISK_DISCLAIMER
        ),
    },

    # ── Scam / Trust ───────────────────────────
    {
        "keywords": ["scam", "fraud", "fake", "trust", "legit", "real", "genuine",
                     "safe", "trustworthy", "verified", "real or fake"],
        "answer": (
            "🛡️ *Is Zorro Trading Legit?*\n\n"
            "We understand your concern. Here's why you can *trust us:*\n\n"
            "✅ All signals posted with full results & screenshots\n"
            "✅ *Free service* — we never ask for upfront deposits\n"
            "✅ Admin is reachable on Telegram\n"
            "✅ Transparent monthly performance reports\n\n"
            "⚠️ *Warning:* Beware of fake accounts impersonating us.\n"
            "Our *only official support* is linked below."
            + RISK_DISCLAIMER
        ),
    },

    # ── Signal Timing ──────────────────────────
    {
        "keywords": ["time", "market hours", "when signal", "signal time", "market open",
                     "kab signal", "trading hours", "when to trade"],
        "answer": (
            "🕐 *Signal Timing & Market Hours*\n\n"
            "📅 *Our Signal Schedule (IST):*\n"
            "• Morning Session:  *9:00 AM – 12:00 PM*\n"
            "• London Session:   *1:30 PM – 5:00 PM*\n"
            "• New York Session: *6:30 PM – 9:00 PM*\n\n"
            "📌 *Best hours:* London + New York overlap (6:30–9:00 PM IST)\n\n"
            "🔔 Enable channel notifications to catch signals in real-time!"
            + RISK_DISCLAIMER
        ),
    },

    # ── News Events ────────────────────────────
    {
        "keywords": ["news", "nfp", "cpi", "fomc", "fed", "economic news",
                     "news trading", "high impact", "event"],
        "answer": (
            "📰 *Trading During News Events*\n\n"
            "News events can cause *extreme volatility!* ⚡\n\n"
            "📌 *Key events we monitor:*\n"
            "• 🇺🇸 NFP — 1st Friday of every month\n"
            "• 📊 CPI — Monthly inflation data\n"
            "• 🏦 FOMC — Fed interest rate decisions\n\n"
            "⚠️ *Our policy:* We avoid trading 30 min before/after major news, "
            "or send special *'news trade'* alerts when appropriate."
            + RISK_DISCLAIMER
        ),
    },

    # ── Contact Admin ──────────────────────────
    {
        "keywords": ["admin", "contact", "support", "help", "customer service",
                     "talk to human", "speak to someone", "real person",
                     "contact admin", "admin se baat"],
        "answer": (
            "📞 *Contact Our Support*\n\n"
            "Our team is *available 7 days a week* to help you! 💪\n\n"
            "⏰ *Support Hours:*\n"
            "Monday–Saturday: *9:00 AM – 9:00 PM IST*\n"
            "Sunday: *10:00 AM – 5:00 PM IST*\n\n"
            "💬 Telegram: Fast response (usually within 1 hour)\n\n"
            "Tap below to connect now 👇"
        ),
    },

    # ── Capital Needed ─────────────────────────
    {
        "keywords": ["minimum deposit", "minimum balance", "how much money",
                     "kitna paisa chahiye", "starting capital", "how much to start",
                     "minimum capital", "small account"],
        "answer": (
            "💵 *How Much Capital Do I Need?*\n\n"
            "You can start with as little as *$100!* 💡\n\n"
            "📊 *Suggested Starting Amounts:*\n"
            "• Beginner:     $100 – $500\n"
            "• Intermediate: $500 – $2,000\n"
            "• Serious:      $2,000+\n\n"
            "⚠️ *Important:* Only trade money you can afford to lose.\n"
            "Never use emergency funds or loans for trading."
            + RISK_DISCLAIMER
        ),
    },

    # ── Copy Trading ───────────────────────────
    {
        "keywords": ["copy trade", "copy trading", "auto trade", "automated",
                     "copy signal", "auto copy", "mirror trade"],
        "answer": (
            "🤖 *Copy Trading / Auto-Follow*\n\n"
            "You can follow our signals manually or set up auto-copy! ✅\n\n"
            "📌 *Options:*\n"
            "• *MT4/MT5 Copy Trade* — Mirror our signal account\n"
            "• *Telegram Auto-Copy bots* — Auto-place trades from signals\n"
            "• *Manual copy* — Signals formatted for easy manual entry\n\n"
            "🛠 Check *Zorro Forex Tools* for ready-made MT5 EAs & tools!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Guarantee / Refund ─────────────────────
    {
        "keywords": ["refund", "guarantee", "money back", "loss cover",
                     "guarantee profit", "sure profit", "guaranteed"],
        "answer": (
            "⚠️ *About Profit Guarantees*\n\n"
            "We want to be *100% honest* with you:\n\n"
            "❌ *No one can guarantee profits in trading.*\n"
            "Anyone who claims guaranteed profits is a scammer!\n\n"
            "✅ *What we DO provide:*\n"
            "• High-quality, well-researched signals\n"
            "• Full transparency in results\n"
            "• Defined risk on every trade (SL always included)\n"
            "• Dedicated support for all questions"
            + RISK_DISCLAIMER
        ),
    },

    # ── Referral ───────────────────────────────
    {
        "keywords": ["referral", "refer", "invite", "affiliate", "earn",
                     "commission", "refer friend", "earn money", "referral program"],
        "answer": (
            "🤝 *Referral / Affiliate Program*\n\n"
            "Yes! We have a *referral program* for our community! 🎉\n\n"
            "💰 *How it works:*\n"
            "• Refer a friend who joins our VIP plan\n"
            "• Earn commission for every successful referral\n"
            "• No limit on referrals!\n\n"
            "💬 Contact support to join the affiliate program!"
            + RISK_DISCLAIMER
        ),
    },

    # ── Social Media ───────────────────────────
    {
        "keywords": ["tiktok", "instagram", "youtube", "social media",
                     "follow", "social", "youtube channel"],
        "answer": (
            "📲 *Follow Us*\n\n"
            "Stay connected with Zorro Trading! 🌐\n\n"
            "📢 *Zorro AI Channel* — Free signals daily\n"
            "📚 *Zorro Education* — Chart studies & market material\n"
            "🛠 *Zorro Forex Tools* — EAs, indicators & techniques\n\n"
            "All links are below 👇"
        ),
    },
]


# ─────────────────────────────────────────────
#  🤖  FALLBACK RESPONSE
# ─────────────────────────────────────────────

FALLBACK_RESPONSE = (
    "🤔 *Hmm, I didn't quite get that!*\n\n"
    "I'm here to help with questions about:\n"
    "📊 Trading signals & analysis\n"
    "💱 Forex, Gold, Crypto & Indices\n"
    "💰 Membership & pricing\n"
    "🏦 Broker recommendations\n"
    "⚖️ Risk management\n"
    "🎓 Beginner guidance\n"
    "🛠 MT5 tools & EAs\n\n"
    "💡 *Try asking:*\n"
    "_'How do I join?'_\n"
    "_'What markets do you cover?'_\n"
    "_'Is this free?'_\n\n"
    "👇 Or connect directly with our team:"
)


# ─────────────────────────────────────────────
#  🔍  KEYWORD MATCHING ENGINE
# ─────────────────────────────────────────────

def find_faq_answer(user_text: str) -> str:
    text_lower = user_text.lower().strip()
    best_match = None
    best_score = 0

    for faq in FAQ_DATA:
        score = sum(1 for kw in faq["keywords"] if kw in text_lower)
        if score > best_score:
            best_score = score
            best_match = faq

    if best_match and best_score > 0:
        return best_match["answer"]

    return FALLBACK_RESPONSE


# ─────────────────────────────────────────────
#  📨  TELEGRAM HANDLER
# ─────────────────────────────────────────────

async def faq_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text or ""
    answer    = find_faq_answer(user_text)

    await update.message.reply_text(
        answer,
        parse_mode="Markdown",
        reply_markup=contact_keyboard(),
    )
