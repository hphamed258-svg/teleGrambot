from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def cooperation_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    education_button = KeyboardButton("📚 امور آموزشی")
    executive_button = KeyboardButton("⚙️ امور اجرایی")

    content_button = KeyboardButton("🎨 تولید محتوا")
    other_button = KeyboardButton("💡 سایر")

    back_button = KeyboardButton("🔙 بازگشت")

    keyboard.row(
        education_button,
        executive_button
    )

    keyboard.row(
        content_button,
        other_button
    )

    keyboard.row(
        back_button
    )

    return keyboard


def content_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    poster_button = KeyboardButton("🎨 طراحی پوستر")
    voice_button = KeyboardButton("🎙 گویندگی پادکست")

    audio_button = KeyboardButton("🎧 صداگذاری و ضبط پادکست")
    text_button = KeyboardButton("📝 تهیه متن پادکست")

    social_button = KeyboardButton("📱 مدیریت شبکه‌های اجتماعی")
    photo_button = KeyboardButton("📸 عکاسی و فیلم‌برداری")

    other_button = KeyboardButton("💡 سایر")
    back_button = KeyboardButton("🔙 بازگشت")

    keyboard.row(
        poster_button,
        voice_button
    )

    keyboard.row(
        audio_button,
        text_button
    )

    keyboard.row(
        social_button,
        photo_button
    )

    keyboard.row(
        other_button
    )

    keyboard.row(
        back_button
    )

    return keyboard


def cancel_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    cancel_button = KeyboardButton("❌ انصراف")

    keyboard.row(cancel_button)

    return keyboard


def phone_menu():
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    phone_button = KeyboardButton(
        "📱 ارسال شماره تلفن",
        request_contact=True
    )

    cancel_button = KeyboardButton("❌ انصراف")

    keyboard.row(phone_button)
    keyboard.row(cancel_button)

    return keyboard