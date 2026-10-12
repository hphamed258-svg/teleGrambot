
from pathlib import Path

from telebot import TeleBot

from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.sessions_menu import (
    sessions_menu,
    session_details_menu,
    session_cancel_menu,
    session_phone_menu,
    session_degree_menu,
    session_entry_year_menu,
)


SESSIONS = {
    "first_session": {
        "title": "💻 سیری در جهان کامپیوتر | فصل دوم، قسمت اول",
        "text": (
            "💻 سیری در جهان کامپیوتر\n\n"
            "فصل دوم، قسمت اول"
        ),
        "poster": "first_session.jpg",
    },
}

ASSETS_PATH = Path(__file__).resolve().parents[1] / "assets"

DEGREES = [
    "کارشناسی",
    "کارشناسی ارشد",
    "دکترا",
]

ENTRY_YEARS = [
    "۴۰۲ ورودی",
    "۴۰۳ ورودی",
    "۴۰۴ ورودی",
    "ورودی ۴۰۱ یا پایین‌تر",
]

selected_sessions = {}
registration_data = {}


def register_sessions_handler(bot: TeleBot):

    # نمایش فهرست نشست‌ها
    @bot.message_handler(
        func=lambda message: message.text == "🎙️ نشست‌های علمی"
    )
    def show_sessions(message):
        bot.send_message(
            message.chat.id,
            "🎙️ لطفاً نشست موردنظر خود را انتخاب کنید:",
            reply_markup=sessions_menu(list(SESSIONS.values())),
        )

    # بازگشت به منوی اصلی
    @bot.message_handler(
        func=lambda message: message.text == "🔙 بازگشت به منوی اصلی"
    )
    def back_to_main(message):
        user_id = message.from_user.id
        selected_sessions.pop(user_id, None)
        registration_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتید.",
            reply_markup=main_menu(),
        )

    # نمایش جزئیات نشست
    @bot.message_handler(
        func=lambda message: message.text in [
            session["title"] for session in SESSIONS.values()
        ]
    )
    def show_session_details(message):
        user_id = message.from_user.id

        session_id = next(
            key
            for key, session in SESSIONS.items()
            if session["title"] == message.text
        )

        selected_sessions[user_id] = session_id
        session = SESSIONS[session_id]
        poster_path = ASSETS_PATH / session["poster"]

        if poster_path.is_file():
            with open(poster_path, "rb") as poster:
                bot.send_photo(
                    message.chat.id,
                    poster,
                    caption=session["text"],
                    reply_markup=session_details_menu(),
                )
        else:
            bot.send_message(
                message.chat.id,
                session["text"],
                reply_markup=session_details_menu(),
            )

    # بازگشت به فهرست نشست‌ها
    @bot.message_handler(
        func=lambda message: message.text == "🔙 بازگشت به نشست‌های علمی"
    )
    def back_to_sessions(message):
        user_id = message.from_user.id
        selected_sessions.pop(user_id, None)
        registration_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "🎙️ لطفاً نشست موردنظر خود را انتخاب کنید:",
            reply_markup=sessions_menu(list(SESSIONS.values())),
        )

    # شروع ثبت‌نام
    @bot.message_handler(
        func=lambda message: message.text == "📝 ثبت‌نام"
    )
    def start_registration(message):
        user_id = message.from_user.id
        session_id = selected_sessions.get(user_id)

        if session_id not in SESSIONS:
            bot.send_message(
                message.chat.id,
                "لطفاً ابتدا یک نشست را انتخاب کنید.",
                reply_markup=main_menu(),
            )
            return

        registration_data[user_id] = {
            "session_id": session_id,
        }

        bot.send_message(
            message.chat.id,
            "لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=session_cancel_menu(),
        )

        bot.register_next_step_handler(message, get_name, session_id)

    # دریافت نام
    def get_name(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.text or not message.text.strip():
            bot.send_message(
                message.chat.id,
                "لطفاً نام و نام خانوادگی خود را وارد کنید.",
                reply_markup=session_cancel_menu(),
            )
            bot.register_next_step_handler(message, get_name, session_id)
            return

        registration_data[user_id]["name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "لطفاً شماره تلفن خود را با دکمه زیر ارسال کنید:",
            reply_markup=session_phone_menu(),
        )

        bot.register_next_step_handler(message, get_phone, session_id)

    # دریافت شماره تلفن
    def get_phone(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.contact:
            bot.send_message(
                message.chat.id,
                "لطفاً از دکمه «📱 ارسال شماره تلفن» استفاده کنید.",
                reply_markup=session_phone_menu(),
            )
            bot.register_next_step_handler(message, get_phone, session_id)
            return

        if (
            message.contact.user_id is not None
            and message.contact.user_id != user_id
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً شماره تلفن خودتان را ارسال کنید.",
                reply_markup=session_phone_menu(),
            )
            bot.register_next_step_handler(message, get_phone, session_id)
            return

        registration_data[user_id]["phone"] = (
            message.contact.phone_number
        )

        bot.send_message(
            message.chat.id,
            "لطفاً مقطع تحصیلی خود را انتخاب کنید:",
            reply_markup=session_degree_menu(),
        )

        bot.register_next_step_handler(message, get_degree, session_id)

    # دریافت مقطع تحصیلی
    def get_degree(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if message.text not in DEGREES:
            bot.send_message(
                message.chat.id,
                "لطفاً مقطع تحصیلی خود را از گزینه‌ها انتخاب کنید.",
                reply_markup=session_degree_menu(),
            )
            bot.register_next_step_handler(message, get_degree, session_id)
            return

        registration_data[user_id]["degree"] = message.text

        bot.send_message(
            message.chat.id,
            "لطفاً سال ورودی خود را انتخاب کنید:",
            reply_markup=session_entry_year_menu(),
        )

        bot.register_next_step_handler(
            message,
            get_entry_year,
            session_id,
        )

    # دریافت سال ورودی
    def get_entry_year(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if message.text not in ENTRY_YEARS:
            bot.send_message(
                message.chat.id,
                "لطفاً سال ورودی خود را از گزینه‌ها انتخاب کنید.",
                reply_markup=session_entry_year_menu(),
            )
            bot.register_next_step_handler(
                message,
                get_entry_year,
                session_id,
            )
            return

        registration_data[user_id]["entry_year"] = message.text

        send_registration_to_admin(message, session_id)

    # ارسال اطلاعات برای ادمین
    def send_registration_to_admin(message, session_id):
        user_id = message.from_user.id
        user = message.from_user
        data = registration_data[user_id]
        session = SESSIONS[session_id]

        username = f"@{user.username}" if user.username else "ندارد"

        admin_message = (
            "🎙️ ثبت‌نام جدید در نشست علمی\n\n"
            f"📌 عنوان نشست: {session['title']}\n"
            f"👤 نام و نام خانوادگی: {data['name']}\n"
            f"🔗 نام کاربری: {username}\n"
            f"🆔 شناسه تلگرام: {user.id}\n"
            f"📱 شماره تلفن: {data['phone']}\n"
            f"🎓 مقطع تحصیلی: {data['degree']}\n"
            f"📚 سال ورودی: {data['entry_year']}"
        )

        try:
            if not ADMIN_ID:
                raise ValueError("ADMIN_ID تنظیم نشده است.")

            bot.send_message(ADMIN_ID, admin_message)

        except Exception:
            bot.send_message(
                message.chat.id,
                "❌ ثبت‌نام انجام نشد. لطفاً بعداً دوباره تلاش کنید.",
                reply_markup=main_menu(),
            )
            registration_data.pop(user_id, None)
            selected_sessions.pop(user_id, None)
            return

        registration_data.pop(user_id, None)
        selected_sessions.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "✅ ثبت‌نام شما با موفقیت انجام شد.",
            reply_markup=main_menu(),
        )

    # لغو ثبت‌نام
    def is_cancel(message):
        if message.text == "❌ انصراف":
            user_id = message.from_user.id

            registration_data.pop(user_id, None)
            selected_sessions.pop(user_id, None)

            bot.send_message(
                message.chat.id,
                "ثبت‌نام لغو شد.",
                reply_markup=main_menu(),
            )
            return True

        return False
