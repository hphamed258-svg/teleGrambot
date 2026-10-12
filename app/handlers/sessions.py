# from pathlib import Path

# from telebot import TeleBot

# from app.config import ADMIN_ID
# from app.keyboards.main_menu import main_menu
# from app.keyboards.sessions_menu import (
#     sessions_menu,
#     session_details_menu,
#     session_cancel_menu,
#     session_phone_menu,
#     session_degree_menu,
#     session_entry_year_menu,
#     session_university_menu,
# )


# SESSIONS = {
#     "first_session": {
#         "title": """💻 سیری در جهان کامپیوتر | فصل دوم، جلسه اول""",
#         "text": """🟢 چقدر با مسیر واقعی ورود به دنیای هوش مصنوعی آشنایی داری؟ تا حالا دوست داشتی از تجربه‌های یک متخصص بشنوی و سؤال‌هایی رو بپرسی که شاید جوابشون رو توی کلاس‌های درس پیدا نکنی؟

# 🔵 در اولین جلسه از فصل دوم مجموعه‌نشست‌های «سیری در جهان کامپیوتر»، میزبان آقای پوریا اعظمی، متخصص حوزه هوش مصنوعی و پردازش تصویر هستیم تا در فضایی صمیمی و تعاملی، درباره تجربه‌ها، مسیر تخصصی و دنیای این فناوری‌ها گفت‌وگو کنیم.

# 🟢 این نشست قراره یک گفت‌وگوی دوطرفه باشه؛ نه صرفاً یک سخنرانی! شما هم در شکل‌گیری بحث نقش دارید و می‌تونید سؤال‌هاتون رو مطرح کنید، از تجربه‌های مهمان نشست بشنوید و از دل پرسش‌وپاسخ‌ها، دید تازه‌ای نسبت به مسیر یادگیری و فعالیت در این حوزه به دست بیارید.

# 📅 تاریخ برگزاری: پنجشنبه، ۲۳ مهر
# ⏰ ساعت: ۱۰ تا ۱۱:۳۰
# 📍 مکان: دانشگاه یزد، دانشکده منابع طبیعی، سالن منتظر قائم
# 💰 هزینه شرکت: رایگان

# 📝 برای تکمیل ثبت‌نام، مراحل بعدی ربات رو دنبال کن و اطلاعات درخواستی رو وارد کن.

# سیری در جهان کامپیوتر؛ جایی برای شنیدن تجربه‌ها، پرسیدن سؤال‌ها و پیدا کردن مسیرهای تازه🌱

# پردیس مهریز دانشگاه یزد با همکاری انجمن های علمی مهندسی کامپیوتر دانشگاه‌های علم‌و‌هنر و میبد
# """,
#         "poster": "first_session.jpg",
#     },
# }

# ASSETS_PATH = Path(__file__).resolve().parents[1] / "assets"

# DEGREES = [
#     "کاردانی",
#     "کارشناسی",
#     "کارشناسی ارشد",
#     "دکترا",
# ]

# ENTRY_YEARS = [
#     "ورودی 401 یا پایین‌تر",
#     "ورودی 402",
#     "ورودی 403",
#     "ورودی 404",
# ]

# UNIVERSITIES = [
#     "دانشگاه یزد",
#     "دانشگاه میبد",
#     "دانشگاه علم و هنر",
#     "سایر",
# ]

# selected_sessions = {}
# registration_data = {}


# def register_sessions_handler(bot: TeleBot):

#     # نمایش نشست‌های علمی
#     @bot.message_handler(
#         func=lambda message: message.text == "🎙️ نشست‌های علمی"
#     )
#     def show_sessions(message):
#         bot.send_message(
#             message.chat.id,
#             "🎙️ لطفاً نشست موردنظر خود را انتخاب کنید:",
#             reply_markup=sessions_menu(list(SESSIONS.values())),
#         )

#     # بازگشت به منوی اصلی
#     @bot.message_handler(
#         func=lambda message: message.text == "🔙 بازگشت به منوی اصلی"
#     )
#     def back_to_main(message):
#         user_id = message.from_user.id
#         selected_sessions.pop(user_id, None)
#         registration_data.pop(user_id, None)

#         bot.send_message(
#             message.chat.id,
#             "به منوی اصلی برگشتید.",
#             reply_markup=main_menu(),
#         )

#     # نمایش جزئیات نشست
#     @bot.message_handler(
#         func=lambda message: message.text in [
#             session["title"] for session in SESSIONS.values()
#         ]
#     )
#     def show_session_details(message):
#         user_id = message.from_user.id

#         session_id = next(
#             key
#             for key, session in SESSIONS.items()
#             if session["title"] == message.text
#         )

#         selected_sessions[user_id] = session_id
#         session = SESSIONS[session_id]
#         poster_path = ASSETS_PATH / session["poster"]

#         if poster_path.is_file():
#             with open(poster_path, "rb") as poster:
#                 bot.send_photo(
#                     message.chat.id,
#                     poster,
#                     caption=session["text"],
#                     reply_markup=session_details_menu(),
#                 )
#         else:
#             bot.send_message(
#                 message.chat.id,
#                 session["text"],
#                 reply_markup=session_details_menu(),
#             )

#     # بازگشت به فهرست نشست‌ها
#     @bot.message_handler(
#         func=lambda message: message.text == "🔙 بازگشت به نشست‌های علمی"
#     )
#     def back_to_sessions(message):
#         user_id = message.from_user.id
#         selected_sessions.pop(user_id, None)
#         registration_data.pop(user_id, None)

#         bot.send_message(
#             message.chat.id,
#             "🎙️ لطفاً نشست موردنظر خود را انتخاب کنید:",
#             reply_markup=sessions_menu(list(SESSIONS.values())),
#         )

#     # شروع ثبت‌نام
#     @bot.message_handler(
#         func=lambda message: message.text == "📝 ثبت‌نام"
#     )
#     def start_registration(message):
#         user_id = message.from_user.id
#         session_id = selected_sessions.get(user_id)

#         if session_id not in SESSIONS:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً ابتدا یک نشست را انتخاب کنید.",
#                 reply_markup=main_menu(),
#             )
#             return

#         registration_data[user_id] = {
#             "session_id": session_id,
#         }

#         bot.send_message(
#             message.chat.id,
#             "لطفاً نام و نام خانوادگی خود را وارد کنید:",
#             reply_markup=session_cancel_menu(),
#         )

#         bot.register_next_step_handler(message, get_name, session_id)

#     # دریافت نام و نام خانوادگی
#     def get_name(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if not message.text or not message.text.strip():
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً نام و نام خانوادگی خود را وارد کنید.",
#                 reply_markup=session_cancel_menu(),
#             )
#             bot.register_next_step_handler(message, get_name, session_id)
#             return

#         registration_data[user_id]["name"] = message.text.strip()

#         bot.send_message(
#             message.chat.id,
#             "لطفاً شماره تلفن خود را با دکمه زیر ارسال کنید:",
#             reply_markup=session_phone_menu(),
#         )

#         bot.register_next_step_handler(message, get_phone, session_id)

#     # دریافت شماره تلفن
#     def get_phone(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if not message.contact:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً از دکمه «📱 ارسال شماره تلفن» استفاده کنید.",
#                 reply_markup=session_phone_menu(),
#             )
#             bot.register_next_step_handler(message, get_phone, session_id)
#             return

#         if (
#             message.contact.user_id is not None
#             and message.contact.user_id != user_id
#         ):
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً شماره تلفن خودتان را ارسال کنید.",
#                 reply_markup=session_phone_menu(),
#             )
#             bot.register_next_step_handler(message, get_phone, session_id)
#             return

#         registration_data[user_id]["phone"] = (
#             message.contact.phone_number
#         )

#         bot.send_message(
#             message.chat.id,
#             "لطفاً مقطع تحصیلی خود را انتخاب کنید:",
#             reply_markup=session_degree_menu(),
#         )

#         bot.register_next_step_handler(message, get_degree, session_id)

#     # دریافت مقطع تحصیلی
#     def get_degree(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if message.text not in DEGREES:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً مقطع تحصیلی خود را از گزینه‌ها انتخاب کنید.",
#                 reply_markup=session_degree_menu(),
#             )
#             bot.register_next_step_handler(message, get_degree, session_id)
#             return

#         registration_data[user_id]["degree"] = message.text

#         bot.send_message(
#             message.chat.id,
#             "لطفاً سال ورودی خود را انتخاب کنید:",
#             reply_markup=session_entry_year_menu(),
#         )

#         bot.register_next_step_handler(
#             message,
#             get_entry_year,
#             session_id,
#         )

#     # دریافت سال ورودی
#     def get_entry_year(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if message.text not in ENTRY_YEARS:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً سال ورودی خود را از گزینه‌ها انتخاب کنید.",
#                 reply_markup=session_entry_year_menu(),
#             )
#             bot.register_next_step_handler(
#                 message,
#                 get_entry_year,
#                 session_id,
#             )
#             return

#         registration_data[user_id]["entry_year"] = message.text

#         bot.send_message(
#             message.chat.id,
#             "دانشگاه خود را انتخاب کنید:",
#             reply_markup=session_university_menu(),
#         )

#         bot.register_next_step_handler(
#             message,
#             get_university,
#             session_id,
#         )

#     # دریافت دانشگاه
#     def get_university(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if message.text not in UNIVERSITIES:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً دانشگاه خود را از گزینه‌ها انتخاب کنید.",
#                 reply_markup=session_university_menu(),
#             )
#             bot.register_next_step_handler(
#                 message,
#                 get_university,
#                 session_id,
#             )
#             return

#         if message.text == "سایر":
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً نام دانشگاه خود را وارد کنید:",
#                 reply_markup=session_cancel_menu(),
#             )
#             bot.register_next_step_handler(
#                 message,
#                 get_other_university,
#                 session_id,
#             )
#             return

#         registration_data[user_id]["university"] = message.text
#         send_registration_to_admin(message, session_id)

#     # دریافت نام دانشگاه در صورت انتخاب «سایر»
#     def get_other_university(message, session_id):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if not message.text or not message.text.strip():
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً نام دانشگاه خود را وارد کنید.",
#                 reply_markup=session_cancel_menu(),
#             )
#             bot.register_next_step_handler(
#                 message,
#                 get_other_university,
#                 session_id,
#             )
#             return

#         registration_data[user_id]["university"] = message.text.strip()
#         send_registration_to_admin(message, session_id)

#     # ارسال اطلاعات ثبت‌نام برای ادمین
#     def send_registration_to_admin(message, session_id):
#         user_id = message.from_user.id
#         user = message.from_user
#         data = registration_data[user_id]
#         session = SESSIONS[session_id]

#         username = f"@{user.username}" if user.username else "ندارد"

#         admin_message = (
#             "🎙️ ثبت‌نام جدید در نشست علمی\n\n"
#             f"📌 عنوان نشست: {session['title']}\n"
#             f"👤 نام و نام خانوادگی: {data['name']}\n"
#             f"🔗 نام کاربری: {username}\n"
#             f"🆔 شناسه تلگرام: {user.id}\n"
#             f"📱 شماره تلفن: {data['phone']}\n"
#             f"🎓 مقطع تحصیلی: {data['degree']}\n"
#             f"📚 سال ورودی: {data['entry_year']}\n"
#             f"🏛 دانشگاه: {data['university']}"
#         )

#         try:
#             if not ADMIN_ID:
#                 raise ValueError("ADMIN_ID تنظیم نشده است.")

#             bot.send_message(ADMIN_ID, admin_message)

#         except Exception:
#             bot.send_message(
#                 message.chat.id,
#                 "❌ ثبت‌نام انجام نشد. لطفاً بعداً دوباره تلاش کنید.",
#                 reply_markup=main_menu(),
#             )
#             registration_data.pop(user_id, None)
#             selected_sessions.pop(user_id, None)
#             return

#         registration_data.pop(user_id, None)
#         selected_sessions.pop(user_id, None)

#         bot.send_message(
#             message.chat.id,
#             "✅ ثبت‌نام شما با موفقیت انجام شد.",
#             reply_markup=main_menu(),
#         )

#     # لغو ثبت‌نام
#     def is_cancel(message):
#         if message.text == "❌ انصراف":
#             user_id = message.from_user.id

#             registration_data.pop(user_id, None)
#             selected_sessions.pop(user_id, None)

#             bot.send_message(
#                 message.chat.id,
#                 "ثبت‌نام لغو شد.",
#                 reply_markup=main_menu(),
#             )
#             return True

#         return False



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


# اطلاعات نشست‌ها
# برای اضافه‌کردن نشست جدید، یک مورد مشابه به این دیکشنری اضافه کن.
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

MAJORS = [
    "مهندسی کامپیوتر",
    "حسابداری",
    "روانشناسی",
    "حقوق",
    "مدیریت بازرگانی",
    "زبان و ادبیات انگلیسی",
]

# اطلاعات موقت کاربران
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
            "🎙️ نشست‌های علمی",
            reply_markup=sessions_menu(list(SESSIONS.values())),
        )

    # بازگشت به منوی اصلی
    @bot.message_handler(
        func=lambda message: message.text == "🔙 بازگشت به منوی اصلی"
    )
    def back_to_main(message):
        selected_sessions.pop(message.from_user.id, None)
        registration_data.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتید.",
            reply_markup=main_menu(),
        )

    # نمایش اطلاعات نشست انتخاب‌شده
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
            "🎙️ نشست‌های علمی",
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

        bot.register_next_step_handler(
            message,
            get_name,
            session_id,
        )

    # دریافت نام و نام خانوادگی
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
            bot.register_next_step_handler(
                message,
                get_name,
                session_id,
            )
            return

        registration_data[user_id]["name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "لطفاً شماره تلفن خود را با دکمه زیر ارسال کنید:",
            reply_markup=session_phone_menu(),
        )

        bot.register_next_step_handler(
            message,
            get_phone,
            session_id,
        )

    # دریافت شماره تلفن با دکمه اشتراک‌گذاری مخاطب
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
            bot.register_next_step_handler(
                message,
                get_phone,
                session_id,
            )
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
            bot.register_next_step_handler(
                message,
                get_phone,
                session_id,
            )
            return

        registration_data[user_id]["phone"] = (
            message.contact.phone_number
        )

        bot.send_message(
            message.chat.id,
            "رشته تحصیلی خود را انتخاب کنید:",
            reply_markup=session_major_menu(),
        )

        bot.register_next_step_handler(
            message,
            get_major,
            session_id,
        )

    # دریافت رشته تحصیلی
    def get_major(message, session_id):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if message.text not in MAJORS:
            bot.send_message(
                message.chat.id,
                "لطفاً رشته تحصیلی خود را از گزینه‌ها انتخاب کنید.",
                reply_markup=session_major_menu(),
            )
            bot.register_next_step_handler(
                message,
                get_major,
                session_id,
            )
            return

        registration_data[user_id]["major"] = message.text

        send_registration_to_admin(message, session_id)

    # ارسال اطلاعات ثبت‌نام به ادمین
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
            f"📌 نشست: {session['title']}\n"
            f"👤 نام و نام خانوادگی: {data['name']}\n"
            f"🔗 نام کاربری: {username}\n"
            f"🆔 شناسه تلگرام: {user.id}\n"
            f"📱 شماره تلفن: {data['phone']}\n"
            f"🎓 رشته تحصیلی: {data['major']}"
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
