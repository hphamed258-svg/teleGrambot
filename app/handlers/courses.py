from telebot import TeleBot


def register_courses_handler(bot: TeleBot):

    @bot.message_handler(
        func=lambda message: message.text == "📚 دوره‌ها"
    )
    def courses(message):

        bot.send_message(
            message.chat.id,
            "فعلاً دوره‌ای در حال برگزاری نیست."
        )