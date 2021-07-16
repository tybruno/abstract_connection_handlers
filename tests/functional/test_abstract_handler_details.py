from abstract_connection_handlers.abstract_connections_handlers.abstract_handler_details import (
    HandlerDetails,
)


class TestAbstractHandlerDetails:
    def test__init(self, auth_details):
        def no_params():
            details = HandlerDetails()
            assert details.auth_details == UNSET_VARIABLE
            assert details.connection_details == UNSET_VARIABLE

        def only_auth_details():
            details = HandlerDetails(auth_details=auth_details)
            assert details.auth_details == auth_details
            assert (
                details.auth_details.auth_username
                == auth_details.auth_username
            )
            assert (
                details.auth_details.auth_password
                == auth_details.auth_password
            )
            assert (
                details.auth_details.auth_secondary
                == auth_details.auth_secondary
            )

        no_params()
        only_auth_details()

    def test_as_dict(self, auth_details):
        def all_unset_variables():
            handler = HandlerDetails()
            dictionary = handler.as_dict()
            assert isinstance(dictionary, dict)
            assert len(dictionary) == 0

        def set_varialbes():
            handler = HandlerDetails(auth_details=auth_details)
            dictionary = handler.as_dict()
            assert isinstance(dictionary, dict)

            print(dictionary)

        # all_unset_variables()
        set_varialbes()
