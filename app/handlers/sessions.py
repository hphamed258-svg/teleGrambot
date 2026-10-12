from pathlib import Path

from telebot import TeleBot

from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.sessions_menu import (
    sessions_menu,
    session_details_menu,
    session_cancel_menu,
    session_phone_menu,
    session_major_menu,
)


# ==========================================
# اطلاعات نشست‌های علمی
# ==========================================

SESSIONS = {
    "first_session": {
        "title": "🎓 گفت‌وگو با استاد",
        "text": """
🎙️ نشست علمی انجمن مهندسی کامپیوتر

به‌زودی جزئیات این نشست اعلام می‌شود.

📅 تاریخ: به‌زودی اعلام می‌شود
⏰ ساعت: به‌زودی اعلام می‌شود
📍 مکان: پردیس مهریز

📝 برای شرکت در نشست، ثبت‌نام خود را تکمیل کنید.
""",
        "poster": "first_session.jpg",
    },

    # برای اضافه کردن نشست جدید، یک مورد دیگر
    # با همین ساختار به این دیکشنری اضافه کن.
    #
    # "ai_session": {
    #     "title": "🤖 گفت‌وگو درباره هوش مصنوعی",
    #     "text": """
    # توضیحات نشست جدید...
    # """,
    #     "poster": "ai_session.jpg",
    # },
}


ASSETS_PATH = Path(__file__).resolve().parents[1] / "assets"

MAJORS = [
    "مهندسی کامپیوتر",
    "حسابداری",
    "روانشناسی",
    "حقوق",
    "مدیریت بازرگانی",
    "ادبیات زبان انگلیسی",
]

# نشست انتخاب‌شده برای هر کاربر
selected_sessions = {}

# اطلاعات موقت فرم ثبت‌نام
registration_data = {}


def register_sessions_handler(bot: TeleBot):

    # --------------------------------------
    # نمایش منوی نشست‌های علمی
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == "🎙️ نشست‌های علمی"
    )
    def show_sessions(message):
        bot.send_message(
            message.chat.id,
            "🎙️ نشست‌های علمی\n\n"
            "لطفاً نشست موردنظر خود را انتخاب کنید:",
            reply_markup=sessions_menu(
                list(SESSIONS.values())
            )
        )

    # --------------------------------------
    # نمایش جزئیات نشست انتخاب‌شده
    # --------------------------------------

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
                    reply_markup=session_details_menu()
                )
        else:
            bot.send_message(
                message.chat.id,
                "⚠️ پوستر این نشست پیدا نشد.\n\n"
                + session["text"],
                reply_markup=session_details_menu()
            )

    # --------------------------------------
    # بازگشت به فهرست نشست‌ها
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: (
            message.text == "🔙 بازگشت به نشست‌های علمی"
        )
    )
    def back_to_sessions(message):
        selected_sessions.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            "🎙️ نشست‌های علمی\n\n"
            "لطفاً نشست موردنظر خود را انتخاب کنید:",
            reply_markup=sessions_menu(
                list(SESSIONS.values())
            )
        )

    # --------------------------------------
    # شروع ثبت‌نام
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: (
            message.text == "📝 ثبت‌نام در نشست"
        )
    )
    def start_registration(message):
        user_id = message.from_user.id
        session_id = selected_sessions.get(user_id)

        if session_id not in SESSIONS:
            bot.send_message(
                message.chat.id,
                "لطفاً ابتدا از منوی نشست‌های علمی، "
                "یک نشست را انتخاب کنید.",
                reply_markup=main_menu()
            )
            return

        registration_data[user_id] = {
            "session_id": session_id
        }

        bot.send_message(
            message.chat.id,
            f"📝 ثبت‌نام در {SESSIONS[session_id]['title']}\n\n"
            "👤 لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=session_cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_name,
            session_id
        )

    # --------------------------------------
    # دریافت نام و نام خانوادگی
    # --------------------------------------

    def get_name(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.text or not message.text.strip():
            bot.send_message(
                message.chat.id,
                "لطفاً نام و نام خانوادگی خود را وارد کنید.",
                reply_markup=session_cancel_menu()
            )
            bot.register_next_step_handler(
                message, get_name, session_id
            )
            return

        registration_data[user_id]["name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "📱 لطفاً شماره تلفن خود را با دکمه زیر ارسال کنید.",
            reply_markup=session_phone_menu()
        )

        bot.register_next_step_handler(
            message,
            get_phone,
            session_id
        )

    # --------------------------------------
    # دریافت شماره تلفن
    # --------------------------------------

    def get_phone(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.contact:
            bot.send_message(
                message.chat.id,
                "لطفاً از دکمه «📱 ارسال شماره تلفن» استفاده کنید.",
                reply_markup=session_phone_menu()
            )
            bot.register_next_step_handler(
                message, get_phone, session_id
            )
            return

        if (
            message.contact.user_id is not None
            and message.contact.user_id != user_id
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً شماره تلفن خودتان را ارسال کنید.",
                reply_markup=session_phone_menu()
            )
            bot.register_next_step_handler(
                message, get_phone, session_id
            )
            return

        registration_data[user_id]["phone"] = (
            message.contact.phone_number
        )

        bot.send_message(
            message.chat.id,
            "🎓 لطفاً رشته تحصیلی خود را انتخاب کنید:",
            reply_markup=session_major_menu()
        )

        bot.register_next_step_handler(
            message,
            get_major,
            session_id
        )

    # --------------------------------------
    # دریافت رشته تحصیلی
    # --------------------------------------

    def get_major(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if message.text not in MAJORS:
            bot.send_message(
                message.chat.id,
                "لطفاً رشته خود را از بین گزینه‌های زیر انتخاب کنید.",
                reply_markup=session_major_menu()
            )
            bot.register_next_step_handler(
                message, get_major, session_id
            )
            return

        registration_data[user_id]["major"] = message.text

        send_registration_to_admin(message, session_id)

    # --------------------------------------
    # ارسال اطلاعات به ادمین
    # --------------------------------------

    def send_registration_to_admin(message, session_id):
        user_id = message.from_user.id
        user = message.from_user
        data = registration_data[user_id]
        session = SESSIONS[session_id]

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        admin_message = (
            "🎙️ ثبت‌نام جدید در نشست علمی\n\n"
            f"📌 عنوان نشست: {session['title']}\n\n"
            f"👤 نام و نام خانوادگی: {data['name']}\n"
            f"🔗 نام کاربری: {username}\n"
            f"🆔 شناسه تلگرام: {user.id}\n"
            f"📱 شماره تلفن: {data['phone']}\n"
            f"🎓 رشته تحصیلی: {data['major']}"
        )

        try:
            bot.send_message(
                ADMIN_ID,
                admin_message
            )
        except Exception:
            bot.send_message(
                message.chat.id,
                "❌ ارسال ثبت‌نام با مشکل مواجه شد. "
                "لطفاً بعداً دوباره تلاش کنید.",
                reply_markup=main_menu()
            )
            registration_data.pop(user_id, None)
            selected_sessions.pop(user_id, None)
            return

        registration_data.pop(user_id, None)
        selected_sessions.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "✅ ثبت‌نام شما با موفقیت انجام شد!\n\n"
            "🎙️ از حضور شما در این نشست خوشحال می‌شویم.",
            reply_markup=main_menu()
        )

    # --------------------------------------
    # لغو ثبت‌نام
    # --------------------------------------

    def is_cancel(message):
        if message.text == "❌ انصراف":
            user_id = message.from_user.id

            registration_data.pop(user_id, None)
            selected_sessions.pop(user_id, None)

            bot.send_message(
                message.chat.id,
                "❌ ثبت‌نام لغو شد.",
                reply_markup=main_menu()
            )
            return True

        return False