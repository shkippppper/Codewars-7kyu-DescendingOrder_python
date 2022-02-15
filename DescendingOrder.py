
newList = []
string = ""
x = "123412"
for y in range(len(x)):
    newList.append(x[y])
    newList.sort(reverse = True)
print(newList)  
for y in range(len(x)):
    string = string + newList[y]
print(string)




