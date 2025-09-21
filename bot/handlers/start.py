from bot.bot_instance import bot
from bot.config import USER_ID
from bot.keyboards.inline import create_menu_inline

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id == USER_ID:
        bot.send_message(
            message.chat.id,
            f"Olá, {message.from_user.first_name}! Escolha uma opção abaixo:",
            reply_markup=create_menu_inline()
        )
    else:
        bot.send_message(message.chat.id, "Você não tem acesso.")
