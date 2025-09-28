from bot.bot_instance import bot
from bot.config import USER_ID

from bot.keyboards.inline import menu_cash_flow, create_menu_inline
from bot.keyboards.inline import investment_menu, buy_sell_assets_menu

from bot.utils.compound_interest import receber_capital
from bot.utils.cash_flow import cashflow_data_request, delete_register
from bot.utils.register_assets import assets_data_request, assets_delete


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.from_user.id != USER_ID:
        return bot.answer_callback_query(call.id, "Você não tem acesso.")

    # Fluxo de Caixa

    if call.data == "cash_flow":
        bot.send_message(call.message.chat.id, "💰 Menu de Fluxo de Caixa:", reply_markup=menu_cash_flow())

    elif call.data == "money_flow":
        cashflow_data_request(call.message.chat.id)

    elif call.data == "register_delete":
        delete_register(call.message.chat.id)

    # Investimentos

    # Menus
    elif call.data == "investment":
        bot.send_message(call.message.chat.id, "Selecione uma das opções abaixo:", reply_markup=investment_menu())

    elif call.data == "register_assets":
        bot.send_message(call.message.chat.id, "Opções Ações:", reply_markup=buy_sell_assets_menu())

    elif call.data == "register_buy_sell_assets":
        assets_data_request(call.message.chat.id)

    elif call.data == "register_delete_buy_sell_assets":
        assets_delete(call.message.chat.id)


    # Calculadora de Juros Compostos

    elif call.data == "compound_interest":
        msg = bot.send_message(call.message.chat.id, "Digite o capital inicial (Ex.: 1.000,00): ")
        bot.register_next_step_handler(msg, receber_capital)

    # Help

    elif call.data == "help":
        bot.send_message(call.message.chat.id, "Use os botões para acessar as funcionalidades.")

    # Retornar ao menu anterior

    elif call.data == "create_menu_inline":
        bot.send_message(call.message.chat.id, "⬅️ Voltando ao menu principal:", reply_markup=create_menu_inline())

    elif call.data == "investment_menu":
        bot.send_message(call.message.chat.id, "⬅️ Voltando ao menu investimento:", reply_markup=investment_menu())



