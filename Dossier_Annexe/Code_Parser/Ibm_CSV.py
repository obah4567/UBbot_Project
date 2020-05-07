import xml.etree.ElementTree as ET
import csv

tree = ET.parse("info.xml")
root = tree.getroot()

# open a file for writing

Resident_data = open('/tmp/ResidentData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Resident_data)
resident_head = []


for book in root.getchildren():
    for codeUE in book.getchildren():
        if codeUE.text and codeUE.tag == "{http://cdm-fr.fr/2012/CDM}programID" :
            print("Le code => " + codeUE.text)
            print()
                
##        for el in elem.getchildren():
##            if el.text and el.tag == "{http://cdm-fr.fr/2012/CDM-frSchema}text" :
##
##                #myfile.write(el.text.encode()+"\n".encode())
##                #myfile.write(el.text.encode())
##                print(" La formation => " + el.text)


    for nomCours in book.getchildren():
        if nomCours.text and nomCours.tag == "{http://cdm-fr.fr/2012/CDM}courseName" :
            print(" La formation => " + nomCours.text)
            print()
            #print("Le code est => " + elem.text + " et La formation => " + el.text)


    for nom in book.getchildren():
        for prof in nom.getchildren():
            if prof.text and prof.tag == "{http://cdm-fr.fr/2012/CDM}given":
                print(" Le nom des profs => " + prof.text)
                if prof.text and prof.tag == "{http://cdm-fr.fr/2012/CDM}family":
                    print(" Le nom des profs => " + prof.text)
                    print()



