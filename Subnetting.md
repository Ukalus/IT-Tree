
#### Einfaches Subnetting (Gleichgroße Subnetze)

Aufgabe: 
Teile folgendes Netz in 4 Gleichgroße Netze auf. Der Hostanteil soll
so klein wie möglich sein. 

Gegebenes Netz: 196.178.40.0 / 23 

Netzbereiche:

Technik = 50 hosts
Software = 50 hosts
Marketing = 20 hosts 
Kunden = 100 hosts 

Lösungsweg:

Das größte Netz braucht 100 hosts also gehen wir davon aus.
Wir brauchen 4 Subnetze mit jeweils 100 hosts. für 4 Subnetze
brauchen wir 2² also 4 bits. für 100 Hosts brauchen wir 2⁷ also 7 bits.

Wir erweitern also die Subnetzmaske auf /25 und haben dann noch
genau 7 bits übrig für den Host anteil.

Lösung:

1. Teilnetz

Netzadresse = 196.178.40.0 / 25
Erster Client = 196.178.40.1 / 25
Letzter Client = 196.178.40.126 / 25
Broadcast = 196.178.40.127 / 25

2. Teilnetz

Netzadresse = 196.178.40.128 / 25
Erster Client = 196.178.40.129 / 25
Letzer Client = 196.178.40.254 / 25
Broadcast = 196.178.40.255 / 25

3. Teilnetz

Netzadresse = 196.178.41.0 / 25
Erster Client = 196.178.41.1 / 25
Letzer Client =  196.178.41.126 / 25
Broadcast = 196.178.41.127 / 25 

4. Teilnetz 

Netzadresse = 196.178.41.128 / 25
Erster Client = 196.178.41.129 / 25 
Letzer Client = 196.178.41.254 / 25 
Letzer Client = 196.178.41.255 / 25




