
f= open("D:\\document\\Data Science\\Python\\funny.txt","r")
f_out=open("D:\\document\\Data Science\\Python\\funny_wc.txt","w")

for line in f:
    token=str(len(line.split(" ")))+":"+line
    print(token)
    f_out.write(token)

f.close()
f_out.close()