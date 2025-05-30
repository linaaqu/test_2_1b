from math import factorial

def fact(x):
    if(x == 0):
        return 1
    return factorial(x)

print(fact(0))



def simple(q):
    if q == 1:
        return "Простое"
    if q <= 1:
        return "Ни простое, ни составное"
    for i in range(2, q):
        if q % i == 0:
            return "Составное"
    return "Простое"

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = elements(my_list)
print(unique_list)



def group_words(words):
    list = {}
    for word in words:
        length = len(word)
        if length not in list:
            list[length] = []
        list[length].append(word)
    return list

words_list = ["apple", "banana", "pear", "kiwi", "grape", "fig"]
result = group_words(words_list)
print(result)
