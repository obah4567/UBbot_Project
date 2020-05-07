import xml.etree.ElementTree as ET
import csv

tree = ET.parse("biologie.xml")
root = tree.getroot()

# open a file for writing
with open('matiere.csv', mode='w', encoding='utf-8') as Responsable_file:
    info_writer = csv.writer(Responsable_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


#Ici, uniquement les matiéres
    compteur = 0
    for book in root.getchildren():
        p = []
        chaine = ""
        for coursNom in book.getchildren():
            if len(p) == 0: # Si la liste est pas vide
                p.append('Matière')

            if coursNom.text and (coursNom.tag == "{http://cdm-fr.fr/2012/CDM}courseName"  or coursNom.tag == "{http://cdm-fr.fr/2012/CDM}courseID"):
                compteur = compteur +1

                if len(p) == 2:
                    chaine = coursNom.text
                    p[1] = chaine
                else :
                    p.append(coursNom.text)
                print(" Matière => " + coursNom.text)
                print()
        if len(p) == 2:
            info_writer.writerow(p)
