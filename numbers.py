# my machine accepts string from a user and calculates the number of digits and letters
print("Enter a string:")
string=input()
letternumbers,digitnumbers=0,0

for C in string:
    if (C>='a' and C<='z' ):
        letternumbers+=1
    if (C>='0' and C<='9'):
         digitnumbers+=1
print("Entered string:",string)
print("Total number of letters:",letternumbers)
print("Total number of digits:",digitnumbers)