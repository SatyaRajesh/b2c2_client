from requests import Session
from requests.adapters import Response
from app.service_api import ServiceApi
from utils.url_mapping import (
    get_request_for_quote_url,
    get_new_order_url,
    get_instruments_url,
    get_balance_url,
)


class B2C2Client(ServiceApi):
    def __init__(self, session: Session, url: str, token: str) -> None:
        super().__init__(session, url, token)

    def instruments(self):
        return self.get_data(relative_url=get_instruments_url(), data={})

    def request_for_quote(
        self, instrument: str, side: str, quantity: str, current_order_uuid: str
    ):
        data = {
            "instrument": instrument,
            "side": side,
            "quantity": quantity,
            "client_rfq_id": current_order_uuid,
        }
        return self.post_data(relative_url=get_request_for_quote_url(), data=data)

    def new_order(self):
        data = ""
        return self.get_data(relative_url=get_new_order_url(), data=data)

    def balance_in_account(self):
        data = ""
        return self.get_data(relative_url=get_balance_url(), data=data)