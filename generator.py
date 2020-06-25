import hashlib

def hash_gen(fname):
    with open(fname) as fin:
        for i in fin:
            yield hashlib.md5(i.encode()).digest()
            
for i in hash_gen('countries.json'):
    print(i)          