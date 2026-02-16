from bot.bot_instance import bot
from bot.keyboards.inline import menu_cash_flow
from bot.database.db_instance import DbInstance
from bot.database.tables_obj import tb_cash_flow


# Registrar Fluxo de Caixa
def cashflow_data_request(chat_id):
    text = (
        "💰 *Novo Registro no Fluxo de Caixa*\n\n"
        "Envie os dados no seguinte formato:\n\n"
        "`Carteira, Tipo, Nome, Categoria, Valor, Data`\n\n"
        "📌 *Exemplo:*\n"
        "`Nubank, Despesa, Camiseta Vans, Compras, 169.99, 2025-06-01`\n\n"
        "━━━━━━━━━━━━━━\n"
        "🟣 Carteira: Nubank / Itaú\n"
        "🔁 Tipo: Receita ou Despesa\n"
        "🏷 Nome: descrição do item\n"
        "📂 Categoria: ex. Alimentação, Compras\n"
        "💵 Valor: use ponto para centavos (ex: 49.90)\n"
        "📅 Data: formato AAAA-MM-DD\n\n"
        "⚠️ Separe tudo por vírgula."
    )

    msg = bot.send_message(chat_id, text, parse_mode="Markdown")
    bot.register_next_step_handler(msg, register_user)


def register_user(message):
    try:
        text_user = message.text
        response = register_cash_flow(text_user)
        bot.send_message(message.chat.id, f"✅ Registro salvo com sucesso! ID do registro: {response}")
    except Exception as e:
        print("Erro:", e)
        bot.send_message(message.chat.id, "❌ Formato inválido. Tente novamente.")
        bot.register_next_step_handler(message, register_user)
        return  
    
    bot.send_message(message.chat.id, "📋 O que você deseja fazer agora?", reply_markup=menu_cash_flow())


def register_cash_flow(info_user: str):
    db_client = pointer_with_database

    operation_wallet, operation_type, operation_name, operation_category, operation_value, operation_date = info_user.split(',')

    data = {
        'operation_wallet': operation_wallet.strip(),
        'operation_type': operation_type.strip(), 
        'operation_name': operation_name.strip(), 
        'operation_category': operation_category.strip(), 
        'operation_value': float(operation_value.strip()),
        'operation_date' : operation_date.strip()
    }

    response = db_client.insert_data(table_obj=tb_cash_flow, values=data, id_name='operation_id')
    
    return response


# Deletar Registros
def delete_register(chat_id):
    msg = bot.send_message(chat_id, text="Qual é o ID do registro que você deseja deletar: ")
    bot.register_next_step_handler(msg, row_delete)


def row_delete(message):
    try:
        text_user = str(message.text)
        pointer_with_database.delete_data(table_obj=tb_cash_flow, column='operation_id', value=text_user)
        bot.send_message(message.chat.id, f"✅ Registro deleta com sucesso")
    except Exception as e:
        print("Erro:", e)
        bot.send_message(message.chat.id, "❌ Formato inválido. Tente novamente.")
        bot.send_message(message.chat.id, reply_markup=menu_cash_flow())
        bot.register_next_step_handler(message, register_user)
        return
    
    bot.send_message(message.chat.id, "📋 O que você deseja fazer agora?", reply_markup=menu_cash_flow())




# Conexão com o banco de dados
pointer_with_database = DbInstance()
