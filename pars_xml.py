import xml.etree.ElementTree as ET
import csv

def record_file(name_file, tree):
    all_data = []
    data_tags = [i for i in input().split()]  # первым вводите id
    with open(name_file, 'w', newline='', encoding='utf - 8 - sig') as f:
        writer = csv.writer(f) # создание объекта csv для записи
        writer.writerow(data_tags) # запись в первую строку наименований столбцов
        for elem in tree.iter(): # проходимся по объекту ET, итер для того, чтобы получить итератор
            if elem.tag == 'offer': # если тег оффер, то
                all_data.append(elem.get('id')) # добавляем сначала id, т.к. это атрибут другой синтаксис
                for i in range(1, len(data_tags)): # далее в цикле добавляем весь текст, заключенный в интересующие нас теги
                    all_data.append(elem.findtext(data_tags[i]))
                all_data = ['Not value' if i is None else i for i in all_data] # если тега нет, то он возвращает None, в excel будут просто пустые строки. Чтобы не путать с ошибкой какой-то заменяет None на 'Not value'
                writer.writerow(all_data) #добавление строки в результирующий файл
                all_data.clear() #очищение списка, чтобы добавлять построчно каждый раз

    print(1)
    
    
name_xml = 'axolotl.DBS.xml'  # можно на инпут заменить

try:
    tree = ET.parse(name_xml) # если не правильное имя xml-файла, или он в другой дирректории, то будет обработана ошибка, и предложен ввод с клавиатуры
except FileNotFoundError:
    name_xml = input('Enter correct xml_name: ')

name_file = 'result.csv'
record_file(name_file, tree)
