#My Salary and net bonus calculator
print("""Hello employees,it's end of the year again:,kindly put in your details to 
          know if you qualify for end of the year bonuses""")
print("Enter salary here:")
salary=int(input())
print("Enter yos")
yearofservice=int(input())
if yearofservice > 10:
    print("Your bonus is",(10/100)*salary,"Naira")
elif yearofservice>=6:
    print("Your bonus is",(8/100)*salary,"Naira")
elif yearofservice<=10:
    print("Your bonus is ",(8/100)*salary,"Naira")
elif yearofservice<6:
    print("Your bonus is",(5/100)*salary,"Naira")
else:
    print("We are so sorry, you do not have bonus this year")



#Welcome to my grade checker
print("Welcome Student,you can enter your marks here")
Marks=int(input())
if Marks<25:
   print("Your grade is F")
elif Marks>=25 and Marks<45:
   print("Your grade is E")
elif Marks>=45 and Marks<50:
   print("Your grade is D")
elif Marks>=50 and Marks<60:
   print("Your grade is C")
elif Marks>=60 and Marks<80:
   print("Your grade is D")
else:
   print("Your grade is A")

#Welcome to my number decider
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number"))
smallestnumber=0
if a<b and a<c:
    smallestnumber=a
if b<a and b<c:
    smallestnumber=b
if c<a and c<b:
    smallestnumber=c
else:
    print(smallestnumber,"is the smallest of the three numbers")

