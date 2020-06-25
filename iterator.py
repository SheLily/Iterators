import wikipedia
import json
from tqdm import tqdm

class countries(object):
    def __init__(self, fname):
        with open(fname) as fin:
            temp = json.load(fin)
        self.countries = [i['name']['common'] for i in temp]
        self.i = 0
        wikipedia.set_lang("en")
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >= len(self.countries):
            raise StopIteration()
        search = wikipedia.search(self.countries[self.i])
        page = wikipedia.page(search[0])
        self.i += 1
        return self.countries[self.i - 1], page.url
        
with open('result.txt', 'w') as fout:      
    for i in tqdm(countries('countries.json')):
        try:
            fout.write(f'Country: {i[0]} url: {i[1]}\n')
        except:
            pass
        
        