import sys
from dependency_injector.wiring import inject, Provide
from menu.menu import Menu
from app.b2c2_client import B2C2Client
from dependency_injection.container import Container


@inject
def main_menu(
    b2c2_client: B2C2Client = Provide[Container.b2c2_client],
):
    my_menu = Menu(b2c2_client)
    my_menu.main_menu()


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.config.from_ini("config.ini")
    container.wire(modules=[sys.modules[__name__]])

    main_menu()