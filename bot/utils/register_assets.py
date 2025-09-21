from bot.bot_instance import bot
from bot.keyboards.inline import buy_sell_assets_menu
from bot.database.db_instance import DbInstance
from bot.database.tables_obj import tb_assets


# Registrar Ativos
def assets_data_request(chat_id):
    text = (
        "Digite o item do fluxo de caixa:\n\n"
        "Formato:\n"
        "`Tipo do Ativo, Nome do Ativo, Cotação Atual, Quantidade, Data de Compra.`\n\n"
    )
    msg = bot.send_message(chat_id, text, parse_mode="Markdown")
    bot.register_next_step_handler(msg, register_user)


def register_user(message):
    try:
        text_user = message.text
        response = register_assets(text_user)
        bot.send_message(message.chat.id, f"✅ Registro salvo com sucesso! ID do registro: {response}")
    except Exception as e:
        print("Erro:", e)
        bot.send_message(message.chat.id, "❌ Formato inválido. Tente novamente.")
        bot.register_next_step_handler(message, register_user)
        return  
    
    bot.send_message(message.chat.id, "📋 O que você deseja fazer agora?", reply_markup=buy_sell_assets_menu())



def register_assets(info_user: str) -> int:
    db_client = pointer_with_database

    assets_type, assets_name, current_quote, amount, buy_date = info_user.split(',')
    
    response = db_client.insert_data(
        table_obj=tb_assets,
        id_name='assets_id',
        assets_type=assets_type,
        assets_name=assets_name,
        current_quote=current_quote,
        amount=amount,
        buy_date=buy_date
    )
    return response


# Deletar Ativos
def assets_delete(chat_id):
    msg = bot.send_message(chat_id, text="Qual é o ID do registro que você deseja deletar: ")
    bot.register_next_step_handler(msg, row_delete)


def row_delete(message):
    try:
        text_user = int(message.text)
        pointer_with_database.delete_data(table_obj=tb_assets, column='assetes_id', value=str(text_user))
        bot.send_message(message.chat.id, f"✅ Registro deleta com sucesso")
    except Exception as e:
        print("Erro:", e)
        bot.send_message(message.chat.id, "❌ Formato inválido. Tente novamente.")
        bot.register_next_step_handler(message, register_user)
        return
    
    bot.send_message(message.chat.id, "📋 O que você deseja fazer agora?", reply_markup=buy_sell_assets_menu())


# Conexão com o banco de dados
pointer_with_database = DbInstance()
