
import os
import requests
import json
import win32com.client as win32
import urllib.parse

# Mining and storing the Data I need in json Data File

main_api = 'https://api.github.com/search/repositories?q'
while True:
    address = input('Address: ')

    if address == 'quit' or address == 'q':
        break
    my_url = main_api + urllib.parse.urlencode({'': address})
    print(my_url)
    uData = requests.get(my_url).json()
    print(type(uData))

    with open('Data.json', 'w') as json_file:
        json.dump(uData, json_file)

# Locating and opening the json Data File

json_data = json.loads(open('Data.json', encoding="utf-8").read())

# Examing the data and flatten the records into a 2D layout

rows = []
totCount = json_data['total_count']
print('Total Count:', totCount)

for record in json_data['items']:
    tc = record['id']
    private = record['private']
    name = record['name']
    fullName = record['full_name']
    html_url = record['html_url']
    lang = record['language']
    fork = record['forks']
    size = record['size']
    desc = record['description']

    rows.append([tc, private, name, fullName, html_url, lang, fork, size, desc])

# Inserting Records to the Excel SpreadSheet

ExcelApp = win32.Dispatch('Excel.Application')
ExcelApp.visible = True

wb = ExcelApp.Workbooks.Add()
ws = wb.Worksheets(1)

# Inserting header Label
header_labels = ('ID', 'PRIVATE', 'NAME', 'FULL NAME', 'HTML URL', 'LANGUAGE', 'FORK', 'SIZE', 'DESCRIPTION')

for index, val in enumerate(header_labels):
    ws.cells(1, index + 1).value = val

# Inserting Records into the Excel File
row_tracker = 2
column_size = len(header_labels)

for row in rows:
    ws.Range(
        ws.cells(row_tracker, 1),
        ws.cells(row_tracker, column_size)
    ).value = row
    row_tracker += 1

wb.SaveAs(os.path.join(os.getcwd(), 'json output.xlsx'), 51)
wb.Close()
ExcelApp.quit()
ExcelApp = None
