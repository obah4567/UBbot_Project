import xml.etree.ElementTree as ET
import csv

tree = ET.parse("info.xml")
root = tree.getroot()

# open a file for writing
with open('Noms_responsable.csv', mode='w', encoding='utf-16') as Responsable_file:
    info_writer = csv.writer(Responsable_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for book in root.getchildren():
        for nom in book.getchildren():
            p = []
            chaine = ""
            for prof in nom.getchildren():
                if prof.text: # Si la balise "prof" est pas vide
                    if len(p) == 0: # Si la liste est pas vide
                        p.append('Responsable')
                    if (prof.tag == "{http://cdm-fr.fr/2012/CDM}given" or prof.tag == "{http://cdm-fr.fr/2012/CDM}family" or prof.tag == "{http://cdm-fr.fr/2012/CDM}email"):
                        if len(prof.text) < 40 and len(prof.text) > 1 : # On ajoute l'élément si les deux conditions sont respectées
                            if len(p) == 2: # Si la taille de la liste est égal à 2
                                chaine = p[1] + " " + prof.text #+ "," + "   Email: "  + p[1] + "." +prof.text + "@u-bordeaux.fr"
                                p[1] = chaine
                            else:   # Dans tout autre cas
                                p.append(prof.text)
                            print(" Le nom des profs => " + prof.text)
            if len(p) == 2: #Si la taille de la liste est égal à 2 on procède à l'ajout dans le fichier xml
                info_writer.writerow(p)
