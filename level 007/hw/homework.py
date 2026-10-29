# დავალება [1]
# input არის ბრძანება და ვიყენებთ როდესაც გვინდა რომ მომხმარებელს შემოვაყვანინოთ რაიმე სახის ინფორმაცია.

# დავალება [2]
# type casting არის ერთის მეორედ გადაქცევა მაგალითად სტრინგი რომ ინტეგერად გადავაქციოთ int(input("Enter Age"))

# დავალება [3]
# ჩვენ ვისწავლეთ str int float buliani

# დავალება[4]
# == ესარის გატოლება  >ესარის რო მეტია ეს კი ნაკლებია< >= მეტა ან ტოლია => ნაკლებია ან ტოლია != არაატოლი

# დავალება [5]

number = int(input("Enter Another Number: "))
print(number == 5)
print(number >= 5)
print(number <= 5)
print(number != 5)


# დავალება [6]

age = int(input("Enter Your Age"))

print(age >= 18)

# დავალება [7]

speed = int(input("Enter Vehicle Speed: "))
distance = int(input("Sheikvanet Gasavleli Mandzili: "))
time = int(input("Enter Time: "))


required_time = distance / speed



print(required_time, "hours")
print(required_time <= time)

# დავაკლება [8]

price1 = int(input("Enter Product Price: "))
price2 = int(input("Enter Product Price: "))
price3 = int(input("Enter Product Price: "))

money = int(input("Enter Your Money: "))

total = price1 + price2 + price3
print(total <= money)

# დავალება [9]

freesize = int(input("Enter Game Size To GB: "))
GB = int(input("Enter Your GB In PC: "))

print(GB <= freesize)

# დავალება [10]

math = int(input("Enter Your Sign: "))
history = int(input("Enter Your Sign: "))
art = int(input("Enter Your Sign: "))

average = (math + history + art) / 4

print(average > 5)

# დავალება [11]


# [1]
num1 = input("Enter first number: ")
num2 = int(input("Enter second number: "))

result = num1 + num2
print(result)

# აქ შეცდომა არის num1 არააქვს int ანუ სტრინგი ინტეგერად არარის გადაკეთებული მომხმარებელს ეუბვნება რიცხვის შემოყვანას და ინტეჯერად უნდა იყოს.

# [2]

num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 - "5" * num2
print(result)

# აქ შეცდომა ისარის რომ "5" მითუმეტეს სტრინგია და ინტეჯერის ფრჩხილები საერთოდ არაა საჭირო და არც ეგ 5 არაა საჭირო რადგან მომხმარებელს შემოვაყვანინეთ 2 რიცხვი

# [3]

hours = input("Enter hours worked: ")
rate = float(input("Enter hourly rate: "))
bonus = input("Enter bonus: ")

salary = hours * rate
total = salary + bonus
final_salary = total / "2"

print(final_salary)

# total / "2" აქ სტრინგის ფრჩხილები არუნდა და salary ში hours უნდა გავამრავლოთ bonus ზე  და hours bonus ცვლადს უნდა წინ int

price = float(input("Enter product price: "))
quantity = input("Enter quantity: ")
discount = float(input("Enter discount percentage: "))

subtotal = price + quantity
discount_amount = subtotal * discount
final_price = subtotal - "10"

print(int(final_price))

# quantity როწერია მანდ უნდა წინ int რადგან რაოდენობაა და ინტეგერად უნდა შემოიყვანოს მომხმარებელმა.ასევე final price ში "10"ეს სტრინგის ფრჩხილები უნდა ჩამოცილდეს


# [4]


num1 = int(input("Enter first number: "))
num2 = input("Enter second number: ")
num3 = float(input("Enter third number: "))

total = num1 + num2
average = total / num3
remainder = average % "2"
result = int(remainder + num1)

print(result)  

# "2" ეს შეცდომაა.ნუმ 2 ს უნდა int