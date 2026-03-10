print("day 2 and am here for it\nwill see what happens")
#actually its day 3 as i did not do it on actual day two

#will know about different data types current we know string  so will learn about integer  float boolean

#subscripting     pulling out a particular number from the string from the sequence
#its start with 0 the sequence i mean
#also we can select or count from back  with - numbers
#negative starts from -1 from back not 0as  -0 is i guess you know

print("kaisa hai bhai"[3])
print("halo"[-3])

# integer   are whole numbers here means numbers without decimals

print(121 + 212)   # so we can use number data when we don't use "" as these converts and read data as just data \

# float called as floating point numbers

print(7.7789)

#boolean

print(True)
print(False)

#----------------

len("halloo")
# we use typer(xyzdata type)   to know the data type in the (the)

print(type("kihalchal bravoo"))
print(type(12334445555))
print(type(8.989809))
print(type(True))

#type conversion or type casting
print(int("123") + int("321"))           #int converts data into integer
print(float("1.23") + float("3.21"))     #float converts data into decimal numbers or floats
print(str("abc") + str("def"))           #str coverts data to strings which normally "" does, I guess
print(bool(False) + bool(True))          #bool converts or read data to boolean  ture or false thingy


# problem one     have to solve this
# print("numbers of letters in your name: " + len(input("enter your name")))

#trying to solve if it's a real problem or at a level of a problem

a = input("enter your name")
print("numbers of letters in your name: " + str(len(a)))

#i think i have solved without even running once
#so its working we h=just have to make the other data type as string as we cant add up differnt data types

#------------------------------------

#mathematical operations

print(123 + 321)            # addition
print(200 - 400)            #substraction
print(9 * 999)              #multiplication
print(9 / 4)                #division but but it give the anser in float type measn in decimal even if there are non like 0
print(9 // 4)               #division but give answers in non decimal way but it removels the digits after decimal means if the answer is 4.5 it will give 4 as answer
print(9 // 4.5)             #but when you give it a decimal value then if will surely give result in decimal learn by muself now
print(123 ** 2)             #when want to have the result of powers like here its 123 the power of 2

#here two priorities are there like bodmas  or  she told  pemdaslr here lr is left to right
'''
()
**
* or /    here  the ones which is most left will executed first
+ or -    here  the ones which is most left will executed first same 
'''

#second problem or this is what she told it is
# print(3 * 3 + 3 / 3 - 3)  this results into 7
#the question is what will we change in this so the result will come as 3  will try

print(3 * 3 - 3 / 3 * 3 - 3)
#or
print(3 * 3 / 3 + 3 - (3 + 3) + 3)

# done i guess lets check
# yup its right got as 3

#------------------------

#round function used for rounding off value  digits after decimal

print(round(1 / 2 ** 1))         #  round off the decimals and shows with decimals
print(round(1 / 9 ** 1, 4))      #  round off teh decimals and shows answers till number of digits which is written after ,x

#assignment operator   or  number manipulation
#inshort manipulating value of a data but by keeping it previous data measn manupulating the data which it was holding previously
#we uses += -= *= /=
a = 123
print(a)
a -= 23
print(a)

#f-string    its helps to mix and add different data type
a = 1
b = 1.2
c = True

print(f"buddy now a is = {a}. your b is = {b} and your c is {c}")

#--------------------------------

# tip calculator plus bill spilter
# I am trying to build it myself just to try with looking at her doing jus by hearing what the project is here i go

print("let me help you")
u = input("Your total bill is : ₹")
v = input("how much percent of tip you want to give : %")
x = input("how many people are splitting the bill : ")

y = round(int(u) * (int(v) / 100 + 1), 2)
z = round(int(y) / int(x), 2)
print(f"you total bill is : ₹{y}")
print(f"your bill per person will be : ₹{z}")
print("thankyou for coming")

# acting here as i am working therein shop

# wow done bey me not even seen her video and also didnt took long like it was fast