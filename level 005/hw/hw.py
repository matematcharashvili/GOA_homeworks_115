#გამარჯობა

# დავალება [1]

name = input("Enter Your Name: ")
surname = input("Enter Your Surname:")
age = input("Enter Your Age")

print("My Name Is: ", name)
print("My Surname Is: ", surname)
print("My Age is :", age)
# დავალება [2]

price1 = int(input("Enter Product Price "))

price2 = int(input("Enter Product Price "))

price3 = int(input("Enter Product Price "))

total = price1 + price2 + price3

print(total)

# დავალება [3]

age = int(input("Enter Your Age: "))
years = int(input("Enter Number Of Years: "))

total = age + years

print(f"int {years} years you will be {total} years old")


# დავალება [4]

ganvlili_mandzili = int(input("Sheikvanet Gavlili Mandzili: "))

daxarjuli_dro = int(input("SheikvaneT Daxarjuli Dro: "))

print(ganvlili_mandzili / daxarjuli_dro)

# დავალება [5]

#100კმზე მოიხმარს 8 ლიტრ საწვავს.

Gasavleli_Mandzili = int(input("მიუთითეთ გასავლელი მანძილი: "))

# ფორმულა არის (მანძილი * 8 ) / 100

print((Gasavleli_Mandzili * 8 ) /100 )

# დავალება [6]

Distance = int(input("Enter Distance To KM: "))
Sawvavis_Xarji = int(input("Miutitet Sawvavis Xarji: "))
Sawvavis_Fasi = float(input("Miutitet Sawvavis Fasi: "))

Sawvavi = (Distance * Sawvavis_Xarji ) / 100

Girebuleba = Sawvavi * Sawvavis_Fasi

print("დასჭირდა ამდენი ლიტრი საწვავი: ", Sawvavi)
print("საწვავი დაუჯდება: ", Girebuleba)

# დავალება [7]

sallary = int(input("მიუთითეთ თქვენი ანაზღაურება საათში: "))
time = int(input("მიუთითეთ თქვენი ნამუშევარი დრო: "))

oneweek = sallary * time
print(oneweek)


# დავალება [8]

money = int(input("Enter Money in GEL: "))
people = int(input("Enter Number Of People: "))

# გავიგოთ რამდენი სრული ლარი შეხვდება თითოეულ ადამიანს

print("Person Gets: ", money // people)
print("Remeaning Money: ",  money % people)

# დავალება [9]
full_price = int(input("Enter product price: "))
fasdaklebis_procenti = int(input("Enter discount percentage: "))

discount = full_price * fasdaklebis_procenti / 100
lastprice = fullprice - discount

print(lastprice)


# დავალება [10]

pages = int(input("Enter your book pages: "))

dsss = int(input("Write down how many pages you read per day: "))


waikitxavs = pages / dsss

print("წაიკითხავს", waikitxavs , "დღეში")

# მადლობა ნახვამდის.