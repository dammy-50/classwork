# creating data types
x = 25
y = 15
z =  5
address = "296 adesida road"
# run variables
print ("hello world")
print (type(x))
print (type(y))
print (type(z))
print ("address")

# area of a triangle
base = 25
height =30
half=0.5

areatriangle = half * base * height
print (areatriangle)

# simple interest
principal=50
rate=20/100
time=10
simpleinterest = principal*rate*time
print(simpleinterest)

# height of a cuboid
length=325
breadth=50
volume=1360
h=volume/(length*breadth)
print(h)


# creating days and time
# welcome to my day and time calculating machine
x=12
print(x)
day=365*12
print(day)
y=5
print("numbers of years =",y,"years")
days=(day*y)
print("numbers of days= ",days,"days")
months=12*12*y
print("numbers of months=",months,"months")
minutes=60*24*days
print("numbers of minutes=",minutes,"months")
seconds=60*60*24*days
print("numbers of seconds=",seconds,"seconds")

#my time and date calculating machine
age=int(input("how old are you?"))
print(age)
Days=age*365
print("you have spent a total of",Days,"days on earth")
Months=age*12
print("you have spent a total of",Months,"months on earth")
Minutes=Days*24*60
print("you have spent a total of",Minutes,"minutes on earth")
Seconds=Minutes*60
print("you have spent a total of",Seconds,"seconds on earth")
#in the next 5years
AGE=age+5
print("in the next 5years,you will be",AGE,"years old")
DAYZ=Days*5
print("in the next 5years,you would have spent",DAYZ,"days on earth")
MONTHS=Months*5
print("in the next 5years,you would have spent",MONTHS,"months on earth")
MINUTES=Minutes*5
print("in the next 5years,you would have spent",MINUTES,"minutes on earth")
SECONDS=Seconds*5
print("in the next 5years,you would have spent",SECONDS,"seconds on earth")

#program to convert temperature from celsius to fahrenheit
x=int(input("enter the temperature in celsius:"))
x=round(x*(9/5)+32)
print(str(x)+'f')




# calculating area of a circle and radius of a circle

x=22/7
pi=float(x)


# hi,welcome to my radius of a circle calculator
print(" what is the radius of the circle","?")
print("enter the radius of the circle")
radius=int(input())
expR=radius**2
area=pi*expR
print("the area of a circle =answer",area)
































