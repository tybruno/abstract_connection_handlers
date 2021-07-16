from abstract_connection_handlers.abstract_connections_handlers import (
    AuthenticationDetails,
)
from typing import Type
from dataclasses import fields


class TestAuthenticationDetails:
    def test__call(self):

        auth_details: Type[
            AuthenticationDetails
        ] = AuthenticationDetails.default_args()
        details = auth_details(auth_username="hello")
        print(details)
