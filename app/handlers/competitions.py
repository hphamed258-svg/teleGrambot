# from pathlib import Path
# from telebot import TeleBot
# # from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# from app.config import ADMIN_ID
# from app.keyboards.main_menu import main_menu
# from app.keyboards.competitions_menu import (
#     COMPETITION_TITLE,
#     competitions_menu,
#     competition_details_menu,
#     cancel_menu,
#     phone_menu,
#     major_menu
# )


# # ==========================================
# # تنظیمات مسابقه سی‌رنگ
# # ==========================================

# COMPETITION_TEXT = """
# 🎨 ثبت‌نام مسابقه نقاشی «سی‌رنگ»

# آماده‌ای خلاقیتت رو به چالش بکشی؟ 🖌️🔥

# در مسابقه‌ی سی‌رنگ قراره نقاشی رو با چالش‌های هیجان‌انگیز و غیرمنتظره ترکیب کنیم! اینجا فقط مهارت نقاشی مهم نیست؛ خلاقیت، تمرکز و توانایی تو برای کنار اومدن با چالش‌ها هم محک زده می‌شه!

# 📅 تاریخ برگزاری: دوشنبه، ۲۰ مهر
# ⏰ ساعت: ۱۱ تا ۱۳
# 📍 مکان: اتاق فکر (روبروی سلف پسران)

# 💰 هزینه شرکت: رایگان! 🎉

# 🏆 جوایز: جوایز ارزنده برای نفرات برتر

# 👥 نحوه داوری: آثار شرکت‌کنندگان توسط سایر شرکت‌کنندگان داوری می‌شن و نفرات برتر بر اساس نتیجه داوری مشخص خواهند شد.

# 📝 برای ثبت‌نام، کافیه بزنی روی دکمه ی ثبت نام در مسابقه و مراحل بعدی ربات رو دنبال کنی و اطلاعات درخواستی رو وارد کنی.

# پس آماده شو تا رنگ‌ها رو به چالش بکشی و خلاقیتت رو به نمایش بذاری! 🎨

# ✨ سی‌رنگ؛ جایی که خلاقیت، رنگ تازه‌ای می‌گیره!
# """

# # مسیر پوستر:
# # فایل عکس را داخل app/assets قرار بده
# # و نام آن را sirang_poster.jpg بگذار.
# POSTER_PATH = (
#     Path(__file__).resolve().parents[1]
#     / "assets"
#     / "sirang_poster.jpg"
# )

# MAJORS = [
#     "مهندسی کامپیوتر",
#     "حسابداری",
#     "روانشناسی",
#     "حقوق",
#     "مدیریت بازرگانی",
#     "ادبیات زبان انگلیسی",
# ]

# registration_data = {}


# # ==========================================
# # ثبت هندلرهای مسابقه
# # ==========================================

# def register_competitions_handler(bot: TeleBot):

#     # نمایش فهرست مسابقات
#     @bot.message_handler(
#         func=lambda message: message.text == "🏆 مسابقات"
#     )
#     def show_competitions(message):
#         bot.send_message(
#             message.chat.id,
#             "🏆 لطفاً مسابقه موردنظر خود را انتخاب کنید:",
#             reply_markup=competitions_menu()
#         )

#     # بازگشت از فهرست مسابقات به منوی اصلی
#     @bot.message_handler(
#         func=lambda message: (
#             message.text == "🔙 بازگشت به منوی اصلی"
#         )
#     )
#     def back_to_main(message):
#         bot.send_message(
#             message.chat.id,
#             "به منوی اصلی برگشتید.",
#             reply_markup=main_menu()
#         )

#     # نمایش جزئیات مسابقه سی‌رنگ
#     @bot.message_handler(
#         func=lambda message: message.text == COMPETITION_TITLE
#     )
#     def show_sirang(message):
#         if POSTER_PATH.is_file():
#             with open(POSTER_PATH, "rb") as poster:
#                 bot.send_photo(
#                     message.chat.id,
#                     poster,
#                     caption=COMPETITION_TEXT,
#                     reply_markup=competition_details_menu()
#                 )
#         else:
#             bot.send_message(
#                 message.chat.id,
#                 "⚠️ پوستر پیدا نشد؛ فعلاً متن مسابقه را می‌فرستیم.\n\n"
#                 + COMPETITION_TEXT,
#                 reply_markup=competition_details_menu()
#             )

#     # بازگشت از جزئیات به فهرست مسابقات
#     @bot.message_handler(
#         func=lambda message: (
#             message.text == "🔙 بازگشت به مسابقات"
#         )
#     )
#     def back_to_competitions(message):
#         bot.send_message(
#             message.chat.id,
#             "🏆 لطفاً مسابقه موردنظر خود را انتخاب کنید:",
#             reply_markup=competitions_menu()
#         )

#     # شروع فرم ثبت‌نام
#     @bot.message_handler(
#         func=lambda message: (
#             message.text == "📝 ثبت‌نام در مسابقه"
#         )
#     )
#     def start_registration(message):
#         user_id = message.from_user.id

#         registration_data[user_id] = {
#             "step": "name"
#         }

#         bot.send_message(
#             message.chat.id,
#             "🎨 ثبت‌نام مسابقه سی‌رنگ\n\n"
#             "👤 لطفاً نام و نام خانوادگی خود را وارد کنید:",
#             reply_markup=cancel_menu()
#         )

#         bot.register_next_step_handler(
#             message,
#             get_name
#         )

#     # دریافت نام و نام خانوادگی
#     def get_name(message):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if not message.text or not message.text.strip():
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً نام و نام خانوادگی خود را به‌صورت متنی وارد کنید."
#             )
#             bot.register_next_step_handler(message, get_name)
#             return

#         registration_data[user_id]["name"] = message.text.strip()

#         bot.send_message(
#             message.chat.id,
#             "📱 لطفاً شماره تلفن خود را با زدن دکمه زیر ارسال کنید.",
#             reply_markup=phone_menu()
#         )

#         bot.register_next_step_handler(
#             message,
#             get_phone
#         )

#     # دریافت شماره تلفن از طریق دکمه اشتراک‌گذاری مخاطب
#     def get_phone(message):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if not message.contact:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً از دکمه «📱 ارسال شماره تلفن» استفاده کنید.",
#                 reply_markup=phone_menu()
#             )
#             bot.register_next_step_handler(message, get_phone)
#             return

#         if (
#             message.contact.user_id is not None
#             and message.contact.user_id != user_id
#         ):
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً شماره تلفن خودتان را ارسال کنید.",
#                 reply_markup=phone_menu()
#             )
#             bot.register_next_step_handler(message, get_phone)
#             return

#         registration_data[user_id]["phone"] = (
#             message.contact.phone_number
#         )

#         bot.send_message(
#             message.chat.id,
#             "🎓 لطفاً رشته تحصیلی خود را انتخاب کنید:",
#             reply_markup=major_menu()
#         )

#         bot.register_next_step_handler(
#             message,
#             get_major
#         )

#     # دریافت رشته از بین گزینه‌های تعیین‌شده
#     def get_major(message):
#         user_id = message.from_user.id

#         if is_cancel(message):
#             return

#         if message.text not in MAJORS:
#             bot.send_message(
#                 message.chat.id,
#                 "لطفاً رشته خود را از بین گزینه‌های زیر انتخاب کنید.",
#                 reply_markup=major_menu()
#             )
#             bot.register_next_step_handler(message, get_major)
#             return

#         registration_data[user_id]["major"] = message.text

#         send_registration_to_admin(message)

#     # ارسال ثبت‌نام به ادمین
#     def send_registration_to_admin(message):
#         user_id = message.from_user.id
#         user = message.from_user
#         data = registration_data[user_id]

#         username = (
#             f"@{user.username}"
#             if user.username
#             else "ندارد"
#         )

#         admin_message = (
#             "🎨 ثبت‌نام جدید مسابقه سی‌رنگ\n\n"
#             f"👤 نام و نام خانوادگی: {data['name']}\n"
#             f"🔗 نام کاربری: {username}\n"
#             f"🆔 شناسه تلگرام: {user.id}\n"
#             f"📱 شماره تلفن: {data['phone']}\n"
#             f"🎓 رشته تحصیلی: {data['major']}"
#         )

#         try:
#             bot.send_message(
#                 ADMIN_ID,
#                 admin_message
#             )
#         except Exception:
#             bot.send_message(
#                 message.chat.id,
#                 "❌ ارسال ثبت‌نام با مشکل مواجه شد. "
#                 "لطفاً کمی بعد دوباره تلاش کنید.",
#                 reply_markup=main_menu()
#             )
#             registration_data.pop(user_id, None)
#             return

#         registration_data.pop(user_id, None)

#         bot.send_message(
#             message.chat.id,
#             "✅ ثبت‌نام شما در مسابقه سی‌رنگ با موفقیت انجام شد!\n\n"
#             "🎨 منتظر دیدنت در مسابقه هستیم. موفق باشی!",
#             reply_markup=main_menu()
#         )

#     # لغو ثبت‌نام
#     def is_cancel(message):
#         if message.text == "❌ انصراف":
#             registration_data.pop(
#                 message.from_user.id,
#                 None
#             )

#             bot.send_message(
#                 message.chat.id,
#                 "❌ ثبت‌نام لغو شد.",
#                 reply_markup=main_menu()
#             )
#             return True

#         return False



# # from telebot import TeleBot


# # def register_competitions_handler(bot: TeleBot):

# #     @bot.message_handler(
# #         func=lambda message: message.text == "🏆 مسابقات"
# #     )
# #     def competitions(message):

# #         bot.send_message(
# #             message.chat.id,
# #             "فعلاً مسابقه ای در حال برگزاری نیست."
# #         )

from pathlib import Path
import logging

from telebot import TeleBot

from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.competitions_menu import (
    COMPETITION_TITLE,
    MINI_ARC_TITLE,
    competitions_menu,
    competition_details_menu,
    cancel_menu,
    phone_menu,
    entry_year_menu,
    retry_menu,
)


logger = logging.getLogger(__name__)


# ==========================================
# تنظیمات مسابقه سی‌رنگ
# ==========================================

SIRANG_CLOSED_TEXT = (
    "مسابقه سی‌رنگ قبلاً برگزار شده است و مهلت ثبت‌نام آن "
    "به پایان رسیده است.\n\n"
    "برای مشاهده مسابقات دیگر، به فهرست مسابقات برگردید."
)


# ==========================================
# تنظیمات مسابقه مینی آرک
# ==========================================

PROJECT_ROOT = Path(__file__).resolve().parents[1]

MINI_ARC_POSTER_PATH = (
    PROJECT_ROOT / "assets" / "mini_arc_poster.jpg"
)

MINI_ARC_TEXT = """
🏁 مینی آرک | MINI ARC
💻 مسابقه برنامه‌نویسی الگوریتمی

اگه دوست داری مهارت‌های الگوریتمی خودت رو محک بزنی و یه رقابت برنامه‌نویسی رو تجربه کنی، مینی آرک فرصتی برای توئه!

🚀 مینی آرک، رقابت مقدماتی مسابقه اصلی ARC هست؛ فرصتی برای تمرین، سنجش توانایی‌ها و آماده‌شدن برای رقابت اصلی.

📌 اطلاعات مسابقه
📅 دوشنبه ۱۱ آبان
⏰ ساعت ۱۲
📍 سالن مطالعه

👥 نحوه برگزاری: تیم‌های دونفره
🎓 مخاطبان: تمام ورودی‌های مهندسی کامپیوتر
💰 هزینه شرکت: رایگان

🔥 آماده‌ای توانایی‌هات رو به چالش بکشی؟

برای شرکت در مینی آرک، ثبت‌نامت رو انجام بده!
"""

ENTRY_YEARS = {
    "ورودی 401",
    "ورودی 402",
    "ورودی 403",
    "ورودی 404",
}

# اطلاعات موقت ثبت‌نام هر کاربر
registration_data = {}


# ==========================================
# ثبت هندلرهای مسابقات
# ==========================================

def register_competitions_handler(bot: TeleBot):

    # --------------------------------------
    # نمایش فهرست مسابقات
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == "🏆 مسابقات"
    )
    def show_competitions(message):
        registration_data.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            "لطفاً مسابقه موردنظر خود را انتخاب کنید:",
            reply_markup=competitions_menu()
        )

    # --------------------------------------
    # سی‌رنگ: ثبت‌نام بسته
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == COMPETITION_TITLE
    )
    def show_sirang(message):
        registration_data.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            SIRANG_CLOSED_TEXT,
            reply_markup=competitions_menu()
        )

    # --------------------------------------
    # نمایش مینی آرک
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == MINI_ARC_TITLE
    )
    def show_mini_arc(message):
        registration_data.pop(message.from_user.id, None)

        if MINI_ARC_POSTER_PATH.is_file():
            with open(MINI_ARC_POSTER_PATH, "rb") as poster:
                bot.send_photo(
                    message.chat.id,
                    poster,
                    caption=MINI_ARC_TEXT,
                    reply_markup=competition_details_menu()
                )
        else:
            bot.send_message(
                message.chat.id,
                "پوستر مینی آرک پیدا نشد.\n\n" + MINI_ARC_TEXT,
                reply_markup=competition_details_menu()
            )

    # --------------------------------------
    # بازگشت به فهرست مسابقات
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == "🔙 بازگشت به مسابقات"
    )
    def back_to_competitions(message):
        registration_data.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            "لطفاً مسابقه موردنظر خود را انتخاب کنید:",
            reply_markup=competitions_menu()
        )

    # --------------------------------------
    # بازگشت به منوی اصلی
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text in {
            "🔙 بازگشت به منوی اصلی",
            "🏠 منوی اصلی",
        }
    )
    def back_to_main(message):
        registration_data.pop(message.from_user.id, None)

        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتید.",
            reply_markup=main_menu()
        )

    # --------------------------------------
    # شروع ثبت‌نام
    # --------------------------------------

    @bot.message_handler(
        func=lambda message: message.text == "📝 ثبت‌نام در مسابقه"
    )
    def start_registration(message):
        user_id = message.from_user.id

        registration_data[user_id] = {
            "step": "name",
            "data": {}
        }

        bot.send_message(
            message.chat.id,
            "ثبت‌نام مسابقه مینی آرک\n\n"
            "لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(message, get_name)

    # ======================================
    # مدیریت انصراف و بازگشت
    # ======================================

    def handle_navigation(message):
        text = message.text
        user_id = message.from_user.id

        navigation_options = {
            "❌ انصراف",
            "🔙 بازگشت به مسابقات",
            "🏆 مسابقات",
        }

        if text not in navigation_options:
            return False

        registration_data.pop(user_id, None)

        if text == "❌ انصراف":
            bot.send_message(
                message.chat.id,
                "ثبت‌نام شما لغو شد.",
                reply_markup=competitions_menu()
            )
        else:
            bot.send_message(
                message.chat.id,
                "لطفاً مسابقه موردنظر خود را انتخاب کنید:",
                reply_markup=competitions_menu()
            )

        return True

    # ======================================
    # مرحله اول: نام و نام خانوادگی
    # ======================================

    def get_name(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id
        state = registration_data.get(user_id)

        if not state:
            return

        if (
            message.content_type != "text"
            or not message.text.strip()
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً نام و نام خانوادگی خود را به‌صورت متنی وارد کنید.",
                reply_markup=cancel_menu()
            )
            bot.register_next_step_handler(message, get_name)
            return

        state["data"]["name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "لطفاً نام تیم خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(message, get_team_name)

    # ======================================
    # مرحله دوم: نام تیم
    # ======================================

    def get_team_name(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id
        state = registration_data.get(user_id)

        if not state:
            return

        if (
            message.content_type != "text"
            or not message.text.strip()
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً نام تیم را به‌صورت متنی وارد کنید.",
                reply_markup=cancel_menu()
            )
            bot.register_next_step_handler(message, get_team_name)
            return

        state["data"]["team_name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "لطفاً شماره دانشجویی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(message, get_student_id)

    # ======================================
    # مرحله سوم: شماره دانشجویی
    # ======================================

    def get_student_id(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id

        if user_id not in registration_data:
            return

        student_id = message.text.strip() if message.text else ""

        # تبدیل ارقام فارسی و عربی به انگلیسی
        digit_map = str.maketrans(
            "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
            "01234567890123456789"
        )
        student_id = student_id.translate(digit_map)

        # بررسی تعداد رقم‌ها و عدد بودن
        if not student_id.isdigit() or len(student_id) != 8:
            bot.send_message(
                message.chat.id,
                "شماره دانشجویی باید دقیقاً ۸ رقم باشد.\nلطفاً دوباره وارد کنید:",
                reply_markup=cancel_menu()
            )
            bot.register_next_step_handler(message, get_student_id)
            return

        # جلوگیری از شماره‌هایی مثل 00000000 یا 11111111
        if len(set(student_id)) == 1:
            bot.send_message(
                message.chat.id,
                "این شماره دانشجویی معتبر نیست؛ تمام رقم‌ها نمی‌توانند یکسان باشند.\nلطفاً شماره صحیح را وارد کنید:",
                reply_markup=cancel_menu()
            )
            bot.register_next_step_handler(message, get_student_id)
            return

        registration_data[user_id]["data"]["student_id"] = student_id

        registration_data[user_id]["step"] = "phone"

        bot.send_message(
            message.chat.id,
            "لطفاً شماره تماس خود را ارسال کنید. می‌توانید از دکمه زیر استفاده کنید یا شماره را دستی وارد کنید.",
            reply_markup=phone_menu()
        )
        bot.register_next_step_handler(message, get_phone)

    # ======================================
    # مرحله چهارم: شماره تماس
    # ======================================

    def get_phone(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id
        state = registration_data.get(user_id)

        if not state:
            return

        if message.content_type == "contact":
            contact = message.contact

            if (
                contact.user_id is not None
                and contact.user_id != user_id
            ):
                bot.send_message(
                    message.chat.id,
                    "لطفاً شماره تماس متعلق به خودتان را ارسال کنید.",
                    reply_markup=phone_menu()
                )
                bot.register_next_step_handler(message, get_phone)
                return

            phone = contact.phone_number

        elif message.content_type == "text":
            phone = message.text.strip()
            normalized_phone = (
                phone.replace(" ", "")
                .replace("-", "")
                .replace("(", "")
                .replace(")", "")
            )

            if not normalized_phone.lstrip("+").isdigit():
                bot.send_message(
                    message.chat.id,
                    "شماره تماس معتبر نیست. لطفاً دوباره وارد کنید.",
                    reply_markup=phone_menu()
                )
                bot.register_next_step_handler(message, get_phone)
                return

            phone = normalized_phone

        else:
            bot.send_message(
                message.chat.id,
                "لطفاً شماره تماس خود را ارسال کنید.",
                reply_markup=phone_menu()
            )
            bot.register_next_step_handler(message, get_phone)
            return

        state["data"]["phone"] = phone

        bot.send_message(
            message.chat.id,
            "لطفاً سال ورودی خود را انتخاب کنید:",
            reply_markup=entry_year_menu()
        )

        bot.register_next_step_handler(message, get_entry_year)

    # ======================================
    # مرحله پنجم: سال ورودی
    # ======================================

    def get_entry_year(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id
        state = registration_data.get(user_id)

        if not state:
            return

        if (
            message.content_type != "text"
            or message.text not in ENTRY_YEARS
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً سال ورودی خود را از بین گزینه‌های زیر انتخاب کنید:",
                reply_markup=entry_year_menu()
            )
            bot.register_next_step_handler(message, get_entry_year)
            return

        state["data"]["entry_year"] = message.text

        send_registration_to_admin(message)

    # ======================================
    # ارسال اطلاعات به مدیر
    # ======================================

    def send_registration_to_admin(message):
        user_id = message.from_user.id
        user = message.from_user
        state = registration_data.get(user_id)

        if not state:
            return

        data = state["data"]

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        admin_message = (
            "ثبت‌نام جدید مسابقه مینی آرک\n\n"
            f"نام و نام خانوادگی: {data['name']}\n"
            f"نام تیم: {data['team_name']}\n"
            f"شماره دانشجویی: {data['student_id']}\n"
            f"شماره تماس: {data['phone']}\n"
            f"سال ورودی: {data['entry_year']}\n"
            f"نام کاربری تلگرام: {username}\n"
            f"شناسه تلگرام: {user.id}"
        )

        try:
            bot.send_message(ADMIN_ID, admin_message)

        except Exception:
            logger.exception(
                "Failed to send Mini ARC registration to admin."
            )

            bot.send_message(
                message.chat.id,
                "ارسال اطلاعات با مشکل مواجه شد. اطلاعات شما حفظ شده است؛ لطفاً دوباره تلاش کنید.",
                reply_markup=retry_menu()
            )

            bot.register_next_step_handler(
                message,
                retry_registration
            )
            return

        registration_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "ثبت‌نام شما در مسابقه مینی آرک با موفقیت انجام شد.\n\n"
            "از ثبت‌نام شما سپاسگزاریم.",
            reply_markup=main_menu()
        )

    # ======================================
    # تلاش مجدد برای ارسال
    # ======================================

    def retry_registration(message):
        if handle_navigation(message):
            return

        user_id = message.from_user.id
        state = registration_data.get(user_id)

        if not state:
            return

        if message.text == "🔄 تلاش مجدد برای ثبت‌نام":
            send_registration_to_admin(message)
            return

        bot.send_message(
            message.chat.id,
            "لطفاً تلاش مجدد را انتخاب کنید یا ثبت‌نام را لغو کنید.",
            reply_markup=retry_menu()
        )

        bot.register_next_step_handler(
            message,
            retry_registration
        )
