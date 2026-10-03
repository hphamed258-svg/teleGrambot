from telebot import TeleBot


def register_competitions_handler(bot: TeleBot):

    @bot.message_handler(
        func=lambda message: message.text == "🏆 مسابقات"
    )
    def competitions(message):

        bot.send_message(
            message.chat.id,
            "فعلاً مسابقه‌ای در حال برگزاری نیست."
        )