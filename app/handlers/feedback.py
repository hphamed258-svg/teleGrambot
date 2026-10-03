from telebot import TeleBot

from app.config import ADMIN_ID
from app.keyboards.main_menu import main_menu
from app.keyboards.cooperation_menu import cancel_menu


def register_feedback_handler(bot: TeleBot):

    @bot.message_handler(
        func=lambda message:
        message.text == "💡 پیشنهادات و انتقادات"
    )
    def start_feedback(message):

        bot.send_message(
            message.chat.id,
            "لطفاً پیشنهاد یا انتقاد خود را ارسال کنید:",
            reply_markup=cancel_menu()
        )

        bot.register_next_step_handler(
            message,
            receive_feedback
        )

    def receive_feedback(message):

        if message.text == "❌ انصراف":

            bot.send_message(
                message.chat.id,
                "درخواست شما لغو شد.",
                reply_markup=main_menu()
            )

            return

        user = message.from_user

        username = (
            f"@{user.username}"
            if user.username
            else "ندارد"
        )

        feedback_text = message.text

        admin_message = (
            "💡 پیشنهاد یا انتقاد جدید\n\n"
            f"👤 نام: {user.first_name}\n"
            f"🔗 Username: {username}\n"
            f"🆔 Telegram ID: {user.id}\n\n"
            "📝 متن:\n"
            f"{feedback_text}"
        )

        bot.send_message(
            ADMIN_ID,
            admin_message
        )

        bot.send_message(
            message.chat.id,
            "پبام شما با موفقیت ارسال شد",
            reply_markup=main_menu()
        )