from sqlalchemy import MetaData, Table, Column, Integer, String, Numeric

metadata_obj = MetaData()

tb_cash_flow = Table(
    "tb_cash_flow",
    metadata_obj,
    Column("operation_id", Integer(), primary_key=True),
    Column("operation_wallet", String()),
    Column("operation_type", String()),
    Column("operation_name", String()),
    Column("operation_category", String()),
    Column("operation_value", Numeric()),
    Column("operation_date", String()),
    schema="public"
)

tb_assets = Table(
    "tb_assets",
    metadata_obj,
    Column("assets_id", Integer(), primary_key=True),
    Column("assets_type", String()),
    Column("assets_name", String()),
    Column("current_quote", Numeric()),
    Column("amount", Numeric()),
    Column("buy_date", String()),
    schema="public"
)
