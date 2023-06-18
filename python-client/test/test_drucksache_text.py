"""
    Deutscher Bundestag - DIP

    API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

    The version of the OpenAPI document: 1.2
    Contact: parlamentsdokumentation@bundestag.de
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.dip_bundestag.model.dokument_text_base import DokumentTextBase
from deutschland.dip_bundestag.model.drucksache import Drucksache
from deutschland.dip_bundestag.model.drucksache_autoren_anzeige_inner import (
    DrucksacheAutorenAnzeigeInner,
)
from deutschland.dip_bundestag.model.fundstelle import Fundstelle
from deutschland.dip_bundestag.model.ressort import Ressort
from deutschland.dip_bundestag.model.urheber import Urheber
from deutschland.dip_bundestag.model.vorgangsbezug import Vorgangsbezug

from deutschland import dip_bundestag

globals()["DokumentTextBase"] = DokumentTextBase
globals()["Drucksache"] = Drucksache
globals()["DrucksacheAutorenAnzeigeInner"] = DrucksacheAutorenAnzeigeInner
globals()["Fundstelle"] = Fundstelle
globals()["Ressort"] = Ressort
globals()["Urheber"] = Urheber
globals()["Vorgangsbezug"] = Vorgangsbezug
from deutschland.dip_bundestag.model.drucksache_text import DrucksacheText


class TestDrucksacheText(unittest.TestCase):
    """DrucksacheText unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDrucksacheText(self):
        """Test DrucksacheText"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DrucksacheText()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()