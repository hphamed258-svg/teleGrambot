from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    workshops_button = KeyboardButton("🛠 کارگاه‌ها")
    courses_button = KeyboardButton("📚 دوره‌ها")

    competitions_button = KeyboardButton("🏆 مسابقات")
    feedback_button = KeyboardButton("💡 پیشنهادات و انتقادات")

    cooperation_button = KeyboardButton("🤝 همکاری با ما")

    keyboard.row(
        workshops_button,
        courses_button
    )

    keyboard.row(
        competitions_button,
        feedback_button
    )

    keyboard.row(
        cooperation_button
    )

    return keyboard