# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from deutschland.dip_bundestag.api.aktivitten_api import AktivittenApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from deutschland.dip_bundestag.api.aktivitten_api import AktivittenApi
from deutschland.dip_bundestag.api.drucksachen_api import DrucksachenApi
from deutschland.dip_bundestag.api.personenstammdaten_api import PersonenstammdatenApi
from deutschland.dip_bundestag.api.plenarprotokolle_api import PlenarprotokolleApi
from deutschland.dip_bundestag.api.vorgangspositionen_api import VorgangspositionenApi
from deutschland.dip_bundestag.api.vorgnge_api import VorgngeApi
