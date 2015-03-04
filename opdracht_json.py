#!/usr/bin/env python
#Daphne Groot

from collections import namedtuple
import json

def main():
	""" Opend het bestand blood-die.json en zoekt de talen waarbij het woord voor 'bloed'
	overeenkomt met het woord voor 'sterevn' """
	
	lijstOvereenkomsten = []
	LIJST = namedtuple('LIJST','taalNaam , classificatie')
	
	
	#bestand wordt geopend
	with open('blood-die.json') as json_bestand:
		bestand = json.load(json_bestand)
		json_bestand.close()
		
		
	#Voor iedere regel in het bestand wordt gekeken of de gegevens overeenkomen en dan worden ze 
	#toegevoegd aan een nieuwe lijst
	for regel in bestand:
		lijstBloed = regel[2].split()
		lijstSterven = regel[3].split()
		
		
		gegevens = LIJST(regel[0], regel[1])
		[lijstOvereenkomsten.append(gegevens) for item in lijstBloed if item in lijstSterven]
		
		
	#Uitkomsten worden onder elkaar geprint
	[print(item) for item in lijstOvereenkomsten]


if __name__ == "__main__":
	main()
