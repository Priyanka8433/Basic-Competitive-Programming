grade = float(input("Enter your percentage: "))

if  grade<=25 :
    grade = "D"
elif grade >=25 and grade<=45:
    grade = "C"
elif grade>= 45 and grade<=65:
    grade = "B"
elif grade >= 65 and grade<=85:
    grade = "A"
elif grade >=85:
    grade = "A+"
else:
    grade = "Invalid percentage!"                     


print("Your Grade is:", grade)

