print('create txt')
text_file = open('write_it.txt', 'w', encoding='utf-8')
text_file.write('строка 1\n это строка 2\n енто 3\n')
text_file.close()

print('reading the created file')
text_file = open('write_it.txt', 'w', encoding='utf-8')
print(text_file.read())
text_file.close()

print('creating a file using the method writelines()')
text_file = open('write_lines.txt', 'w', encoding='utf-8')

lines = ['Строка 1\n'
      'Это строка 2\n'
      'Вау это же 3\n']

text_file.writelines(lines)
text_file.close()

print('reading the created file')
text_file = open('write_lines.txt', 'w', encoding='utf-8')
print(text_file.read())
text_file.close()

input('press enter')