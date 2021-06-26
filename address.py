

book={}

book['tom']={'name':'tom',
             'address':'21 steet road',
             'phone':827382738}

book['bob']={'name':'bob',
             'address':'22 steet road',
             'phone':827562738}

import json
s=json.dumps(book)
with open("D:\\document\\book.txt","w") as f:
    f.write(s)
    