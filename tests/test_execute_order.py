import pytest
from dependency_injection.container import Container
from tests.fake.fake_session import fake_session


@pytest.fixture
def container():
    container = Container()
    return container


def test_sample_get(container):
    with container.client_session.override(fake_session):
        # Set the get return value as per requirements fake_session

        fake_b2c2_client = container.b2c2_client()
        my_instruments = fake_b2c2_client.instruments()
        # Assert Instrument
