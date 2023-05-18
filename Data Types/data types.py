#data types

#--integer are whole numbers--
num = 45

#--float are numbers with decimals --
nums = 2.232

#--strings a string of characters--
name = "Toby"

#--string concatenation--
#add string to string to create new string 
print("Hello " + name)

#--escaping a string--
#because the double quotes is special it denotes a string if you want to use it in a string you need to escape it with a "\"
speech = "Lauren said: \"Hi\""
print(speech)

#--F-Strings--
#You can insert a variable into a string using f-string
day = 240
print(f"There are {day} in a year")

#--Converting Data Types --
#You can convert a variable from 1 data type to another 
n = 354
new_n = float(n)
print(new_n)

#--Checking Data Types --
#You can use the type() function to check what is the data type of a particular variable 
v = 2.35
print(type(v))
