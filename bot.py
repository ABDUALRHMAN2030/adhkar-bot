import os, random
from telegram import Bot
from telegram.constants import ParseMode

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

if not BOT_TOKEN or not CHANNEL_ID:
    raise SystemExit("Please set BOT_TOKEN and CHANNEL_ID as repo secrets")

bot = Bot(BOT_TOKEN)

adhkar_morning = [
    "أصبحنا وأصبح الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له...",
    "اللهم بك أصبحنا وبك أمسينا وبك نحيا وبك نموت وإليك النشور.",
    "سبحان الله وبحمده عدد خلقه ورضا نفسه وزنة عرشه ومداد كلماته."
]

adhkar_evening = [
    "أمسينا وأمسى الملك لله، والحمد لله، لا إله إلا الله وحده لا شريك له...",
    "اللهم بك أمسينا وبك أصبحنا وبك نحيا وبك نموت وإليك المصير.",
    "أعوذ بكلمات الله التامات من شر ما خلق."
]

short_duas = [
    "ربنا آتنا في الدنيا حسنة وفي الآخرة حسنة وقِنا عذاب النار.",
    "اللهم صلِّ على محمد وعلى آل محمد.",
    "اللهم اغفر لي ولوالديَّ وللمؤمنين والمؤمنات.",
    "اللهم ارزقنا حسن الخاتمة.",
    "اللهم اجعل القرآن ربيع قلوبنا."
]

friday_salat = [
    "اللهم صلِّ وسلِّم على نبينا محمد 🌿",
    "إن الله وملائكته يصلون على النبي، يا أيها الذين آمنوا صلّوا عليه وسلّموا تسليماً ﷺ"
]

def post(text):
    footer = "\n\n— 🤍 نشر تلقائي للأذكار"
    bot.send_message(chat_id=CHANNEL_ID, text=text + footer,
                     parse_mode=ParseMode.HTML, disable_web_page_preview=True)

def run_job(kind):
    if kind == "morning":
        post(random.choice(adhkar_morning))
    elif kind == "evening":
        post(random.choice(adhkar_evening))
    elif kind == "short":
        post(random.choice(short_duas))
    elif kind == "friday":
        post(random.choice(friday_salat))
    else:
        print("نوع غير معروف:", kind)

if __name__ == "__main__":
    import sys
    run_job(sys.argv[1] if len(sys.argv) > 1 else "morning")
