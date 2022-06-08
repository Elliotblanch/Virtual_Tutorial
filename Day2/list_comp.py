my_words = {"hello":"hola", "thanky you":"gracias", "yes":"si"}
result = []
for x in my_words.values():
    result.append(x)
    print(result)

# returns
# ['hola']
# ['hola', 'gracias']
# ['hola', 'gracias', 'si']