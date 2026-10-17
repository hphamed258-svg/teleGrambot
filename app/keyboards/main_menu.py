from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    workshops_button = KeyboardButton("🛠 کارگاه‌ها")
    courses_button = KeyboardButton("📚 دوره‌ها")
    competitions_button = KeyboardButton("🏆 مسابقات")
    sessions_button = KeyboardButton("🎙️ نشست‌های علمی")
    feedback_button = KeyboardButton("💡 پیشنهادات و انتقادات")
    cooperation_button = KeyboardButton("🤝 همکاری با ما")
    festivals_button = KeyboardButton("🎉 جشن‌ها")

    keyboard.row(workshops_button, courses_button)
    keyboard.row(competitions_button, sessions_button)
    keyboard.row(feedback_button, cooperation_button)
    keyboard.row(festivals_button)

    return keyboard