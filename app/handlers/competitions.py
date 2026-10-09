from pathlib import Path
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.competitions_menu import (
    competitions_menu,
    competition_details_menu,
    cancel_menu,
    phone_menu,
    major_menu
)


# ==========================================
# تنظیمات مسابقه سی‌رنگ
# ==========================================

COMPETITION_TITLE = "🎨 سی‌رنگ"

COMPETITION_TEXT = """
🎨🖌️ سی‌رنگ؛ جایی که نقاشی کشیدن، دیگه کار آسونی نیست!

فکر می‌کنی می‌تونی هر چیزی رو نقاشی کنی؟ 🤔

حالا تصور کن آهنگ توی گوشت پخش می‌شه، تمرکزت به‌هم ریخته و باید همون چیزی رو بکشی که ازت خواستن! 😂

توی مسابقه‌ی سی‌رنگ قراره با چالش‌های عجیب‌وغریب، خلاقیت و کلی لحظه‌ی بامزه روبه‌رو بشیم.

اینجا مهم نیست چقدر نقاشی بلدی؛ مهم اینه که بتونی از پس چالش‌ها بربیای! 🎨🔥

📅 دوشنبه، ۲۰ مهر
⏰ ساعت ۱۲ تا ۱۳
📍 اتاق فکر (سلف پسران)

🖍️ آماده‌ای ببینیم آخرش چی از آب درمیاد؟

انجمن علمی مهندسی کامپیوتر پردیس مهریز
"""

# مسیر پوستر:
# فایل عکس را داخل app/assets قرار بده
# و نام آن را sirang_poster.jpg بگذار.
POSTER_PATH = (
    Path(__file__).resolve().parents[1]
    / "assets"
    / "sirang_poster.jpg"
)

MAJORS = [
    "مهندسی کامپیوتر",
    "حسابداری",
    "روانشناسی",
    "حقوق",
    "مدیریت بازرگانی",
    "ادبیات زبان انگلیسی",
]

# اطلاعات موقت ثبت‌نام کاربران؛ بدون دیتابیس
registration_data = {}


# # ==========================================
# # کیبوردها
# # ==========================================

# def competitions_menu():
#     keyboard = ReplyKeyboardMarkup(
#         resize_keyboard=True
#     )
#     keyboard.row(KeyboardButton(COMPETITION_TITLE))
#     keyboard.row(
#         KeyboardButton("🔙 بازگشت به منوی اصلی")
#     )
#     return keyboard


# def competition_details_menu():
#     keyboard = ReplyKeyboardMarkup(
#         resize_keyboard=True
#     )
#     keyboard.row(
#         KeyboardButton("📝 ثبت‌نام در مسابقه")
#     )
#     keyboard.row(
#         KeyboardButton("🔙 بازگشت به مسابقات")
#     )
#     return keyboard


# def cancel_menu():
#     keyboard = ReplyKeyboardMarkup(
#         resize_keyboard=True
#     )
#     keyboard.row(KeyboardButton("❌ انصراف"))
#     return keyboard


# def phone_menu():
#     keyboard = ReplyKeyboardMarkup(
#         resize_keyboard=True
#     )
#     keyboard.row(
#         KeyboardButton(
#             "📱 ارسال شماره تلفن",
#             request_contact=True
#         )
#     )
#     keyboard.row(KeyboardButton("❌ انصراف"))
#     return keyboard


# def major_menu():
#     keyboard = ReplyKeyboardMarkup(
#         resize_keyboard=True
#     )

#     keyboard.row(
#         KeyboardButton("مهندسی کامپیوتر"),
#         KeyboardButton("حسابداری")
#     )
#     keyboard.row(
#         KeyboardButton("روانشناسی"),
#         KeyboardButton("حقوق")
#     )
#     keyboard.row(
#         KeyboardButton("مدیریت بازرگانی"),
#         KeyboardButton("ادبیات زبان انگلیسی")
#     )
#     keyboard.row(KeyboardButton("❌ انصراف"))

#     return keyboard


# ==========================================
# ثبت هندلرهای مسابقه
# ==========================================

def register_competitions_handler(bot: TeleBot):

    # نمایش فهرست مسابقات
    @bot.message_handler(
        func=lambda message: message.text == "🏆 مسابقات"
    )
    def show_competitions(message):
        bot.send_message(
            message.chat.id,
            "🏆 لطفاً مسابقه موردنظر خود را انتخاب کنید:",
            reply_markup=competitions_menu()
        )

    # بازگشت از فهرست مسابقات به منوی اصلی
    @bot.message_handler(
        func=lambda message: (
            message.text == "🔙 بازگشت به منوی اصلی"
        )
    )
    def back_to_main(message):
        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتید.",
            reply_markup=main_menu()
        )

    # نمایش جزئیات مسابقه سی‌رنگ
    @bot.message_handler(
        func=lambda message: message.text == COMPETITION_TITLE
    )
    def show_sirang(message):
        if POSTER_PATH.is_file():
            with open(POSTER_PATH, "rb") as poster:
                bot.send_photo(
                    message.chat.id,
                    poster,
                    caption=COMPETITION_TEXT,
                    reply_markup=competition_details_menu()
                )
        else:
            bot.send_message(
                message.chat.id,
                "⚠️ پوستر پیدا نشد؛ فعلاً متن مسابقه را می‌فرستیم.\n\n"
                + COMPETITION_TEXT,
                reply_markup=competition_details_menu()
            )

    # بازگشت از جزئیات به فهرست مسابقات
    @bot.message_handler(
        func=lambda message: (
            message.text == "🔙 بازگشت به مسابقات"
        )
    )
    def back_to_competitions(message):
        bot.send_message(
            message.chat.id,
            "🏆 لطفاً مسابقه موردنظر خود را انتخاب کنید:",
            reply_markup=competitions_menu()
        )

    # شروع فرم ثبت‌نام
    @bot.message_handler(
        func=lambda message: (
            message.text == "📝 ثبت‌نام در مسابقه"
        )
    )
    def start_registration(message):
        user_id = message.from_user.id

        registration_data[user_id] = {
            "step": "name"
        }

        bot.send_message(
            message.chat.id,
            "🎨 ثبت‌نام مسابقه سی‌رنگ\n\n"
            "👤 لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_name
        )

    # دریافت نام و نام خانوادگی
    def get_name(message):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.text or not message.text.strip():
            bot.send_message(
                message.chat.id,
                "لطفاً نام و نام خانوادگی خود را به‌صورت متنی وارد کنید."
            )
            bot.register_next_step_handler(message, get_name)
            return

        registration_data[user_id]["name"] = message.text.strip()

        bot.send_message(
            message.chat.id,
            "📱 لطفاً شماره تلفن خود را با زدن دکمه زیر ارسال کنید.",
            reply_markup=phone_menu()
        )

        bot.register_next_step_handler(
            message,
            get_phone
        )

    # دریافت شماره تلفن از طریق دکمه اشتراک‌گذاری مخاطب
    def get_phone(message):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.contact:
            bot.send_message(
                message.chat.id,
                "لطفاً از دکمه «📱 ارسال شماره تلفن» استفاده کنید.",
                reply_markup=phone_menu()
            )
            bot.register_next_step_handler(message, get_phone)
            return

        if (
            message.contact.user_id is not None
            and message.contact.user_id != user_id
        ):
            bot.send_message(
                message.chat.id,
                "لطفاً شماره تلفن خودتان را ارسال کنید.",
                reply_markup=phone_menu()
            )
            bot.register_next_step_handler(message, get_phone)
            return

        registration_data[user_id]["phone"] = (
            message.contact.phone_number
        )

        bot.send_message(
            message.chat.id,
            "🎓 لطفاً رشته تحصیلی خود را انتخاب کنید:",
            reply_markup=major_menu()
        )

        bot.register_next_step_handler(
            message,
            get_major
        )

    # دریافت رشته از بین گزینه‌های تعیین‌شده
    def get_major(message):
        user_id = message.from_user.id

        if is_cancel(message):
            return

        if message.text not in MAJORS:
            bot.send_message(
                message.chat.id,
                "لطفاً رشته خود را از بین گزینه‌های زیر انتخاب کنید.",
                reply_markup=major_menu()
            )
            bot.register_next_step_handler(message, get_major)
            return

        registration_data[user_id]["major"] = message.text

        send_registration_to_admin(message)

    # ارسال ثبت‌نام به ادمین
    def send_registration_to_admin(message):
        user_id = message.from_user.id
        user = message.from_user
        data = registration_data[user_id]

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        admin_message = (
            "🎨 ثبت‌نام جدید مسابقه سی‌رنگ\n\n"
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
                "لطفاً کمی بعد دوباره تلاش کنید.",
                reply_markup=main_menu()
            )
            registration_data.pop(user_id, None)
            return

        registration_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "✅ ثبت‌نام شما در مسابقه سی‌رنگ با موفقیت انجام شد!\n\n"
            "🎨 منتظر دیدنت در مسابقه هستیم. موفق باشی!",
            reply_markup=main_menu()
        )

    # لغو ثبت‌نام
    def is_cancel(message):
        if message.text == "❌ انصراف":
            registration_data.pop(
                message.from_user.id,
                None
            )

            bot.send_message(
                message.chat.id,
                "❌ ثبت‌نام لغو شد.",
                reply_markup=main_menu()
            )
            return True

        return False