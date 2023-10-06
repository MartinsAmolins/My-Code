import pandas
get_info=input()  #input information from terminal

fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA") # if no pages are specified, then the last one saved is open
info_list = fails.values.tolist()

geo_kods=[]
geo_count=0

for line in info_list:
    for i in range(len(line)):
        if(line[i]==str(get_info)):
            geo_kods=line[i-1]

with open("data.csv") as k:
    next(k)
    for lines in k:
        row=lines.rstrip().split(",")
        for i in range(len(row)):
            if(row[i]==str(geo_kods)):
                geo_count+=int(row[i+2])
           
print(geo_count)