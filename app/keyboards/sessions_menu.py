from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def sessions_menu(sessions):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    for session in sessions:
        keyboard.row(KeyboardButton(session["title"]))

    keyboard.row(KeyboardButton("🔙 بازگشت به منوی اصلی"))

    return keyboard


def session_details_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(KeyboardButton("📝 ثبت‌نام در نشست"))
    keyboard.row(KeyboardButton("🔙 بازگشت به نشست‌های علمی"))

    return keyboard


def session_cancel_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("❌ انصراف"))
    return keyboard


def session_phone_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton(
            "📱 ارسال شماره تلفن",
            request_contact=True
        )
    )
    keyboard.row(KeyboardButton("❌ انصراف"))

    return keyboard


def session_major_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("مهندسی کامپیوتر"),
        KeyboardButton("حسابداری")
    )
    keyboard.row(
        KeyboardButton("روانشناسی"),
        KeyboardButton("حقوق")
    )
    keyboard.row(
        KeyboardButton("مدیریت بازرگانی"),
        KeyboardButton("ادبیات زبان انگلیسی")
    )
    keyboard.row(KeyboardButton("❌ انصراف"))

    return keyboard