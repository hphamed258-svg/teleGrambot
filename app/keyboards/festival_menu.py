
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def festival_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("🎨 جشنواره رنگ و شور")
    )
    keyboard.row(
        KeyboardButton("🔙 بازگشت به منوی اصلی")
    )

    return keyboard


def festival_detail_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("📝 ثبت‌نام جشنواره")
    )
    keyboard.row(
        KeyboardButton("🔙 بازگشت به جشن‌ها")
    )
    keyboard.row(
        KeyboardButton("🏠 منوی اصلی")
    )

    return keyboard


def degree_menu():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("کاردانی"),
        KeyboardButton("کارشناسی")
    )
    keyboard.row(
        KeyboardButton("کارشناسی ارشد"),
        KeyboardButton("دکترا")
    )
    keyboard.row(
        KeyboardButton("❌ لغو ثبت‌نام")
    )

    return keyboard


def cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("❌ لغو ثبت‌نام")
    )

    return keyboard


def phone_keyboard():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )

    keyboard.row(
        KeyboardButton(
            "📱 ارسال شماره تماس",
            request_contact=True
        )
    )
    keyboard.row(
        KeyboardButton("❌ لغو ثبت‌نام")
    )

    return keyboard


def retry_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.row(
        KeyboardButton("🔄 تلاش مجدد برای ثبت‌نام")
    )
    keyboard.row(
        KeyboardButton("❌ لغو ثبت‌نام")
    )

    return keyboard
