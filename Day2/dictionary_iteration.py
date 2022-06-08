my_words = {"hello":"hola", "thanky you":"gracias", "yes":"si"}

for key in my_words:
    print(key)
# returns
# hello
# thanky you
# yes   

for value in my_words.values():
    print(value)
# returns
# hola
# gracias
# si

for keyvalue in my_words.items():
    print(keyvalue)
# returns
# ('hello', 'hola')
# ('thanky you', 'gracias')
# ('yes', 'si')