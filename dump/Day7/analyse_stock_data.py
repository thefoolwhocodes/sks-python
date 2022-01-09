import statistics

print("Example1: Average price for a hardcoded year")
#abs_file_path = input("Please enter file name!")
abs_file_path="/home/santosh/Python/Day7/DataFiles/BSE-BOM504067.csv"
with open(abs_file_path,"r") as fh:
    close_price=list()
    for line in fh:
        data=line.split(",")
        year=data[0].split("-")[0]
        if year=="2019":
            close_price.append(float(data[4]))
    print("Year: 2019  Average:",sum(close_price)/len(close_price))

print("\nExample2: Average price for all the years")
with open(abs_file_path,"r") as fh:
    #Dict of year vs list of day closing 
    year_dict=dict()
    for line in fh:
        data=line.split(",")
        if data[0] == 'Date':
            continue
        year=data[0].split("-")[0]
        if year in year_dict:
            year_dict[year].append(float(data[4]))
        else:
            year_dict[year]=list()
            year_dict[year].append(float(data[4]))

    for year in year_dict:
        print("Year:",year," Average:",sum(year_dict[year])/len(year_dict[year]))

print("\nExample3: Find out standard deviation for every year")
with open(abs_file_path,"r") as fh:
    #Dict of year vs list of day closing 
    year_dict=dict()
    for line in fh:
        data=line.split(",")
        if data[0] == 'Date':
            continue
        year=data[0].split("-")[0]
        if year in year_dict:
            year_dict[year].append(float(data[4]))
        else:
            year_dict[year]=list()
            year_dict[year].append(float(data[4]))

    for year in year_dict:
        print("Year:",year," Average:",sum(year_dict[year])/len(year_dict[year])," standard deviation:", statistics.stdev(year_dict[year]))


print("\nExample4: Find out standard deviation for every year and every quarter(Q1-Q4)")
with open(abs_file_path,"r") as fh:
    year_dict_with_quarter=dict()
    q1=range(4,7)
    q2=range(7,10)
    q3=range(10,13)
    q4=range(1,4)
    quarter=""

    for line in fh:
        data=line.split(",")
        if data[0]=="Date":
            continue
        year=data[0].split("-")[0]
        month=int(data[0].split("-")[1])
        if month in q1:
            quarter="q1"
        elif month in q2:
            quarter="q2"
        elif month in q3:
            quarter="q3"
        elif month in q4:
            quarter="q4"
        key=year+"-"+quarter
        close=float(data[4])
        if key in year_dict_with_quarter:
            year_dict_with_quarter[key].append(close)
        else:
            year_dict_with_quarter[key]=list()
            year_dict_with_quarter[key].append(close)

    for key in year_dict_with_quarter:
        print("Year-Quarter:", key," Average: ", sum(year_dict_with_quarter[key])/len(year_dict_with_quarter[key])," standard deviation:", statistics.stdev(year_dict_with_quarter[key]))
