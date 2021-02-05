fn = r'test.xlsx'
f = open(fn, 'rb').read()

newfile = open('MK.py', 'w+')
newfile.write(f"""def MakeExFile():
    file = {f}
    
    
    new = open('file.xlsx', 'wb+')
    new.write(file)
    new.close()
    
MakeExFile()
""")
newfile.close()

import MK