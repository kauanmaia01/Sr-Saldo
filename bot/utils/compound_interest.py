from bot.bot_instance import bot
from bot.keyboards.inline import create_menu_inline


def calc_juros_composto(capital_inicial: float, taxa_anual: float, aporte_mensal: float, anos: int):
    i = (taxa_anual / 100) / 12  # taxa mensal
    n = anos * 12  # total de meses

    montante_inicial = capital_inicial * (1 + i) ** n
    montante_aportes = aporte_mensal * (((1 + i) ** n - 1) / i)

    return montante_inicial + montante_aportes


def receber_capital(message):
    try:
        capital = str(message.text)
        capital = float(capital.replace('.','').replace(',', '.'))
        msg = bot.send_message(message.chat.id, "Digite a taxa anual em % (Ex.: 13,50): ")
        bot.register_next_step_handler(msg, receber_taxa, capital)
    except ValueError:
        bot.send_message(message.chat.id, "Valor inválido. Digite um número para o capital.")
        bot.register_next_step_handler(message, receber_capital)


def receber_taxa(message, capital):
    try:
        taxa = str(message.text)
        taxa = float(taxa.replace(',', '.'))
        msg = bot.send_message(message.chat.id, "Digite o aporte mensal (Ex.: 259,00): ")
        bot.register_next_step_handler(msg, receber_aportes, capital, taxa)
    except ValueError:
        bot.send_message(message.chat.id, "Valor inválido. Digite um número para a taxa.")
        bot.register_next_step_handler(message, receber_taxa, capital)


def receber_aportes(message, capital, taxa):
    try:
        aporte = str(message.text)
        aporte = float(aporte.replace('.','').replace(',', ''))
        msg = bot.send_message(message.chat.id, "Digite o número de anos (Ex.: 1): ")
        bot.register_next_step_handler(msg, receber_anos, capital, taxa, aporte)
    except ValueError:
        bot.send_message(message.chat.id, "Valor inválido. Digite o aporte mensal.")
        bot.register_next_step_handler(message, receber_aportes, capital, taxa)


def receber_anos(message, capital, taxa, aporte):
    try:
        anos = int(message.text)
        resultado = calc_juros_composto(capital, taxa, aporte, anos)
        total_aportado = capital + (aporte * 12 * anos)
        juros = resultado - total_aportado

        texto = (
            f"📈 Simulação de Juros Compostos:\n\n"
            f"➡️ Capital inicial: R$ {capital:,.2f}\n"
            f"➡️ Taxa anual: {taxa:.2f}%\n"
            f"➡️ Aporte mensal: R$ {aporte:,.2f}\n"
            f"➡️ Tempo: {anos} anos\n\n"
            f"💰 Valor futuro: R$ {resultado:,.2f}\n"
            f"💸 Total investido: R$ {total_aportado:,.2f}\n"
            f"📊 Juros obtidos: R$ {juros:,.2f}"
        )
        texto = texto.replace(',', 'X').replace('.', ',').replace('X', '.')
        bot.send_message(message.chat.id, texto)

    except ValueError:
        bot.send_message(message.chat.id, "Valor inválido. Digite um número inteiro para os anos.")
        bot.register_next_step_handler(message, receber_anos, capital, taxa, aporte)
    
    bot.send_message(message.chat.id, "📋 O que você deseja fazer agora?", reply_markup=create_menu_inline())
