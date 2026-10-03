import telebot

from app.config import API_TOKEN

from app.handlers.start import register_start_handler
from app.handlers.workshops import register_workshops_handler
from app.handlers.courses import register_courses_handler
from app.handlers.competitions import register_competitions_handler
from app.handlers.feedback import register_feedback_handler
from app.handlers.cooperation import register_cooperation_handler


bot = telebot.TeleBot(API_TOKEN)


register_start_handler(bot)
register_workshops_handler(bot)
register_courses_handler(bot)
register_competitions_handler(bot)
register_feedback_handler(bot)
register_cooperation_handler(bot)


print("Bot is running...")

bot.infinity_polling()