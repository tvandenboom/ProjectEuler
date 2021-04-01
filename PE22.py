#Function outputting numerical value of a string:
def string_val(str):
    sum = 0
    for i in range(0,len(str)):
        sum += ord(str[i])-64
    return sum

#Create a list of names from the file
data = open("p022_names.txt","r")
file = data.read()
name_list = file.split(",")

#Trim the unnecessary quotation marks from the names in the list
for i in range(0,len(name_list)):
    name_list[i] = name_list[i][1:-1]

#Sort name_list alphabetically
name_list.sort()


#Compute sum of string_val*position
total = 0
for i in range(0,len(name_list)):
    total += (i+1)*string_val(name_list[i])

print(total)
