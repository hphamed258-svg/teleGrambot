import os
from pathlib import Path
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from app.keyboards.main_menu import main_menu
from app.keyboards.festival_menu import (
    festival_menu,
    festival_detail_menu,
    degree_menu,
)


# مسیر پوستر جشنواره
PROJECT_ROOT = Path(__file__).resolve().parents[2]
FESTIVAL_POSTER = PROJECT_ROOT / "assets" / "rang_o_shoor.jpg"

# متن موقت جشنواره؛ بعداً با اطلاعات نهایی جایگزین کن
FESTIVAL_DESCRIPTION = (
    "🎨 جشنواره رنگ و شور\n\n"
    "به جشنواره رنگ و شور خوش اومدی! 🎉\n"
    "برای شرکت در جشنواره، از دکمه زیر استفاده کن."
)

# شناسه عددی ادمین یا گروه دریافت‌کننده ثبت‌نام‌ها
# مقدار ADMIN_CHAT_ID را در فایل .env تنظیم کن.
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# وضعیت موقت هر کاربر؛ اطلاعات در دیتابیس ذخیره نمی‌شود.
registration_states = {}


def register_festival_handler(bot):

    @bot.message_handler(
        func=lambda message: message.text == "🎉 جشن‌ها"
    )
    def show_festivals(message):
        registration_states.pop(message.chat.id, None)

        bot.send_message(
            message.chat.id,
            "🎉 بخش جشن‌ها\n\nجشنواره موردنظرت رو انتخاب کن:",
            reply_markup=festival_menu()
        )

    @bot.message_handler(
        func=lambda message: message.text == "🎨 جشنواره رنگ و شور"
    )
    def show_festival_details(message):
        registration_states.pop(message.chat.id, None)

        if FESTIVAL_POSTER.is_file():
            with open(FESTIVAL_POSTER, "rb") as poster:
                bot.send_photo(
                    message.chat.id,
                    poster,
                    caption=FESTIVAL_DESCRIPTION,
                    reply_markup=festival_detail_menu()
                )
        else:
            bot.send_message(
                message.chat.id,
                FESTIVAL_DESCRIPTION
                + "\n\n⚠️ پوستر هنوز در پوشه assets قرار نگرفته.",
                reply_markup=festival_detail_menu()
            )

    @bot.message_handler(
        func=lambda message: message.text == "📝 ثبت‌نام جشنواره"
    )
    def start_registration(message):
        registration_states[message.chat.id] = {
            "step": "full_name",
            "data": {}
        }

        bot.send_message(
            message.chat.id,
            "لطفاً نام و نام خانوادگی خودت رو وارد کن:",
            reply_markup=cancel_keyboard()
        )

    @bot.message_handler(
        func=lambda message: message.text == "❌ لغو ثبت‌نام"
    )
    def cancel_registration(message):
        registration_states.pop(message.chat.id, None)

        bot.send_message(
            message.chat.id,
            "ثبت‌نام لغو شد.",
            reply_markup=festival_detail_menu()
        )

    @bot.message_handler(
        func=lambda message: message.text in (
            "🔙 بازگشت به جشن‌ها",
            "🏠 منوی اصلی",
            "🔙 بازگشت به منوی اصلی",
        )
    )
    def navigate_back(message):
        registration_states.pop(message.chat.id, None)

        if message.text == "🔙 بازگشت به جشن‌ها":
            bot.send_message(
                message.chat.id,
                "🎉 یکی از گزینه‌های زیر رو انتخاب کن:",
                reply_markup=festival_menu()
            )
        else:
            bot.send_message(
                message.chat.id,
                "به منوی اصلی برگشتیم.",
                reply_markup=main_menu()
            )

    @bot.message_handler(
        func=lambda message: message.chat.id in registration_states,
        content_types=["text"]
    )
    def handle_registration(message):
        chat_id = message.chat.id
        state = registration_states.get(chat_id)

        if not state:
            return

        text = (message.text or "").strip()

        if text in ("❌ لغو ثبت‌نام", "🔙 بازگشت به جشن‌ها",
                    "🏠 منوی اصلی", "🔙 بازگشت به منوی اصلی"):
            return

        if not text:
            bot.send_message(chat_id, "لطفاً پاسخ رو وارد کن.")
            return

        step = state["step"]
        data = state["data"]

        if step == "full_name":
            data["full_name"] = text
            state["step"] = "student_id"

            bot.send_message(
                chat_id,
                "شماره دانشجویی‌ات رو وارد کن:",
                reply_markup=cancel_keyboard()
            )

        elif step == "student_id":
            data["student_id"] = text
            state["step"] = "phone"

            bot.send_message(
                chat_id,
                "شماره تماس خودت رو وارد کن:",
                reply_markup=cancel_keyboard()
            )

        elif step == "phone":
            data["phone"] = text
            state["step"] = "degree"

            bot.send_message(
                chat_id,
                "مقطع تحصیلی‌ات رو انتخاب کن:",
                reply_markup=degree_menu()
            )

        elif step == "degree":
            allowed_degrees = {
                "کاردانی",
                "کارشناسی",
                "کارشناسی ارشد",
                "دکترا",
            }

            if text not in allowed_degrees:
                bot.send_message(
                    chat_id,
                    "لطفاً مقطع تحصیلی رو از گزینه‌های زیر انتخاب کن:",
                    reply_markup=degree_menu()
                )
                return

            data["degree"] = text
            state["step"] = "major"

            bot.send_message(
                chat_id,
                "رشته تحصیلی‌ات رو در یک پیام متنی وارد کن:",
                reply_markup=cancel_keyboard()
            )

        elif step == "major":
            data["major"] = text

            if not ADMIN_CHAT_ID:
                bot.send_message(
                    chat_id,
                    "متأسفانه ثبت‌نام فعلاً تکمیل نشد. لطفاً بعداً تلاش کن.",
                    reply_markup=festival_detail_menu()
                )
                registration_states.pop(chat_id, None)
                return

            admin_message = (
                "رنگ و شور ✅\n\n"
                f"👤 نام و نام خانوادگی: {data['full_name']}\n"
                f"🆔 شماره دانشجویی: {data['student_id']}\n"
                f"📞 شماره تماس: {data['phone']}\n"
                f"🎓 مقطع تحصیلی: {data['degree']}\n"
                f"📚 رشته تحصیلی: {data['major']}"
            )

            try:
                bot.send_message(
                    int(ADMIN_CHAT_ID),
                    admin_message
                )
            except Exception:
                bot.send_message(
                    chat_id,
                    "ارسال ثبت‌نام با مشکل مواجه شد. لطفاً کمی بعد دوباره تلاش کن.",
                    reply_markup=festival_detail_menu()
                )
                registration_states.pop(chat_id, None)
                return

            registration_states.pop(chat_id, None)

            bot.send_message(
                chat_id,
                "✅ ثبت‌نامت با موفقیت انجام شد!\n"
                "ممنون که در جشنواره رنگ و شور شرکت می‌کنی. 🎨",
                reply_markup=festival_detail_menu()
            )


def cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton("❌ لغو ثبت‌نام"))
    return keyboard
