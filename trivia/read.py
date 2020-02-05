text_file = open('scenario.txt', 'r', encoding='utf-8')
text_file.close()

print('Читаю файл посимвольно')
text_file = open('scenario.txt', 'r')
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print('Читаю целиком')
file = open('scenario.txt', 'r', encoding='utf-8')
whole_thing = file.read()
print(whole_thing)
text_file.close()

print('читаю одну строку посимвольно')
text_file = open('scenario.txt', 'r', encoding='utf-8')
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print('Читаю одну строку целиком')
text_file = open('scenario.txt', 'r', encoding='utf-8')
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print('Читаю весь файл в список')
text_file = open('scenario.txt', 'r', encoding='utf-8')
lines = text_file.readlines()
print(lines)
print(len(lines))
text_file.close()

text_file = open('scenario.txt', 'r', encoding='utf-8')
for line in text_file:
    print(line)
text_file.close()

input('press enter')