CREATE TABLE IF NOT EXISTS public.tb_cash_flow (
    operation_id INT PRIMARY KEY,
    operation_wallet TEXT,
    operation_type TEXT,
    operation_name TEXT,
    operation_category TEXT,
    operation_value NUMERIC,
    operation_date TEXT
);

CREATE TABLE IF NOT EXISTS public.tb_assets (
    assets_id INT PRIMARY KEY,
    assets_type TEXT,
    assets_name TEXT,
    current_quote NUMERIC,
    amount NUMERIC,
    buy_date TEXT
);