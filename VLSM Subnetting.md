
VLSM (Variable Length Subnet Masking) wird benutzt um möglichst kleine Subnetze zu bilden. Anders als bei normalem Subnetting ist der Hostteil nicht bei jedem Subnet gleich, sondern immer nur genau so groß wie er sein muss.

Gegebenes Netz für die Firma:

- 192.167.128.0 / 21

- 255.255.11111000.00000000

Abteilungen der Firma: 

- Technik = 200 hosts
- Software = 100 hosts
- Marketing = 50 hosts

Lösungsweg: 

Als erstes finden bestimmen sortieren wir die Bereiche nach ihrer größe und fangen mit dem Größten bereich an. Der Technik bereich benötigt 200 hosts. Wir bestimmen nun wie viele bits für diesen Bereich. 200 hosts + 2 (Netz und Broadcast-Adresse).

2⁸ (256 Adressen) ist am nächsten dran also brauchen wir 8 bits für das erste Sub-netz.
Wir erweitern also unsere Subnetzmaske auf /24 (32 - 8 = 24). 

Änderung der Subnetzmaske:

In Dezimal

	255.255.248.0
	255.255.255.0

In Binär

	1111 1111.1111 1111.1111 1000.0000 0000
	1111 1111.1111 1111.1111 1111.0000 0000




