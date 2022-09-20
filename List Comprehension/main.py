list1 = []

list2 = []

l = open("List Comprehension/file1.txt")
letter_cont1 = l.readlines()
for name in letter_cont1:
    s = name.strip()
    list1.append(s)

k = open("List Comprehension/file2.txt")
letter_cont = k.readlines()
for name in letter_cont:
    s = name.strip()
    list2.append(s)

result = [num for num in list1 if num in list2]
# Write your code above 👆
print(list1)
print(list2)
print(result)
