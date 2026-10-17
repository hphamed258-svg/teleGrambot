
import logging
import os
from pathlib import Path

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from app.keyboards.main_menu import main_menu
from app.keyboards.festival_menu import (
    festival_menu,
    festival_detail_menu,
    degree_menu,
    cancel_keyboard,
    phone_keyboard,
    retry_keyboard,
)


logger = logging.getLogger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parents[1]
FESTIVAL_POSTER = PROJECT_ROOT / "assets" / "rang_o_shoor.jpg"

FESTIVAL_DESCRIPTION = """🎊 ثبت‌نام جشنواره رنگ و شور

آماده‌اید برای دو شب پر از رنگ، هیجان و تجربه‌های تازه؟ 💥
از بازی‌های هیجان‌انگیز و بردگیم‌های متنوع گرفته تا غرفه‌های خوراکی، دست‌سازه‌ها و آثار هنری؛ قراره کلی تجربه‌ی جذاب کنار هم داشته باشیم 🎮🛍
توضیحات بازی‌ها رو به‌زودی براتون می‌ذاریم؛ پس منتظر باشید! 👀

پذیرایی هم براتون در نظر گرفتیم که با حال بهتری کنارمون باشین 🍪
سرویس رفت‌وبرگشت هم برای رفت‌وآمد شما عزیزان فراهم شده 🚌

📅 زمان: دوشنبه و سه‌شنبه، ۲۷ و ۲۸ مهر
⏰ ساعت: ۱۸ تا ۲۲
📍 مکان: پردیس مهریز دانشگاه یزد

🔔 برای شرکت در جشنواره، ثبت‌نامتون رو تکمیل کنید.
 منتظرتونیم تا کنار هم دو شب خاطره‌انگیز بسازیم 🧡

برای اطلاعات بیشتر، به آیدی زیر پیام بدید:

@CEPM_admin
"""

ALLOWED_DEGREES = {
    "کاردانی",
    "کارشناسی",
    "کارشناسی ارشد",
    "دکترا",
}

# نگهداری موقت اطلاعات ثبت‌نام در حافظه
registration_states = {}


def register_festival_handler(bot):

    @bot.message_handler(
        func=lambda message: message.text == "🎉 جشن‌ها"
    )
    def show_festivals(message):
        registration_states.pop(message.chat.id, None)

        bot.send_message(
            message.chat.id,
            "لطفاً جشن موردنظر خود را انتخاب کنید:",
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
                + "\n\nپوستر جشنواره هنوز بارگذاری نشده است.",
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
            "لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=cancel_keyboard()
        )

    @bot.message_handler(
        func=lambda message: message.text == "❌ لغو ثبت‌نام"
    )
    def cancel_registration(message):
        registration_states.pop(message.chat.id, None)

        bot.send_message(
            message.chat.id,
            "ثبت‌نام شما لغو شد.",
            reply_markup=festival_detail_menu()
        )

    @bot.message_handler(
        func=lambda message: (
            message.text == "🔄 تلاش مجدد برای ثبت‌نام"
            and message.chat.id in registration_states
        )
    )
    def retry_registration(message):
        state = registration_states.get(message.chat.id)

        if state and state.get("step") == "retry":
            send_registration_to_admin(
                bot,
                message.chat.id,
                state
            )

    @bot.message_handler(
        func=lambda message: message.text in {
            "🔙 بازگشت به جشن‌ها",
            "🔙 بازگشت به منوی اصلی",
            "🏠 منوی اصلی",
        }
    )
    def navigate_back(message):
        registration_states.pop(message.chat.id, None)

        if message.text == "🔙 بازگشت به جشن‌ها":
            bot.send_message(
                message.chat.id,
                "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
                reply_markup=festival_menu()
            )
        else:
            bot.send_message(
                message.chat.id,
                "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:",
                reply_markup=main_menu()
            )

    @bot.message_handler(
        func=lambda message: message.chat.id in registration_states,
        content_types=["text", "contact"]
    )
    def handle_registration(message):
        chat_id = message.chat.id
        state = registration_states.get(chat_id)

        if not state:
            return

        text = (message.text or "").strip()

        # دکمه‌های ناوبری توسط هندلرهای اختصاصی مدیریت می‌شوند.
        if text in {
            "❌ لغو ثبت‌نام",
            "🔙 بازگشت به جشن‌ها",
            "🔙 بازگشت به منوی اصلی",
            "🏠 منوی اصلی",
            "🔄 تلاش مجدد برای ثبت‌نام",
        }:
            return

        data = state["data"]
        step = state["step"]
        data["username"] = message.from_user.username or "ندارد"

        if step == "full_name":
            if message.content_type != "text" or not text:
                bot.send_message(
                    chat_id,
                    "لطفاً نام و نام خانوادگی خود را به‌صورت متنی وارد کنید:",
                    reply_markup=cancel_keyboard()
                )
                return

            data["full_name"] = text
            state["step"] = "student_id"

            bot.send_message(
                chat_id,
                "لطفاً شماره دانشجویی خود را وارد کنید:",
                reply_markup=cancel_keyboard()
            )

        elif step == "student_id":
            if message.content_type != "text" or not text:
                bot.send_message(
                    chat_id,
                    "لطفاً شماره دانشجویی خود را به‌صورت متنی وارد کنید:",
                    reply_markup=cancel_keyboard()
                )
                return

            data["student_id"] = text
            state["step"] = "phone"

            bot.send_message(
                chat_id,
                "لطفاً شماره تماس خود را با دکمه زیر ارسال کنید. "
                "در صورت نیاز می‌توانید شماره را دستی نیز وارد کنید:",
                reply_markup=phone_keyboard()
            )

        elif step == "phone":
            if message.content_type == "contact":
                contact = message.contact

                if (
                    contact.user_id is not None
                    and contact.user_id != message.from_user.id
                ):
                    bot.send_message(
                        chat_id,
                        "لطفاً شماره تماس متعلق به خود را ارسال کنید:",
                        reply_markup=phone_keyboard()
                    )
                    return

                phone = contact.phone_number

            elif message.content_type == "text":
                phone = text.replace(" ", "").replace("-", "")

                if not phone.lstrip("+").isdigit():
                    bot.send_message(
                        chat_id,
                        "لطفاً شماره تماس معتبر وارد کنید یا از دکمه ارسال شماره تماس استفاده کنید:",
                        reply_markup=phone_keyboard()
                    )
                    return
            else:
                bot.send_message(
                    chat_id,
                    "لطفاً شماره تماس خود را ارسال کنید:",
                    reply_markup=phone_keyboard()
                )
                return

            data["phone"] = phone
            state["step"] = "degree"

            bot.send_message(
                chat_id,
                "لطفاً مقطع تحصیلی خود را انتخاب کنید:",
                reply_markup=degree_menu()
            )

        elif step == "degree":
            if (
                message.content_type != "text"
                or text not in ALLOWED_DEGREES
            ):
                bot.send_message(
                    chat_id,
                    "لطفاً مقطع تحصیلی خود را از گزینه‌های زیر انتخاب کنید:",
                    reply_markup=degree_menu()
                )
                return

            data["degree"] = text
            state["step"] = "major"

            bot.send_message(
                chat_id,
                "لطفاً رشته تحصیلی خود را در قالب یک پیام متنی ارسال کنید:",
                reply_markup=cancel_keyboard()
            )

        elif step == "major":
            if message.content_type != "text" or not text:
                bot.send_message(
                    chat_id,
                    "لطفاً رشته تحصیلی خود را در قالب یک پیام متنی ارسال کنید:",
                    reply_markup=cancel_keyboard()
                )
                return

            data["major"] = text

            required_fields = (
                "full_name",
                "student_id",
                "phone",
                "degree",
                "major",
            )

            if not all(data.get(field) for field in required_fields):
                bot.send_message(
                    chat_id,
                    "اطلاعات ثبت‌نام کامل نیست. لطفاً ثبت‌نام را دوباره آغاز کنید.",
                    reply_markup=festival_detail_menu()
                )
                registration_states.pop(chat_id, None)
                return

            state["step"] = "retry"

            send_registration_to_admin(
                bot,
                chat_id,
                state
            )


def send_registration_to_admin(bot, chat_id, state):
    data = state["data"]
    admin_chat_id = os.getenv("ADMIN_ID")

    if not admin_chat_id:
        logger.error("ADMIN_CHAT_ID is not configured.")

        bot.send_message(
            chat_id,
            "ثبت‌نام شما هنوز نهایی نشده است؛ "
            "تنظیمات مقصد دریافت ثبت‌نام نیاز به بررسی دارد.",
            reply_markup=retry_keyboard()
        )
        return

    try:
        admin_chat_id = int(admin_chat_id)

        admin_message = (
            "رنگ و شور ✅\n\n"
            f"\n👤 آیدی تلگرام: @{data['username']}"
            f"👤 نام و نام خانوادگی: {data['full_name']}\n"
            f"🆔 شماره دانشجویی: {data['student_id']}\n"
            f"📞 شماره تماس: {data['phone']}\n"
            f"🎓 مقطع تحصیلی: {data['degree']}\n"
            f"📚 رشته تحصیلی: {data['major']}"
        )

        bot.send_message(
            admin_chat_id,
            admin_message
        )

    except Exception:
        logger.exception(
            "Failed to send festival registration to admin."
        )

        bot.send_message(
            chat_id,
            "ارسال اطلاعات ثبت‌نام با مشکل مواجه شد. "
            "اطلاعات شما حفظ شده است؛ لطفاً دوباره تلاش کنید.",
            reply_markup=retry_keyboard()
        )
        return

    registration_states.pop(chat_id, None)

    bot.send_message(
        chat_id,
        "✅ ثبت‌نام شما با موفقیت انجام شد!\n"
        "از شرکت شما در جشنواره رنگ و شور سپاسگزاریم. 🎨",
        reply_markup=festival_detail_menu()
    )
