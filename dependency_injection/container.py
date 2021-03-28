from dependency_injector import containers, providers
import logging.config
from requests import Session
from app.b2c2_client import B2C2Client


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    active_url = None
    active_token = None

    log = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    if config.application.environment:
        active_url = config.uat.url
        active_token = config.uat.token
    else:
        # Set as per Environment
        url = None
        token = None

    client_session = providers.Singleton(Session)

    b2c2_client = providers.Factory(
        B2C2Client,
        session=client_session,
        url=active_url,
        token=active_token,
    )
