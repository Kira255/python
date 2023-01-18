'''Напишите программу, удаляющую из текста все слова, содержащие ""абв"".'''

line = 'фысабв, свфсфабв: аолым'

while ',' in line or '.' in line or ';' in line:
    line = line.replace(',', '')
    line = line.replace('.', '')
    line = line.replace(';', '')

print(line)

arr = line.split()
print(arr)

arr2 = []
for word in arr:
    if 'абв' not in word:
        arr2.append(word)
print(arr2)
