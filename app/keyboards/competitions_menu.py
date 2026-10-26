
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


COMPETITION_TITLE = "🎨 سی‌رنگ"
MINI_ARC_TITLE = "🧠 مسابقه مقدماتی آرک (مینی آرک)"


def competitions_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(KeyboardButton(COMPETITION_TITLE))
    keyboard.row(KeyboardButton(MINI_ARC_TITLE))
    keyboard.row(KeyboardButton("🔙 بازگشت به منوی اصلی"))

    return keyboard


def competition_details_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(KeyboardButton("📝 ثبت‌نام در مسابقه"))
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))
    keyboard.row(KeyboardButton("🏠 منوی اصلی"))

    return keyboard


def cancel_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(KeyboardButton("❌ انصراف"))
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))
    keyboard.row(KeyboardButton("🏠 منوی اصلی"))

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
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))
    keyboard.row(KeyboardButton("🏠 منوی اصلی"))

    return keyboard


def entry_year_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("ورودی 401"),
        KeyboardButton("ورودی 402")
    )
    keyboard.row(
        KeyboardButton("ورودی 403"),
        KeyboardButton("ورودی 404")
    )
    keyboard.row(KeyboardButton("❌ انصراف"))
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))
    keyboard.row(KeyboardButton("🏠 منوی اصلی"))

    return keyboard


def retry_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(KeyboardButton("🔄 تلاش مجدد برای ثبت‌نام"))
    keyboard.row(KeyboardButton("❌ انصراف"))
    keyboard.row(KeyboardButton("🔙 بازگشت به مسابقات"))
    keyboard.row(KeyboardButton("🏠 منوی اصلی"))

    return keyboard
