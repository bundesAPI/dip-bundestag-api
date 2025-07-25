"""
Deutscher Bundestag - DIP

API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

The version of the OpenAPI document: 1.2
Contact: parlamentsdokumentation@bundestag.de
Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.dip_bundestag.model.deskriptor import Deskriptor
from deutschland.dip_bundestag.model.fundstelle import Fundstelle
from deutschland.dip_bundestag.model.vorgangspositionbezug import Vorgangspositionbezug

from deutschland import dip_bundestag

globals()["Deskriptor"] = Deskriptor
globals()["Fundstelle"] = Fundstelle
globals()["Vorgangspositionbezug"] = Vorgangspositionbezug
from deutschland.dip_bundestag.model.aktivitaet import Aktivitaet


class TestAktivitaet(unittest.TestCase):
    """Aktivitaet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAktivitaet(self):
        """Test Aktivitaet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Aktivitaet()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
