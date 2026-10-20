# მოგესალმებით

# დავალება [1]


#ჩვენ level 4 გაკვეთილზე ვისწავლეთ დანაშთვა რომელიც გამოიხატება ასე მაგალითად 150%2 ეს ნიშნავს რომ 150 გაყოფს 2 ზე და ნაშთი რამდენია გამოგიტანს მას output ში.


#ასევე ჩვენ გავეცანით ახარისხებას,მაგალითად 10**5 ნიშნავს 10 ხარისხად 5-ს
print(10**5)

print(150%2)

#ჩვენ ასევე ვისწავლეთ მთელი გაყოფა ანუ 31 რომ გავყოთ 2 ზე // გაყოფით გაყოფს პითონი და output ში გამოიტანს პასუხს მთელ რიცხვს .მაგალითად 31რომ გავყოთ 2 გაყოფით 2 ზე 
#იქნება 15 და ნაშთს არგამოიტანს

print(31//2)


# დავალება[2]

num1 = int(input("ჩაწერეთ ნებისმიერი ციფრი: "))

num2 = int(input("ჩაწერეთ მეორე ნებისმიერი ციფრი: "))

square1 = int(num1 ** 3)
square2 = int(num2 ** 3)

cube1 = int(num1 ** 2)
cube2 = int(num2 ** 2)

print(square1, square2, cube1, cube2)

# დავალება [3]

n1 = int(input("შეიყვანეთ ნებისმიერი ციფრი: "))
n2 = int(input("შეიყვანეთ ნებისმიერი მეორე ციფრი ციფრი: "))

print(n1 + n2,   n1 * n2,   n1 / n2,   n1 - n2,   n1 // n2,   n1 ** n2,    n1%n2)

# დავალება [4]


candies = int(input("Enter Candies Amount"))

boxes =  candies // 12

remaining = candies % 12
print("full boxes: ", boxes)
print("remaining candies: ", remaining)

# ჩვენი ბრძანება candies // 12 გვეუბნება თუ რამდენი ყუთი გაივსება მთლიანად,ხოლო candies % 12 გვეუბნება რამდენი კამფეტი დარჩება.


# დავალება [5]

minutes = int(input("Enter Minutes: "))

full_hours = minutes // 60

remaining_minutes = minutes % 60

print("სრული დრო = ",full_hours)

print("დარჩენილი წუთები = ",remaining_minutes)

