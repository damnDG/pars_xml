import xml.etree.ElementTree as ET
import csv

def record_file(name_file, tree):
    all_data = []
    data_tags = [i for i in input().split()]  # первым вводите id
    with open(name_file, 'w', newline='', encoding='utf - 8 - sig') as f:
        writer = csv.writer(f)
        writer.writerow(data_tags)  
        for elem in tree.iter():
            if elem.tag == 'offer':
                all_data.append(elem.get('id'))
                for i in range(1, len(data_tags)):
                    all_data.append(elem.findtext(data_tags[i]))
                all_data = ['Not value' if i is None else i for i in all_data]
                writer.writerow(all_data)
                all_data.clear()

    print(1)
    
    
name_xml = 'axolotl.DBS.xml'  # можно на инпут заменить

try:
    tree = ET.parse(name_xml)
except FileNotFoundError:
    name_xml = input('Enter correct xml_name: ')

name_file = 'result.csv'
record_file(name_file, tree)