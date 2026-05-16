import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Отримуємо токен з безпечних налаштувань сервера
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_TOKEN_HERE')
bot = telebot.TeleBot(BOT_TOKEN)

# URL твого Mini App (GitHub Pages, який ти вже налаштував для index.html)
# Заміни це посилання на твоє реальне посилання на Mini App!
MINI_APP_URL = "https://cypto-time-bot.vercel.app/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name if message.from_user.first_name else "Трейдер"
    
    welcome_text = (
        f"👋 Привіт, {user_name}!\n\n"
        f"Вітаємо у **CryptoTime** — твоєму кишеньковому хабі для аналізу крипторинку! 📊\n\n"
        f"У нашому додатку ти знайдеш:\n"
        f"• Актуальні курси топ-криптовалют\n"
        f"• Індекс страху та жадібності 😱/🤑\n"
        f"• Пульс ринку та твій особистий портфель\n\n"
        f"Натискай кнопку нижче, щоб запустити додаток прямо всередині Telegram 👇"
    )
    
    markup = InlineKeyboardMarkup()
    web_app = WebAppInfo(url=MINI_APP_URL)
    btn_open_app = InlineKeyboardButton(text="🚀 Запустити CryptoTime", web_app=web_app)
    markup.add(btn_open_app)
    
    bot.send_message(
        chat_id=message.chat.id, 
        text=welcome_text, 
        reply_markup=markup, 
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "ℹ️ **Довідка CryptoTime Bot**\n\n"
        "• Тисни /start, щоб відкрити головне меню з кнопкою запуску.\n"
        "• Додаток працює прямо всередині Telegram на базі технології Web App."
    )
    bot.send_message(chat_id=message.chat.id, text=help_text, parse_mode="Markdown")

if __name__ == '__main__':
    print("Бот CryptoTime успішно запущений...")
    bot.infinity_polling()
