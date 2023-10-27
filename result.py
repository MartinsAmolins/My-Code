import PyPDF2
import pathlib


file=input()
result=0

date=[]
price=float(0)
i=0
s=0
day=[]
a=0
datums=""

# this part read information from pdf file and place 
data=[]
# split pdf file in to two pages and extraxt page content to text variables
if file!="":       
    row=[]
    pdf_file=PyPDF2.PdfReader(open(file,"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]

    text1=page1.extract_text()
    text2=page2.extract_text()

    pos3 = text2.find("EUR")
    pos4 = text2.find("kWh ")

    Elek = text2[pos4+11:pos4+17].rstrip()
    daudz = text2[pos3+38:pos4].rstrip()
    kwh = text2[pos4+4:pos4+11].rstrip()

 # this part
    daudz=daudz.replace(',','.')
    daudz=daudz.replace(' ','')
    Elek=Elek.replace(',','.')
    Elek=Elek.replace('\nA','')

    if(file=="invoices/invoice1.pdf"):
        datums="2023-04-30 23:00:00"
        datums2="2023-03-31 23:00:00"
    elif(file=="invoices/invoice2.pdf"):
        datums="2023-05-31 23:00:00"
        datums2="2023-04-30 23:00:00"
    elif(file=="invoices/invoice3.pdf"):
        datums="2023-08-31 23:00:00"
        datums2="2023-07-31 23:00:00"

    with open("nordpool.csv","r") as f:
        next(f)
        for lines in f:
            row=lines.rstrip().split(",")
            data.append(row)

    for i in range(len(data)):
        if(data[i][0]==datums and s==0):
            s=s+1
            price=price+float(data[i][2])
            day.append(float(data[i][2]))
            continue
        if(s>0):
            price=price+float(data[i][2])
            day.append(float(data[i][2]))
        if(data[i][0]==datums2):
            break




    if(Elek!=0.0):
        a=len(day)
        kwh2=float()
        kwh1 = float((price/a))
        kwh1=kwh1*float(daudz)
        if(kwh1>float(Elek)):
            kwh2=float(kwh1)-float(Elek)
        else:
            kwh2=float(Elek)-float(kwh1)
        print(kwh2)
if(file==""):
    print("")
