from telebot import types


def create_menu_inline():
    '''Menu Principal'''

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🏦 Registrar Receitas e Gastos", callback_data="cash_flow"),
        types.InlineKeyboardButton("📊 Ver Investimentos", callback_data="investment"),
        types.InlineKeyboardButton("📈 Simulador de Juros Compostos", callback_data="compound_interest"),
        types.InlineKeyboardButton("ℹ️ Ajuda", callback_data="help")
    )
    return markup


def menu_cash_flow():
    '''Menu Principal Registrar Gastos'''

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🤑 Registrar Operação", callback_data="money_flow"),
        types.InlineKeyboardButton("🗑️ Deletar Registro", callback_data="register_delete"),
        types.InlineKeyboardButton("⬅️ Voltar", callback_data="create_menu_inline")
    )
    return markup


# Não Construído.
def wallets():
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🟣 Nu Bank", callback_data="wallet_nubank"),
        types.InlineKeyboardButton("🟠 Itaú", callback_data="wallet_itau")
    )
    return markup


# Menus Investimentos
def investment_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("📊 Registrar Compra/Venda de Ativos", callback_data="register_assets"),
        types.InlineKeyboardButton("🪙 Info. dos Ativos", callback_data="info_assets_menu"),
        types.InlineKeyboardButton("⬅️ Voltar", callback_data="create_menu_inline")
    )
    return markup


def buy_sell_assets_menu():
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("🤑 Registrar Compra/Venda", callback_data="register_buy_sell_assets"),
        types.InlineKeyboardButton("🗑️ Deletar Registro", callback_data="register_delete_buy_sell_assets"),
        types.InlineKeyboardButton("⬅️ Voltar", callback_data="investment_menu")
    )
    return markup
    