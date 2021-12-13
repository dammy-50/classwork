import maths as mts

# program to find numbers divisible by 7 and multiple of 5,between 1500 and 2700
print("hello guys,my calculator can find numbers divisible by 7 and mutiples of 5,","you can try it out!")
if (num>=1500or num<=2700):
    print("number is valid")
else:
    print("number is invalid")
num=int(input())
if (num//7)==0:
    print("it is divisible by seven")
else:
    print("it is not divisible by 7")
if (num%5)==0:
    print("the number is a multiple of five")
else:
    print("the number is not a multiple of five")
