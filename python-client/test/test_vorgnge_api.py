"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.dip_bundestag.api.vorgnge_api import VorgngeApi  # noqa: E501

from deutschland import dip_bundestag


class TestVorgngeApi(unittest.TestCase):
    """VorgngeApi unit test stubs"""

    def setUp(self):
        self.api = VorgngeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_vorgang(self):
        """Test case for get_vorgang

        Liefert Metadaten zu einem Vorgang  # noqa: E501
        """
        pass

    def test_get_vorgang_list(self):
        """Test case for get_vorgang_list

        Liefert eine Liste von Metadaten zu Vorgängen  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()