# DIP Bundestag API 
Bundestag: Dokumentations- und Informationssystem für Parlamentsmaterialien


## Authentifizierung
Aktuell wird ein API-Key benötigt, der per Mail an infoline.id3@bundestag.de beantragt werden kann. Alternativ gibt es offenbar temporäre wechselnde öffentliche Keys 
(siehe https://dip.bundestag.de/%C3%BCber-dip/hilfe/api#content).

Folgender API-Key ist im Header der Anfrage zu inkludieren:

**Authorization:** ApiKey N64VhW8.yChkBUIJeosGojQ7CSR2xwLf3Qy7Apw464


Alternativ oder ergänzend kann der API-Key auch als GET-Parameter apikey inkludiert werden:

**apikey:** N64VhW8.yChkBUIJeosGojQ7CSR2xwLf3Qy7Apw464


## Aktivität

**URL:** https://search.dip.bundestag.de/api/v1/aktivitaet


Liste aller Aktivitäten.


## Aktivität-ID

**URL:** https://search.dip.bundestag.de/api/v1/aktivitaet/{id}


Metadaten zu einer Aktivität, mit dem Pfad-Parameter *id* (z.B. 908).


## Drucksache

**URL:** https://search.dip.bundestag.de/api/v1/drucksache


Liste aller Drucksachen.


##  Drucksache-ID

**URL:** https://search.dip.bundestag.de/api/v1/drucksache/{id}


Metadaten zu einer Drucksache, mit dem Pfad-Parameter *id* (z.B. 908).


## Drucksache-Text

**URL:** https://search.dip.bundestag.de/api/v1/drucksache-text


Liste aller Volltexte der Drucksachen.


##  Drucksache-Text-ID

**URL:** https://search.dip.bundestag.de/api/v1/drucksache-text/{id}


Liste aller Personenstammdaten.


##  Person

**URL:** https://search.dip.bundestag.de/api/v1/person


Liste aller Personenstammdaten.


##  Person-ID

**URL:** https://search.dip.bundestag.de/api/v1/person/{id}


Personenstammdaten, mit dem Pfad-Parameter *id* (z.B. 908).


##  Plenarprotokoll

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll


Liste aller Plenarprotokolle.


##  Plenarprotokoll-ID

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll/{id}


Metadaten zu Plenarprotokoll, mit dem Pfad-Parameter *id* (z.B. 908).


##  Plenarprotokoll-Text

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll-text


Liste aller Volltexte der Plenarprotokolle.


##  Plenarprotokoll-Text-ID

**URL:** https://search.dip.bundestag.de/api/v1/plenarprotokoll-text/{id}


Volltexte des Plenarprotokolls, mit dem Pfad-Parameter *id* (z.B. 908).


##  Vorgang

**URL:** https://search.dip.bundestag.de/api/v1/vorgang


Liste aller Vorgänge.


##  Vorgang

**URL:** https://search.dip.bundestag.de/api/v1/vorgang/{id}


Metadaten zu Vorgang, mit dem Pfad-Parameter *id* (z.B. 908).


## Beispiel:

```bash
dip=$(curl -m 60 -H "Authorization: ApiKey N64VhW8.yChkBUIJeosGojQ7CSR2xwLf3Qy7Apw464" \
'https://search.dip.bundestag.de/api/v1/aktivitaet')
```
