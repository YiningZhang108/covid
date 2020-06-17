fileobj = open("06-15-2020.csv", "r") # r,w or a are the options stands for read, write and append
#this will skip over the first line of the data
delfirst = fileobj.readline()
datalist = fileobj.readlines()
fileobj.close()
#print(datalist)

conflist = []

for country in datalist:
    #print(country)
    templist =  country.split(",")
    pname = templist [2]#gets the item from templist by index number (index numbers start at 0)
    cname = templist [3]
    lat = templist [5]
    lon = templist [6]
    conf = int(templist [7])
    #print (pname + cname + lat + lon + conf)
    conflist.append({"pname":pname,"cname":cname,"lat":lat, "lon":lon,"conf":conf})#this is called a dictionary

#print(conflist)
conflist.sort(key=lambda s: s['conf'], reverse=True)#sorts based on the number of confirmed
#reverse=True makes it go from desending order
fileout = open("06-15-2020.js","w") #opens new file called test.js
fileout.write("data = " + str(conflist)) # changes conflist to string
fileout.close()#if doesn't close nothing will be written to disc
