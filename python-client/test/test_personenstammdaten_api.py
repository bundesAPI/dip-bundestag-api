"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.dip_bundestag.api.personenstammdaten_api import (  # noqa: E501
    PersonenstammdatenApi,
)

from deutschland import dip_bundestag


class TestPersonenstammdatenApi(unittest.TestCase):
    """PersonenstammdatenApi unit test stubs"""

    def setUp(self):
        self.api = PersonenstammdatenApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_person(self):
        """Test case for get_person

        Liefert Personenstammdaten zu einer Person  # noqa: E501
        """
        pass

    def test_get_person_list(self):
        """Test case for get_person_list

        Liefert eine Liste von Personenstammdaten  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()