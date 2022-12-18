'''Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''


xyz = ["X", "Y", "Z"]
a = []
for i in range(3):
    a.append(input(f"Введите значение {xyz[i]}: "))
x = a
left = not (x[0] or x[1] or x[2])
right = not x[0] and not x[1] and not x[2]
result = left == right

if result == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
