# Задание 7:
#     Чтение из файла.
#     Создайте файл с текстом The Zen of Python.
#     Напишите функцию, которая считайте его и возвратит список из слов, которые начинаются на букву “c” или “C”.
#     Подсказка: используйте метод строчных значений, который проверяет, начинается ли слово на переданную букву.
####################################################################
text = """
The Zen of Python, by Tim PetersBeautiful is better than ugly. Explicit is better than implicit.
Simple is better than complex. Complex is better than complicated.
Flat is better than nested.Sparse is better than dense.
Readability counts. Special cases aren't special enough to break the rules.Although practicality beats purity.
Errors should never pass silently.Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea --let's do more of those!
"""
with open('zenpython.txt', 'w') as file:
    file.write(text)
c_words = []
with open('zenpython.txt', 'r') as file:
    txt = file.read()
    txt = [i for i in txt.replace('\n', ' ').split(' ')]
    for i in txt:
        if i.startswith('c'):
            c_words.append(i)
        if i.startswith('C'):
            c_words.append(i)
print(c_words)