# A daļa - Saraksti
print("----- A daļa - Saraksti ----")
numbers = [10, 15, 22, 33, 40]
print(f"Saraksts: {numbers}")

#Papildinam sarakstu ar skaitli 55
numbers.append(55)
print(f"Papildinats saraksts: {numbers}")

#Izdzēsīsim no saraksta pedējo skaitli:
numbers.pop()
print(f"Pēc skaitļa izdzēšanas saraksts ir: {numbers}")

#Aprēķinām vidējo vērtību
total_sum = 0 
n = 0

for num in numbers:
    total_sum += num
    n += 1

average = total_sum/n
print(f"Vidējā vērtība: {average}")

#Pielietojām filtru- izvēlkam tikai pāra skaitļus
even_numbers = []
for num in numbers:
    if num % 2 == 0:
       even_numbers.append(num)

print(f"Pāra skaitli sarakstā: {even_numbers}")

#Slices
print(f"3 pirmie skaitļi: {numbers[0:3]}")
print(f"2 Pēdējie skaitļi: {numbers[-2:]}")
print(f"Katrais otrais elements: {numbers[::2]}")


# B daļa — Vārdnīcas
print("----- B daļa — Vārdnīcas ----")

# 1. Izveido vārdnīcu ar studentiem
studenti = {"Anna": 8, "Jānis": 6, "Marta": 9, "Pauls": 7}

# 2. Pievieno jaunu studentu un maina atzīmi esošajam
studenti["Laura"] = 10 # Pievieno jaunu
studenti["Jānis"] = 8 # Maina esošo atzīmi

# 3. Iterē cauri vārdnīcai un izvada katru studentu
print("Studentu saraksts: ")
i = 1
for name, grade in studenti.items():
    print(f"{i}. Students: {name}, Atzīme: {grade}")
    i +=1

# 4. Atrod studentu ar visaugstāko atzīmi, izmantojot for ciklu
max_grade = -1
best_student = ""

for name, grade in studenti.items():
    if grade > max_grade:
        max_grade = grade
        best_student = name

print(f"Students ar visaugstāko atzīmi: {best_student} - {max_grade}")


# C daļa — Kombinācija
print("----- C daļa — Kombinācija ----")

# 1. Izveidojam sarakstu ar vārdnīcām
students = [
    {"name": "Anna", "grade": 85},
    {"name": "Māris", "grade": 72},
    {"name": "Laura", "grade": 92},
    {"name": "Jānis", "grade": 45},
    {"name": "Kate", "grade": 80},
    {"name": "Oskars", "grade": 78}
]

# 2. Filtrējam studentus, kuriem atzīme ir >= 80
# Izmantojam saraksta aptveri (list comprehension)
top_students = [s for s in students if s["grade"] >= 80]

# 3. Izmantojam enumerate() un f-string rezultātu izvadei
print("Studenti ar atzīmi 80 vai augstāk:")

for index, student in enumerate(top_students, start=1):
    print(f"{index}. {student['name']} - {student['grade']}")



