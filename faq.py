# ═══════════════════════════════════════════════════════════════
#  faq.py — Zorro Trading Bot FAQ Engine
#  bot.py ke saath same folder mein rakho
# ═══════════════════════════════════════════════════════════════

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# ─────────────────────────────────────────────
# ⚙️  CONFIG — bot.py se match karo
# ─────────────────────────────────────────────

TG_CHANNEL_LINK = "https://t.me/+1GeEbtebtz81NjU8"
TG_ADMIN_LINK   = "https://t.me/abhaykushwaha1"
WA_CHANNEL_LINK = "https://whatsapp.com/channel/0029VbConbY6hENjNS8Ak51S"
WA_ADMIN_LINK   = "https://wa.me/+447848142501"


# ─────────────────────────────────────────────
# 🔘  CONTACT KEYBOARD
# ─────────────────────────────────────────────

def contact_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💬 Telegram Admin",    url=TG_ADMIN_LINK),
         InlineKeyboardButton("🟢 WhatsApp Admin",   url=WA_ADMIN_LINK)],
        [InlineKeyboardButton("📢 Join Free Channel", url=TG_CHANNEL_LINK)],
    ])


# ─────────────────────────────────────────────
# 📚  FAQ DATABASE
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
            "✅ Take Profit 1, 2 & 3 (TP)\n"
            "✅ Signal reasoning & analysis\n\n"
            "📈 Our signals have *85%+ win rate* this month.\n\n"
            "🔔 *Join our free channel* to receive signals directly on your phone!\n\n"
            "❓ Still have questions? Contact our admin 👇"
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
            "💡 On high-volatility days (NFP, CPI, FOMC), we may send extra alerts!\n\n"
            "📢 Join our free channel to never miss a signal!\n\n"
            "❓ Want a custom signal plan? Contact admin 👇"
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
            "💡 Tip: Enable notifications so you never miss one!\n\n"
            "❓ Need help accessing old signals? Contact admin 👇"
        ),
    },

    # ── Win Rate & Results ─────────────────────
    {
        "keywords": ["win rate", "winrate", "accuracy", "success rate", "hit rate",
                     "how accurate", "kitna accurate", "profit"],
        "answer": (
            "🎯 *Our Win Rate & Accuracy*\n\n"
            "📈 *Current Month Win Rate: 85%+*\n\n"
            "📊 Monthly Stats:\n"
            "• Total Signals Sent: 60–80/month\n"
            "• Average Win: 50–120 pips\n"
            "• Average Loss: 20–35 pips\n"
            "• Risk:Reward Ratio: 1:2 to 1:3\n\n"
            "✅ Full monthly results are posted on our channel with screenshots.\n\n"
            "⚠️ *Disclaimer:* Past performance doesn't guarantee future results. "
            "Always trade with proper risk management.\n\n"
            "❓ Want detailed stats? Contact admin 👇"
        ),
    },
    {
        "keywords": ["result", "results", "performance", "track record",
                     "proof", "screenshot", "verified"],
        "answer": (
            "📊 *Our Track Record & Proof*\n\n"
            "We believe in *full transparency!* 🔍\n\n"
            "✅ Every signal result is posted with *broker screenshots*\n"
            "✅ Monthly P&L reports shared publicly\n"
            "✅ Live trade updates in real-time\n"
            "✅ Independent verification by community members\n\n"
            "📢 Check our channel history for all past results!\n\n"
            "❓ Want to verify a specific result? Contact admin 👇"
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
            "💬 For VIP pricing & details, contact our admin directly!\n\n"
            "❓ Questions about plans? Contact admin 👇"
        ),
    },
    {
        "keywords": ["vip", "premium", "paid plan", "pro plan", "upgrade",
                     "vip plan", "vip signals", "paid signals"],
        "answer": (
            "👑 *VIP / Premium Membership*\n\n"
            "Our VIP plan gives you an *unfair trading advantage!* ⚡\n\n"
            "🔥 VIP Benefits:\n"
            "• 5–8 signals per day (vs 2–4 free)\n"
            "• Early entry alerts (before free channel)\n"
            "• Exclusive setups & analysis\n"
            "• Personal 1-on-1 mentoring sessions\n"
            "• Weekly live trading sessions\n"
            "• Portfolio & risk management review\n"
            "• Dedicated support line\n\n"
            "💬 *Contact admin for current pricing & offers!*\n\n"
            "❓ Ready to upgrade? Contact admin 👇"
        ),
    },

    # ── How to Join ────────────────────────────
    {
        "keywords": ["join", "how to join", "kaise join", "register", "sign up",
                     "subscribe", "kaise subscribe", "channel join"],
        "answer": (
            "✅ *How to Join Zorro Trading Community*\n\n"
            "Joining is *super easy & free!* Here's how:\n\n"
            "1️⃣ Click the *'Join Free Channel'* button below\n"
            "2️⃣ Press *'Join'* on the Telegram channel\n"
            "3️⃣ Enable notifications 🔔\n"
            "4️⃣ Start receiving free daily signals!\n\n"
            "📱 *Also available on WhatsApp!*\n"
            "Just click the WhatsApp button to join our WhatsApp channel.\n\n"
            "❓ Need help joining? Contact admin 👇"
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
            "🥇 *Gold:* XAU/USD — Daily signals\n"
            "₿ *Crypto:* BTC · ETH · XRP · SOL\n"
            "📊 *Indices:* US30 · SPX500 · NAS100\n\n"
            "✅ Entry · SL · TP on every signal\n"
            "✅ 85%+ win rate across all pairs\n\n"
            "❓ Want signals for a specific pair? Contact admin 👇"
        ),
    },

    # ── Broker ─────────────────────────────────
    {
        "keywords": ["broker", "which broker", "best broker", "recommended broker",
                     "broker suggest", "which platform", "mt4", "mt5", "metatrader"],
        "answer": (
            "🏦 *Which Broker Should I Use?*\n\n"
            "We are *broker-independent* — our signals work on any broker! ✅\n\n"
            "📌 *We recommend brokers with:*\n"
            "• Low spread on major pairs\n"
            "• Fast execution (no requotes)\n"
            "• MT4 or MT5 platform support\n"
            "• Regulated (FCA, CySEC, ASIC)\n\n"
            "💡 *Popular choices among our members:*\n"
            "XM, Exness, IC Markets, Pepperstone, FBS\n\n"
            "⚠️ Always verify regulation before depositing!\n\n"
            "❓ Need broker advice for your country? Contact admin 👇"
        ),
    },

    # ── Risk Management ────────────────────────
    {
        "keywords": ["risk", "risk management", "lot size", "lot", "how much invest",
                     "kitna invest", "safe", "money management", "capital"],
        "answer": (
            "⚖️ *Risk Management Guide*\n\n"
            "Proper risk management is *more important than signals!* 🔑\n\n"
            "📌 *Golden Rules we follow:*\n"
            "• Risk only *1–2% per trade* of your account\n"
            "• Always use Stop Loss — no exceptions\n"
            "• Never risk more than 5% on open trades total\n"
            "• Don't overtrade — quality over quantity\n\n"
            "📊 *Lot size formula:*\n"
            "`Lot = (Account × Risk%) ÷ (SL in pips × pip value)`\n\n"
            "💡 Example: $1000 account, 1% risk, 30-pip SL = *0.03 lots*\n\n"
            "🎓 Want a full risk management course? Contact admin!\n\n"
            "❓ Need personalized advice? Contact admin 👇"
        ),
    },

    # ── Beginner ───────────────────────────────
    {
        "keywords": ["beginner", "new", "newbie", "start trading", "learning",
                     "how to trade", "trading sikhna", "kaise trade kare", "basic"],
        "answer": (
            "🎓 *Are You a Beginner?*\n\n"
            "Welcome! Everyone starts somewhere. We *love helping beginners!* ❤️\n\n"
            "📚 *For Beginners — Start Here:*\n"
            "1️⃣ Learn basics: Candlesticks, Support & Resistance\n"
            "2️⃣ Understand Forex/Gold charts on MT4/MT5\n"
            "3️⃣ Open a *free demo account* (no real money)\n"
            "4️⃣ Follow our signals on demo for 2–4 weeks\n"
            "5️⃣ Start live trading with small amount ($100–$200)\n\n"
            "💡 We offer a *FREE beginner's trading guide* for new members!\n\n"
            "🎓 Contact admin to get your free guide & personal mentoring!\n\n"
            "❓ Any beginner questions? Contact admin 👇"
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
            "• Learn to execute our signals correctly\n"
            "• Build confidence before going live\n"
            "• Test your broker's platform\n\n"
            "💡 *How long to demo trade?*\n"
            "Minimum 2–4 weeks OR until you hit 70%+ win rate consistently.\n\n"
            "⚠️ Don't rush to go live — patience is key in trading!\n\n"
            "❓ Ready to go live? Contact admin for guidance 👇"
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
            "• Search 'MetaTrader 4' or 'MetaTrader 5' on Google Play / App Store\n"
            "• Available on Android, iOS, Windows & Mac\n\n"
            "💡 After installing, open an account with any recommended broker!\n\n"
            "❓ Need setup help? Contact admin 👇"
        ),
    },

    # ── Withdrawal ─────────────────────────────
    {
        "keywords": ["withdraw", "withdrawal", "payout", "money out", "profit nikalo",
                     "how to withdraw", "payment method", "bank transfer"],
        "answer": (
            "💳 *Withdrawal Questions*\n\n"
            "Withdrawal depends on your *broker's policies*, not us — "
            "we are a signal provider, not a broker.\n\n"
            "📌 *General Withdrawal Tips:*\n"
            "• Most brokers process in 1–5 business days\n"
            "• Minimum withdrawal varies by broker ($5–$50)\n"
            "• Methods: Bank transfer, Skrill, Neteller, Crypto, UPI (India)\n"
            "• Always verify KYC before withdrawing\n\n"
            "⚠️ *We NEVER ask you to deposit money with us directly!*\n"
            "All trading is done on your own broker account.\n\n"
            "❓ Need broker-specific withdrawal help? Contact admin 👇"
        ),
    },

    # ── Scam / Trust ───────────────────────────
    {
        "keywords": ["scam", "fraud", "fake", "trust", "legit", "real", "genuine",
                     "safe", "trustworthy", "verified", "real or fake"],
        "answer": (
            "🛡️ *Is Zorro Trading Legit?*\n\n"
            "We understand your concern — the internet has many scammers. "
            "Here's why you can *trust us:*\n\n"
            "✅ 10,000+ active community members\n"
            "✅ All signals posted with full results & screenshots\n"
            "✅ *Free service* — we never ask for upfront deposits\n"
            "✅ Admin is reachable on Telegram & WhatsApp\n"
            "✅ Transparent monthly performance reports\n"
            "✅ Real community — check member testimonials\n\n"
            "⚠️ *Warning:* Beware of fake accounts impersonating us. "
            "Our *only official admin* is linked below.\n\n"
            "❓ Need more verification? Contact *official* admin 👇"
        ),
    },

    # ── Signal Timing ──────────────────────────
    {
        "keywords": ["time", "market hours", "when signal", "signal time", "market open",
                     "kab signal", "trading hours", "when to trade"],
        "answer": (
            "🕐 *Signal Timing & Market Hours*\n\n"
            "📅 *Our Signal Schedule (IST):*\n"
            "• Morning Session: *9:00 AM – 12:00 PM*\n"
            "• London Session: *1:30 PM – 5:00 PM*\n"
            "• New York Session: *6:30 PM – 9:00 PM*\n\n"
            "📌 *Best trading hours:*\n"
            "London + New York overlap (6:30–9:00 PM IST) — *highest volatility!*\n\n"
            "🔔 Enable channel notifications to catch signals in real-time!\n\n"
            "❓ Questions about timing? Contact admin 👇"
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
            "• 🇺🇸 NFP (Non-Farm Payrolls) — 1st Friday of month\n"
            "• 📊 CPI (Inflation data) — Monthly\n"
            "• 🏦 FOMC (Fed interest rate) — 8 times/year\n"
            "• 📈 DXY (Dollar Index) movements\n\n"
            "⚠️ *Our policy during high-impact news:*\n"
            "We either *avoid trading* 30 min before/after, "
            "or send special *'news trade'* alerts.\n\n"
            "❓ Want news calendar access? Contact admin 👇"
        ),
    },

    # ── Contact Admin ──────────────────────────
    {
        "keywords": ["admin", "contact", "support", "help", "customer service",
                     "talk to human", "speak to someone", "real person",
                     "contact admin", "admin se baat"],
        "answer": (
            "📞 *Contact Our Admin*\n\n"
            "Our admin is *available 7 days a week* to help you! 💪\n\n"
            "⏰ *Support Hours:*\n"
            "Monday–Saturday: *9:00 AM – 9:00 PM IST*\n"
            "Sunday: *10:00 AM – 5:00 PM IST*\n\n"
            "💬 *Ways to reach us:*\n"
            "• Telegram: Fast response (usually within 1 hour)\n"
            "• WhatsApp: For detailed queries & calls\n\n"
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
            "📊 *Recommended Starting Amounts:*\n"
            "• Beginner: $100 – $500\n"
            "• Intermediate: $500 – $2,000\n"
            "• Serious trader: $2,000+\n\n"
            "⚠️ *Important:* Only trade money you can afford to lose!\n"
            "Never use rent money, loans, or emergency funds for trading.\n\n"
            "💡 Start small, learn the process, then scale up gradually.\n\n"
            "❓ Need a personalized capital plan? Contact admin 👇"
        ),
    },

    # ── Copy Trading ───────────────────────────
    {
        "keywords": ["copy trade", "copy trading", "auto trade", "automated",
                     "copy signal", "auto copy", "mirror trade"],
        "answer": (
            "🤖 *Copy Trading / Auto-Follow*\n\n"
            "Great news — you can *copy our trades automatically!* ✅\n\n"
            "📌 *Options available:*\n"
            "• *MT4/MT5 Copy Trade* — Connect to our signal provider account\n"
            "• *Telegram Auto-Copy bots* — Automatically place trades from signals\n"
            "• *Manual copy* — Our signals are formatted for easy manual entry\n\n"
            "💡 *Recommended for busy people:* Telegram-to-MT5 auto-copy setup\n\n"
            "🎓 Admin can help you set up auto-copy step by step!\n\n"
            "❓ Want to set up auto-copy? Contact admin 👇"
        ),
    },

    # ── Guarantee / Refund ─────────────────────
    {
        "keywords": ["refund", "guarantee", "money back", "loss cover",
                     "guarantee profit", "sure profit", "guaranteed"],
        "answer": (
            "⚠️ *About Profit Guarantees*\n\n"
            "We want to be *100% honest* with you:\n\n"
            "❌ *No one can guarantee profits in trading.* Anyone who does is a scammer!\n\n"
            "✅ *What we DO guarantee:*\n"
            "• High-quality, well-researched signals\n"
            "• Full transparency in results\n"
            "• Consistent 80–85% win rate (historical)\n"
            "• Proper risk management on every signal\n"
            "• Dedicated support if you have questions\n\n"
            "❓ More questions about risk? Contact admin 👇"
        ),
    },

    # ── Referral ───────────────────────────────
    {
        "keywords": ["referral", "refer", "invite", "affiliate", "earn",
                     "commission", "refer friend", "earn money", "referral program"],
        "answer": (
            "🤝 *Referral / Affiliate Program*\n\n"
            "Yes! We have a *referral program* for our community members! 🎉\n\n"
            "💰 *How it works:*\n"
            "• Refer a friend who joins our VIP plan\n"
            "• Earn *commission* for every successful referral\n"
            "• No limit on referrals!\n\n"
            "💡 Many of our top affiliates earn ₹15,000–₹50,000/month!\n\n"
            "❓ Want to join the affiliate program? Contact admin 👇"
        ),
    },

    # ── Social Media ───────────────────────────
    {
        "keywords": ["tiktok", "instagram", "youtube", "social media",
                     "follow", "social", "youtube channel"],
        "answer": (
            "📲 *Follow Us on Social Media*\n\n"
            "Stay connected with Zorro Trading everywhere! 🌐\n\n"
            "🎵 *TikTok* — @zorrotrading\n"
            "  Daily market analysis & trading tips\n\n"
            "📢 *Telegram Channel* — Free signals daily\n\n"
            "💡 Our TikTok has *free trading education content* — "
            "perfect for beginners!\n\n"
            "❓ Partnership inquiry? Contact admin 👇"
        ),
    },
]


# ─────────────────────────────────────────────
# 🤖  FALLBACK RESPONSE
# ─────────────────────────────────────────────

FALLBACK_RESPONSE = (
    "🤔 *Hmm, I didn't quite get that!*\n\n"
    "I'm here to help with questions about:\n"
    "📊 Trading signals & win rate\n"
    "💱 Forex, Gold, Crypto & Indices\n"
    "💰 Membership & pricing\n"
    "🏦 Broker recommendations\n"
    "⚖️ Risk management\n"
    "🎓 Beginner guidance\n"
    "📱 Platform & app setup\n\n"
    "💡 *Try asking something like:*\n"
    "_'How do I join?'_\n"
    "_'What is your win rate?'_\n"
    "_'Is this free?'_\n\n"
    "👇 Or connect directly with our admin:"
)


# ─────────────────────────────────────────────
# 🔍  KEYWORD MATCHING ENGINE
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
# 📨  TELEGRAM HANDLER
# ─────────────────────────────────────────────

async def faq_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text or ""
    answer    = find_faq_answer(user_text)

    await update.message.reply_text(
        answer,
        parse_mode="Markdown",
        reply_markup=contact_keyboard(),
    )