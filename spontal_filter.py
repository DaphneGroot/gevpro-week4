#!/usr/bin/env python
#Daphne Groot


import sys
import xml.etree.ElementTree as ET

def main(argv):
	""" Opent het bestand spontal.xml, controlleert of de gegevens correct zijn en schrijft de correcte gegevens naar een nieuw bestand """
	if len(argv) == 3:
		
		tree = ET.parse(argv[1])
		root = tree.getroot()
		
		#Haalt informatie op uit aangegeven velden
		for element in root.findall('POINT'):
			BOTTOM_HZ = element.find('BOTTOM_HZ').text
			TOP_HZ = element.find('TOP_HZ').text
			F0_START = element.find('F0_START').text
			F0_END = element.find('F0_END').text
			
			
			#Zet de string-waarden om in getallen
			BOTTOM_HZ = int(BOTTOM_HZ)
			TOP_HZ = int(TOP_HZ)
			F0_START = float(F0_START)
			F0_END = float(F0_END)
			
			
			#Checkt of de F0-waarden binnen d e HZ-waarden vallen
			if F0_START < BOTTOM_HZ or F0_START > TOP_HZ or F0_END < BOTTOM_HZ or F0_END > TOP_HZ:
				root.remove(element)
				
				
		#Schrijft uitkomst naar het nieuwe bestand
		tree.write(argv[2])
		

	else:
		print("Gebruik spontal_filter.py Argument1 Argument2, waarbij de Argument1 het bestand spontal.xml en Argument2 de naam van het nieuwe bestand is.")
		
		
		
if __name__ == "__main__":
	main(sys.argv)
