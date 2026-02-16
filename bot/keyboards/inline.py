from telebot import types


def create_menu_inline():
    """Menu Principal"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("💰 Fluxo de Caixa", callback_data="cash_flow"),
        types.InlineKeyboardButton("📊 Investimentos", callback_data="investment"),
        types.InlineKeyboardButton("📈 Simulador de Juros Compostos", callback_data="compound_interest"),
        types.InlineKeyboardButton("❓ Ajuda", callback_data="help")
    )
    return markup


def menu_cash_flow():
    """Menu - Fluxo de Caixa"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("➕ Registrar Receita/Despesa", callback_data="money_flow"),
        types.InlineKeyboardButton("🗑️ Excluir Registro", callback_data="register_delete"),
        types.InlineKeyboardButton("⬅️ Voltar ao Menu", callback_data="create_menu_inline")
    )
    return markup


# Não Construído.
def wallets():
    """Selecionar Carteira"""

    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🟣 Nubank", callback_data="wallet_nubank"),
        types.InlineKeyboardButton("🟠 Itaú", callback_data="wallet_itau")
    )
    return markup


# Menus Investimentos
def investment_menu():
    """Menu - Investimentos"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("➕ Registrar Compra/Venda", callback_data="register_assets"),
        types.InlineKeyboardButton("🪙 Informações dos Ativos", callback_data="info_assets_menu"),
        types.InlineKeyboardButton("⬅️ Voltar ao Menu", callback_data="create_menu_inline")
    )
    return markup


def buy_sell_assets_menu():
    """Compra e Venda de Ativos"""

    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(
        types.InlineKeyboardButton("➕ Registrar Operação", callback_data="register_buy_sell_assets"),
        types.InlineKeyboardButton("🗑️ Excluir Operação", callback_data="register_delete_buy_sell_assets"),
        types.InlineKeyboardButton("⬅️ Voltar", callback_data="investment_menu")
    )
    return markup
    