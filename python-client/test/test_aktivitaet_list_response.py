"""
Deutscher Bundestag - DIP

API des Dokumentations- und Informationssystems für Parlamentsmaterialien  # noqa: E501

The version of the OpenAPI document: 1.2
Contact: parlamentsdokumentation@bundestag.de
Generated by: https://openapi-generator.tech
"""

import sys
import unittest

from deutschland.dip_bundestag.model.aktivitaet import Aktivitaet
from deutschland.dip_bundestag.model.aktivitaet_list_response_all_of import (
    AktivitaetListResponseAllOf,
)
from deutschland.dip_bundestag.model.list_response_base import ListResponseBase

from deutschland import dip_bundestag

globals()["Aktivitaet"] = Aktivitaet
globals()["AktivitaetListResponseAllOf"] = AktivitaetListResponseAllOf
globals()["ListResponseBase"] = ListResponseBase
from deutschland.dip_bundestag.model.aktivitaet_list_response import (
    AktivitaetListResponse,
)


class TestAktivitaetListResponse(unittest.TestCase):
    """AktivitaetListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAktivitaetListResponse(self):
        """Test AktivitaetListResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AktivitaetListResponse()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
