from telebot import TeleBot
from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.cooperation_menu import (
    cooperation_menu,
    content_menu,
    cancel_menu,
    phone_menu
)


# اطلاعات موقت کاربرها
user_data = {}


def register_cooperation_handler(bot: TeleBot):

    @bot.message_handler(
        func=lambda message:
        message.text == "🤝 همکاری با ما"
    )
    def start_cooperation(message):

        bot.send_message(
            message.chat.id,
            "لطفاً زمینه‌ای که مایل به همکاری در آن هستید را انتخاب کنید:",
            reply_markup=cooperation_menu()
        )


    # -------------------------
    # بازگشت از منوی همکاری
    # -------------------------

    @bot.message_handler(
        func=lambda message:
        message.text == "🔙 بازگشت"
    )
    def back_button(message):

        bot.send_message(
            message.chat.id,
            "به منوی اصلی برگشتید.",
            reply_markup=main_menu()
        )


    # -------------------------
    # امور آموزشی
    # -------------------------

    @bot.message_handler(
        func=lambda message:
        message.text == "📚 امور آموزشی"
    )
    def education(message):

        start_form(
            message,
            "📚 امور آموزشی"
        )


    # -------------------------
    # امور اجرایی
    # -------------------------

    @bot.message_handler(
        func=lambda message:
        message.text == "⚙️ امور اجرایی"
    )
    def executive(message):

        start_form(
            message,
            "⚙️ امور اجرایی"
        )


    # -------------------------
    # تولید محتوا
    # -------------------------

    @bot.message_handler(
        func=lambda message:
        message.text == "🎨 تولید محتوا"
    )
    def content(message):

        bot.send_message(
            message.chat.id,
            "لطفاً زمینه مورد نظر خود را انتخاب کنید:",
            reply_markup=content_menu()
        )


    # -------------------------
    # زمینه‌های تولید محتوا
    # -------------------------

    content_options = {
        "🎨 طراحی پوستر": "🎨 طراحی پوستر",
        "🎙 گویندگی پادکست": "🎙 گویندگی پادکست",
        "🎧 صداگذاری و ضبط پادکست": "🎧 صداگذاری و ضبط پادکست",
        "📝 تهیه متن پادکست": "📝 تهیه متن پادکست",
        "📱 مدیریت شبکه‌های اجتماعی": "📱 مدیریت شبکه‌های اجتماعی",
        "📸 عکاسی و فیلم‌برداری": "📸 عکاسی و فیلم‌برداری",
    }

    @bot.message_handler(
        func=lambda message:
        message.text in content_options
    )
    def content_option(message):

        start_form(
            message,
            "🎨 تولید محتوا",
            content_options[message.text]
        )


    # -------------------------
    # سایر
    # -------------------------

    @bot.message_handler(
        func=lambda message:
        message.text == "💡 سایر"
    )
    def other(message):

        user_data[message.from_user.id] = {
            "type": "other"
        }

        bot.send_message(
            message.chat.id,
            "لطفاً زمینه‌ای که مایل به همکاری در آن هستید را برای ما توضیح دهید. 📝",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            receive_other
        )


    def receive_other(message):

        user_id = message.from_user.id

        if message.text == "❌ انصراف":

            user_data.pop(user_id, None)

            bot.send_message(
                message.chat.id,
                "❌ درخواست همکاری لغو شد.",
                reply_markup=main_menu()
            )

            return

        user = message.from_user

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        admin_message = (
            "🤝 درخواست همکاری جدید - سایر\n\n"
            f"👤 نام: {user.first_name}\n"
            f"🔗 Username: {username}\n"
            f"🆔 Telegram ID: {user.id}\n\n"
            "📝 توضیحات:\n"
            f"{message.text}"
        )

        bot.send_message(
            ADMIN_ID,
            admin_message
        )

        user_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "✅ درخواست همکاری شما با موفقیت ارسال شد.",
            reply_markup=main_menu()
        )


    # -------------------------
    # شروع فرم همکاری
    # -------------------------

    def start_form(message, category, subcategory=None):

        user_id = message.from_user.id

        user_data[user_id] = {
            "category": category,
            "subcategory": subcategory,
            "step": "name"
        }

        bot.send_message(
            message.chat.id,
            "👤 لطفاً نام و نام خانوادگی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_name
        )


    # -------------------------
    # نام
    # -------------------------

    def get_name(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["name"] = message.text
        user_data[user_id]["step"] = "phone"

        bot.send_message(
            message.chat.id,
            "📱 لطفاً شماره تلفن خود را ارسال کنید.\n\n"
            "برای ارسال شماره تلفن، دکمه زیر را بزنید.",
            reply_markup=phone_menu()
        )

        bot.register_next_step_handler(
            message,
            get_phone
        )


    # -------------------------
    # شماره تلفن
    # -------------------------

    def get_phone(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        if not message.contact:

            bot.send_message(
                message.chat.id,
                "لطفاً با استفاده از دکمه «📱 ارسال شماره تلفن» "
                "شماره خود را ارسال کنید."
            )

            bot.register_next_step_handler(
                message,
                get_phone
            )

            return

        if message.contact.user_id != user_id:

            bot.send_message(
                message.chat.id,
                "لطفاً شماره تلفن خودتان را با استفاده از دکمه زیر ارسال کنید.",
                reply_markup=phone_menu()
            )

            bot.register_next_step_handler(
                message,
                get_phone
            )

            return

        user_data[user_id]["phone"] = message.contact.phone_number
        user_data[user_id]["step"] = "major"

        bot.send_message(
            message.chat.id,
            "🎓 لطفاً رشته تحصیلی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_major
        )


    # -------------------------
    # رشته
    # -------------------------

    def get_major(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["major"] = message.text
        user_data[user_id]["step"] = "degree"

        bot.send_message(
            message.chat.id,
            "📚 لطفاً مقطع تحصیلی خود را وارد کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_degree
        )


    # -------------------------
    # مقطع
    # -------------------------

    def get_degree(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["degree"] = message.text
        user_data[user_id]["step"] = "experience"

        bot.send_message(
            message.chat.id,
            "💼 لطفاً درباره سابقه یا مهارت مرتبط خود توضیح دهید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_experience
        )


    # -------------------------
    # سابقه و مهارت
    # -------------------------

    def get_experience(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["experience"] = message.text
        user_data[user_id]["step"] = "motivation"

        bot.send_message(
            message.chat.id,
            "💭 چرا علاقه‌مند به همکاری با انجمن علمی هستید؟",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_motivation
        )


    # -------------------------
    # انگیزه
    # -------------------------

    def get_motivation(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["motivation"] = message.text
        user_data[user_id]["step"] = "portfolio"

        bot.send_message(
            message.chat.id,
            "🔗 اگر نمونه‌کار دارید، لینک آن را ارسال کنید.\n\n"
            "اگر نمونه‌کار ندارید، بنویسید «ندارم».",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            get_portfolio
        )


    # -------------------------
    # نمونه کار
    # -------------------------

    def get_portfolio(message):

        user_id = message.from_user.id

        if is_cancel(message):
            return

        user_data[user_id]["portfolio"] = message.text

        send_application_to_admin(
            message
        )


    # -------------------------
    # ارسال فرم برای ادمین
    # -------------------------

    def send_application_to_admin(message):

        user_id = message.from_user.id
        user = message.from_user
        data = user_data[user_id]

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        category = data["category"]

        subcategory = data["subcategory"]

        admin_message = (
            "🤝 درخواست همکاری جدید\n\n"
            f"👤 نام و نام خانوادگی:\n"
            f"{data['name']}\n\n"

            f"🔗 Username:\n"
            f"{username}\n\n"

            f"🆔 Telegram ID:\n"
            f"{user.id}\n\n"

            f"📱 شماره تماس:\n"
            f"{data['phone']}\n\n"

            f"🎓 رشته:\n"
            f"{data['major']}\n\n"

            f"📚 مقطع:\n"
            f"{data['degree']}\n\n"

            f"📌 حوزه همکاری:\n"
            f"{category}\n"
        )

        if subcategory:
            admin_message += (
                f"\n🔹 زمینه:\n"
                f"{subcategory}\n"
            )

        admin_message += (
            f"\n💼 سابقه و مهارت:\n"
            f"{data['experience']}\n\n"

            f"💭 انگیزه همکاری:\n"
            f"{data['motivation']}\n\n"

            f"🔗 نمونه‌کار:\n"
            f"{data['portfolio']}"
        )

        bot.send_message(
            ADMIN_ID,
            admin_message
        )

        user_data.pop(user_id, None)

        bot.send_message(
            message.chat.id,
            "✅ درخواست همکاری شما با موفقیت ارسال شد.",
            reply_markup=main_menu()
        )


    # -------------------------
    # بررسی انصراف
    # -------------------------

    def is_cancel(message):

        if message.text == "❌ انصراف":

            user_data.pop(
                message.from_user.id,
                None
            )

            bot.send_message(
                message.chat.id,
                "❌ درخواست همکاری لغو شد.",
                reply_markup=main_menu()
            )

            return True

        return False