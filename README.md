Taakbeheersysteem

Dit taakbeheersysteem is dient om je te helpen bij het organiseren van taken.
Door het bijhouden van taken en personen kan je ook een taak koppelen aan een persoon zodat je weet voor wie de taak bedoeldt is.

Start:

Om het programma te kunnen gebruiken moet je eerst een paar stappen overlopen om het programma geactiveerd te  krijgen.
Deze worden hieronder uitgelegd voor een linux machine.

Stap 1.

	Het clonen van de repository naar je fysieke machine.
	git clone https://github.com/SamynRhune/PiP-project.git
Stap 2.

	Om ervoor te zorgen dat je virtuele omgeving werkt.
	sudo apt-get install python3-venv
Stap 3.

	Deze stap zorgt ervoor dat je virtuele omgeving aangemaakt wordt.
	python3 -m venv .venv
Stap 4.

	Activeren van de virtuel omgeving.
	source .venv/bin/activate
Stap 5.

	Navigeren naar het project en requirements installeren.
	cd PiP-project
	pip install -r requirements.txt
Stap 6.

	Ervoor zorgen dat alle files uitvoerbaar zijn.
	chmod +x Scripts/*
Stap 7.

	Het opstarten van het programma
	python3 Scripts/main.py

De database wordt vanzelf aangemaakt als er nog geen database bestaat in de directory Databases.

Het programma maakt gebruik van de commandline om aanpassingen aan te brengen.

Alle commandos vindt je door het help commando in te geven. De meeste commando's zijn vanzelfsprekend zoals ADD en UPDATE.
Het EXPORT commando heeft wel nog wat verduidelijking nodig maar deze exporteert je database naar een excelbestand.
Je kan taken toevoegen updaten verwijderen net als personen. 

Je kunt ook meteen de functies na elkaar zetten zodat het sneller gaat bijvoorbeeld ADD PERSON ipv deze allebei apart te typen.

Ook kan je de database
omzetten naar een excelfile zodat je het zonder het programma open te hebben staan
toch makkelijk de data kan analyseren.