# DIP Bundestag API 
Bundestag: Dokumentations- und Informationssystem für Parlamentsmaterialien


## How-To

### Authentifizierung
Zur Nutzung der API wird ein API-Schlüssel benötigt:

- Ein individueller Schlüssel kann per Mail an infoline.id3@bundestag.de beantragt werden
- Es steht ein temporärer, öffentlicher Schlüssel zur Verfügung ([Quelle](https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content)). Der aktuelle Schlüssel ist gültig bis Ende 05/2026: `OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw`

Der API-Schlüssel kann sowohl als HTTP-Header sowie als GET-Parameter eingesetzt werden:

- HTTP Header: `Authorization: ApiKey OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw`
- GET-Parameter: `?apikey=OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw`

### Nutzung

#### cURL
```bash
dip=$(curl -m 60 \
'https://search.dip.bundestag.de/api/v1/aktivitaet?apikey=OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw')
```

#### Python
Ein automatisch generierter Python-Client steht via [GitHub](https://github.com/bundesAPI/dip-bundestag-api/tree/main/python-client) und [PyPI](https://pypi.org/project/de-dip-bundestag/) zur Verfügung. Die Nutzungshinweise befinden sich im entsprechenden `README` auf GitHub.

## Endpoints
Die API stellt eine Dokumentation mit SwaggerUI bereit: 

### Aktivität

**URL:** https://search.dip.bundestag.de/api/v1/aktivitaet


Liste aller Aktivitäten.


### Aktivität-ID

**URL:** https://search.dip.bundestag.de/api/v1/aktivitaet/{id}


Metadaten zu einer Aktivität, mit dem Pfad-Parameter *id* (z.B. 908).


### Drucksache

**URL:** https://search.dip.bundestag.de/api/v1/drucksache


Liste aller Drucksachen.


###  Drucksache-ID

**URL:** https://search.dip.bundestag.de/api/v1/drucksache/{id}


Metadaten zu einer Drucksache, mit dem Pfad-Parameter *id* (z.B. 908).


### Drucksache-Text

**URL:** https://search.dip.bundestag.de/api/v1/drucksache-text


Liste aller Volltexte der Drucksachen.


###  Drucksache-Text-ID

**URL:** https://search.dip.bundestag.de/api/v1/drucksache-text/{id}


Liste aller Personenstammdaten.


###  Person

**URL:** https://search.dip.bundestag.de/api/v1/person


Liste aller Personenstammdaten.


###  Person-ID

**URL:** https://search.dip.bundestag.de/api/v1/person/{id}


Personenstammdaten, mit dem Pfad-Parameter *id* (z.B. 908).


###  Plenarprotokoll

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll


Liste aller Plenarprotokolle.


###  Plenarprotokoll-ID

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll/{id}


Metadaten zu Plenarprotokoll, mit dem Pfad-Parameter *id* (z.B. 908).


###  Plenarprotokoll-Text

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll-text


Liste aller Volltexte der Plenarprotokolle.


###  Plenarprotokoll-Text-ID

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll-text/{id}


Volltexte des Plenarprotokolls, mit dem Pfad-Parameter *id* (z.B. 908).


###  Vorgang

**URL:** https://search.dip.bundestag.de/api/v1/vorgang


Liste aller Vorgänge.


###  Vorgang

**URL:** https://search.dip.bundestag.de/api/v1/vorgang/{id}


Metadaten zu Vorgang, mit dem Pfad-Parameter *id* (z.B. 908).

