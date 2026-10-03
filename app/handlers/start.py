from telebot import TeleBot

from app.keyboards.main_menu import main_menu


def register_start_handler(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def start(message):

        text = (
            "سلام👋\n"
            "به ربات انجمن علمی پردیس مهریز خوش آمدید 🎓\n"
            "لطفاً از بین گزینه های زیر یک گزینه را انتخاب کنید"
        )

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=main_menu()
        )