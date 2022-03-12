# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.aktivitaet_api import AktivitaetApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.dip_bundestag.api.aktivitaet_api import AktivitaetApi
from deutschland.dip_bundestag.api.drucksache_api import DrucksacheApi
from deutschland.dip_bundestag.api.person_api import PersonApi
from deutschland.dip_bundestag.api.plenarprotokoll_api import PlenarprotokollApi
from deutschland.dip_bundestag.api.vorgang_api import VorgangApi
from deutschland.dip_bundestag.api.vorgangsposition_api import VorgangspositionApi
