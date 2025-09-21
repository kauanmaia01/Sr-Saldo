from bot.bot_instance import bot
from bot.handlers import start, actions

if __name__ == "__main__":
    print("🤖 Bot está rodando...")
    bot.infinity_polling(timeout=60, long_polling_timeout=55)