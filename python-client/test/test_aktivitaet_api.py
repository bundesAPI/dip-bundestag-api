"""
    DIP Bundestag API

    Bundestag: Dokumentations- und Informationssystem für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.dip_bundestag.api.aktivitaet_api import AktivitaetApi  # noqa: E501

from deutschland import dip_bundestag


class TestAktivitaetApi(unittest.TestCase):
    """AktivitaetApi unit test stubs"""

    def setUp(self):
        self.api = AktivitaetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_aktivitaet(self):
        """Test case for aktivitaet

        Liste aller Aktivitäten  # noqa: E501
        """
        pass

    def test_aktivitaet_id(self):
        """Test case for aktivitaet_id

        Metadaten zu Aktivität  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
