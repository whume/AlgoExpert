array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2
# def moveElementToEnd(array, toMove):
#     hits = 0
#     for idx, i in enumerate(array):
#         if toMove == i:
#             hits += 1
#             # array.append(toMove)
#     for _ in range(hits):
#         array.remove(toMove)
#         array.append(toMove)
#     return array

# Other Option

def moveElementToEnd(array, toMove):
    i = 0 
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
           array[i], array[j] = array[j], array[i] 
        i += 1
    return array

print(moveElementToEnd(array, toMove))

