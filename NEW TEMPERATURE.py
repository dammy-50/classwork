#python program to convert celsius to fahrenheit
#values
print("welcome to your celsius to fahrenheit calculator")
print("enter your name?")
name=input()
print("enter your temperature in celsius:")
Celsius=int(input())
#calculate fahrenheit
fahrenheit=(Celsius*1.8)+32
#Result
print(name,"your temperature in fahrenheit is",fahrenheit,"f")



#Compound interest machine
print("enter your name")
name=input()
p=10000
n=12
r=0.08
print("enter number of years:")
numberofyears=int(input())
t=numberofyears
#calculate compound interest
compoundinterest=p*((1+(r/n))**(n*t))
#result
print(name,"your compound interest =",compoundinterest,"naira")



#My python time converter
print("hello guys,welcome to my badass time converter")
print("enter your name")
name=input()
print("enter totalseconds")
totalseconds=int(input())
minutes=totalseconds//60
seconds=totalseconds%60
print(name,"the total timetaken is",minutes,"minutes", "and",seconds,"seconds")




