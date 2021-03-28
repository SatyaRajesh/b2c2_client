import sys
from app.b2c2_client import B2C2Client
import uuid
import pprint
from datetime import datetime

MAIN_MENU = "main_menu"
NEW_ORDER_RFQ = "1"
PING_TEST = "2"
BALANCE_IN_ACCOUNT = "3"
TRADE_HISTORY = "4"
SPECIFIC_TRADE = "5"
EXIT_MENU = "0"


class Menu:
    def __init__(self, client: B2C2Client) -> None:
        self._client = client
        self._current_option = 0
        self._menu_actions = {}
        self.set_menu_actions_b2c2()

    def set_menu_actions_b2c2(self) -> None:
        self._menu_actions = {
            MAIN_MENU: self.main_menu,
            NEW_ORDER_RFQ: self.new_order_rfq,
            PING_TEST: self.ping_test,
            BALANCE_IN_ACCOUNT: self.balance_in_account,
            TRADE_HISTORY: self.trade_history,
            SPECIFIC_TRADE: self.specific_trade,
            EXIT_MENU: self.exit,
        }

    def main_menu(self) -> None:
        self.clear_screen()

        print("Welcome to B2C2 Client")
        print("Operation Type:")
        print("1. New Order With Request for Quatation (RFQ)")
        print("2. Ping (test Connection)")
        print("3. Balance In Your Account")
        print("4. Trade History")
        print("5. Specific Trade Details")
        print("0. Quit")
        self._current_option = input(" >>  ")
        print(
            f"Selected Option {self._current_option} typeof:{type(self._current_option)}"
        )
        print(f"Menu Actions: {self._menu_actions}")
        return self.exec_menu()

    def back_to_main_menu(self) -> None:
        input("Press any key to main menu")
        self.main_menu()

    @staticmethod
    def clear_screen():
        print("\n" * 80)

    def exec_menu(self) -> None:
        self.clear_screen()

        if self._current_option in self._menu_actions:
            self._menu_actions[self._current_option]()
        else:
            print("INVALID OPTION: (Redirecting to main menu)")

        self.back_to_main_menu()

    def new_order_rfq(self) -> None:
        self.clear_screen()
        print("NEW ORDER via RFQ")
        print("Select Instrument")
        instruments = self._client.instruments()
        instrument_names = [each_instrument["name"] for each_instrument in instruments]
        pprint.pprint(f"List of Instruments: {instrument_names}")
        instrument = input(" >>  ")
        print("Select to Buy or Sell")
        print("1. Buy")
        print("2. Sell")
        print("Any Other character Defaults to Sell")
        side_nbr = input(" >> ")
        side = "buy" if side_nbr == "1" else "sell"
        print("Enter Quantity:")
        quantity = input(" >> ")
        try:
            val = int(quantity)
        except ValueError:
            input("Invalid Quantity")
            self.main_menu()
        current_order_uuid = str(uuid.uuid4())
        response = self._client.request_for_quote(
            instrument, side, quantity, current_order_uuid
        )
        print("Details of Balance: (Need to Calculate)")
        self.balance_in_account()
        pprint.pprint(f"Request for Quote: {response}")
        if "b2c2_error" not in response:
            print("Select to Execute This Order")
            print("1. Yes")
            print("2. No")
            print("Any Other character Defaults to No")
            execute_order = input(" >> ")
            valid_until = str(response["valid_until"])
            valid_datetime = datetime.strptime(valid_until[0:19], "%Y-%m-%dT%H:%M:%S")
            print(
                f"Valid_Until: {valid_datetime} And Current Datetime: {datetime.now()}"
            )
            if execute_order == "1" and datetime.now() > valid_datetime:
                print("Valid Data - Executing the Order")
                self._client.new_order()
        input("Done With Execution")

    def ping_test(self) -> None:
        self.clear_screen()
        print("PING TEST")
        print("#TODO")

    def balance_in_account(self) -> None:
        self.clear_screen()
        print("BALANCE IN ACCOUNT")
        res = self._client.balance_in_account()
        pprint.pprint(f"Balance: {res}")

    def trade_history(self) -> None:
        self.clear_screen()
        print("TRADE HISTORY")
        print("#TODO")

    def specific_trade(self) -> None:
        self.clear_screen()
        print("SPECIFIC TRADE")
        print("#TODO")

    @staticmethod
    def exit():
        sys.exit()
