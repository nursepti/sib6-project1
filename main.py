import json
from modules.book import Book
from modules.magazine import Magazine
from modules.cd import Cd
from modules.dvd import Dvd
from modules.catalog import Catalog

f = open("sib6-project1/file/catalog.json") 
data_json = json.load(f)

book = []
magazine = []

for item in data_json:
    if item['source'] == 'book':
        book.append(
            Book(
                title=item['title'],
                subject=item['subject'],
                upc = item['upc'],
                issbn = item['issbn'],
                authors = item['authors'],
                dds_number= item['dds_number'] 
            )
        )

    elif item['source'] == 'magazine':
        magazine.append(
            Magazine(
                title=item['title'],
                subject = item['subject'],
                upc = item['upc'],
                volume =item['volume'],
                issue = item['issue']
            )
        )


catalog_all = [book,magazine]
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

for index, result in enumerate(results):
    print(f'result ke-{index+1} | {result} ')