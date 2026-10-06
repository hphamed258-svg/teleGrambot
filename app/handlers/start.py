from telebot import TeleBot

from app.keyboards.main_menu import main_menu


def register_start_handler(bot: TeleBot):

    @bot.message_handler(commands=["start"])
    def start(message):

        text = '''سلام 👋✨

به ربات انجمن علمی مهندسی کامپیوتر
پردیس مهریز خوش اومدی! 🎓💻

اینجا قراره در جریان برنامه‌ها و فعالیت‌های انجمن باشی 🚀

📌 ثبت‌نام در مراسم و رویدادها
🤝 همکاری با انجمن
💬 ارسال پیشنهاد و انتقاد

از منوی زیر انتخاب کن 👇
'''

        bot.send_message(
            message.chat.id,
            text,
            reply_markup=main_menu()
        )