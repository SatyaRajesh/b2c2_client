REQUEST_FOR_QUOTE_KEY = "request_for_quote"
NEW_ORDER_KEY = "order"
INSTRUMENT_KEY = "instrument"
TRADE_KEY = "trade"
BALANCE_KEY = "balance"
HISTORY_KEY = "history"

RELATIVE_DATA = {
    REQUEST_FOR_QUOTE_KEY: {"url": "/request_for_quote/"},
    NEW_ORDER_KEY: {"url": "/order/"},
    INSTRUMENT_KEY: {"url": "/instruments/"},
    TRADE_KEY: {"url": "/trade/"},
    BALANCE_KEY: {"url": "/balance/"},
    HISTORY_KEY: {"url": "/history/"},
}


def get_request_for_quote_url() -> str:
    return RELATIVE_DATA[REQUEST_FOR_QUOTE_KEY]["url"]


def get_new_order_url() -> str:
    return RELATIVE_DATA[NEW_ORDER_KEY]["url"]


def get_instruments_url() -> str:
    return RELATIVE_DATA[INSTRUMENT_KEY]["url"]


def get_balance_url() -> str:
    return RELATIVE_DATA[BALANCE_KEY]["url"]