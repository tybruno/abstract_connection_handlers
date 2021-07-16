import pytest
from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    AuthenticationDetails,
    ConnectionDetails,
    HandlerDetails,
)

AUTH_USERNAME = "auth_username"
AUTH_PASSWORD = "auth_password"
AUTH_SECONDARY = "auth_secondary"


@pytest.fixture
def empty_auth_details():
    return AuthenticationDetails()


@pytest.fixture
def auth_details():
    return AuthenticationDetails(
        auth_username=AUTH_USERNAME,
        auth_secondary=AUTH_SECONDARY,
    )


@pytest.fixture
def connection_details():
    return ConnectionDetails()


@pytest.fixture
def empty_handler_details():
    ...
    # return HandlerDetails()


@pytest.fixture
def handler_details(auth_details, connection_details):
    return HandlerDetails(
        auth_details=auth_details, connection_details=connection_details
    )
