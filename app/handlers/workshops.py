from telebot import TeleBot


def register_workshops_handler(bot: TeleBot):

    @bot.message_handler(
        func=lambda message: message.text == "🛠 کارگاه‌ها"
    )
    def workshops(message):

        bot.send_message(
            message.chat.id,
            "فعلاً کارگاهی در حال برگزاری نیست."
        )