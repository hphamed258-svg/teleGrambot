from telebot import TeleBot

from app.keyboards.main_menu import main_menu


def register_start_handler(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def start(message):

        text = (
            "سلام👋\n"
            "به ربات انجمن علمی مهندسی کامپیوتر پردیس مهریز خوش آمدید 🎓\n"
            "شما میتوانید از طریق این ربات در مراسمات ثبت نام کنید،برای همکاری با ما درخواست دهید و یا پیشنهادات و انتقادات خودتون رو باهامون در میون بذارید"
        )

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=main_menu()
        )