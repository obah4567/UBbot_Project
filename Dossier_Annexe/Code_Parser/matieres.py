import xml.etree.ElementTree as ET
import csv

tree = ET.parse("biologie.xml")
root = tree.getroot()

# open a file for writing
with open('parcours.csv', mode='w', encoding='utf-16') as Responsable_file:
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
                print(" Les cours => " + coursNom.text)
                print()
        if len(p) == 2:
            info_writer.writerow(p)
    #print(compteur)


#"Ici, pour afficher le code des UE et les matières"
##    compteur = 0
##    for book in root.getchildren():
##        p = []
##        p2 = []
##        chaine = ""
##        chaine2 = ""
##        total = []
##        for coursNom in book.getchildren():
##            if len(p) and len(p2)== 0: 
##                p.append('Matiere')
##                p2.append('CodeUE')
##
##            if coursNom.text and (coursNom.tag == "{http://cdm-fr.fr/2012/CDM}courseName" or coursNom.tag == "{http://cdm-fr.fr/2012/CDM}courseID"):
##                compteur = compteur +1
##
##                if len(p) and len(p2)== 2:
##                    chaine = p[1] + " " + coursNom.text
##                    chaine2 = p2[2] + " " + coursNom.text
##                    p[1] = chaine
##                    p2[2] = chaine2
##                    total = p[2] + " " + p2[2]
##                else :
##                    p.append(coursNom.text)
##                    p2.append(coursNom.text)
##                print(" Les cours => " + coursNom.text)
##                print()
##        if len(p) == 2 and len(p2) == 2 :
##            info_writer.writerow(p)
##
##    print(compteur)   

