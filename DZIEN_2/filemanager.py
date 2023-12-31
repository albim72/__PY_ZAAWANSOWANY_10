class FileManager(object):
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with FileManager('test.txt','w','utf-8') as f:
    f.write('to jest pierwsza linia tekstu\n')

print(f.closed)

with open('abc.txt','w',encoding='utf-8') as g:
    g.write('drugi plik za danymi \n')
print(g.closed)

with FileManager('test.txt','r','utf-8') as f:
    print(f.read())


