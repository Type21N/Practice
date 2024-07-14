name =(input("Enter Name : "))
male =(input("Enter male : "))

heihght =int(input("Enter Height : "))
weight =int(input("Enter weight : "))

heihght1 = heihght/100
total = weight/(heihght1*heihght1)

print("-----------------")
print(" RESULT yoUR BMI ")
print("-----------------")
print(name)
print(male)
print(heihght,"CM ")
print(weight,"KILO")
print('BMI:',"%.2f"%total)

if total >= 35:
    print("Ex OBESE")
elif total >=30:
    print("OBESE")
elif total >=25:
    print("OVERWEIGHT")
elif total >=18:
    print("NORMAL")
else:
    print("UNDEREIGHT")

