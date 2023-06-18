"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.drucksache_autoren_anzeige_inner import (
    DrucksacheAutorenAnzeigeInner,
)
from deutschland.dip_bundestag.model.fundstelle import Fundstelle
from deutschland.dip_bundestag.model.ressort import Ressort
from deutschland.dip_bundestag.model.urheber import Urheber
from deutschland.dip_bundestag.model.vorgangsbezug import Vorgangsbezug

from deutschland import dip_bundestag

globals()["DrucksacheAutorenAnzeigeInner"] = DrucksacheAutorenAnzeigeInner
globals()["Fundstelle"] = Fundstelle
globals()["Ressort"] = Ressort
globals()["Urheber"] = Urheber
globals()["Vorgangsbezug"] = Vorgangsbezug
from deutschland.dip_bundestag.model.drucksache import Drucksache


class TestDrucksache(unittest.TestCase):
    """Drucksache unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDrucksache(self):
        """Test Drucksache"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Drucksache()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()