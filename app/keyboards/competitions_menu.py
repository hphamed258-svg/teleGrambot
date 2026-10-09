from telebot.types import ReplyKeyboardMarkup, KeyboardButton

COMPETITION_TITLE = "🎨 سی‌رنگ"

def competitions_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


    keyboard.row(KeyboardButton(COMPETITION_TITLE))
    keyboard.row(KeyboardButton("🔙 بازگشت به منوی اصلی"))

    return keyboard


def competition_details_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


    keyboard.row(KeyboardButton("📝 ثبت‌نام در مسابقه"))
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))

    return keyboard


def cancel_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


    keyboard.row(KeyboardButton("❌ انصراف"))

    return keyboard


def phone_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)


    keyboard.row(
        KeyboardButton(
            "📱 ارسال شماره تلفن",
            request_contact=True
        )
    )
    keyboard.row(KeyboardButton("❌ انصراف"))

    return keyboard


def major_menu():
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

