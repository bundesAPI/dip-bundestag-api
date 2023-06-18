"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.inkrafttreten import Inkrafttreten
from deutschland.dip_bundestag.model.verkuendung import Verkuendung
from deutschland.dip_bundestag.model.vorgang_deskriptor import VorgangDeskriptor
from deutschland.dip_bundestag.model.vorgang_verlinkung import VorgangVerlinkung

from deutschland import dip_bundestag

globals()["Inkrafttreten"] = Inkrafttreten
globals()["Verkuendung"] = Verkuendung
globals()["VorgangDeskriptor"] = VorgangDeskriptor
globals()["VorgangVerlinkung"] = VorgangVerlinkung
from deutschland.dip_bundestag.model.vorgang import Vorgang


class TestVorgang(unittest.TestCase):
    """Vorgang unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVorgang(self):
        """Test Vorgang"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Vorgang()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()