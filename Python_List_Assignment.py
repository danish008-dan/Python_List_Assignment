# 1. Reverse a list in python
''''
Given - list1 = [100, 200, 300, 400, 500]
Expected output - [500, 400, 300, 400, 500]
'''

# Solution 1: list function reverse()
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

# Solution 2: Using negative slicing
list1 = list1[::-1]
print(list1)

# 2. Concatenate two lists index-wise
''''
Given - listtA = ["M", "na", "i", "ke"] listB = ["y", "me", "s", "lly"]
expected output: ['My', 'name', 'is', 'kelly']
'''

# Solution
listA = ["M", "na", "i", "ke"]
listB = ["y", "me", "s", "lly"]
listC = [i + j for i,j in zip(listA,listB)]
print(listC)

# 3. Turn every item of a list into its square
''''
Given - numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output - [1, 4, 9, 25, 36, 49]
'''

# Solution 1: Using loop and list method
numbers = [1, 2, 3, 4, 5, 6, 7]
# result list
res = []
for i in numbers:
    res.append(i*i)
print(res)

# Solution 2: Use list comprehension
res = [x * x for x in numbers]
print(res)

# 4. Concatenate two lists in the following order
''''
list1 = ["Hello", "take"] list2 = ["Dear", "Sir"]
Expected output: ["Hello Dear", "Hello Sir", "take Dear", "take Sir"]
'''

# Solution
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
res = [x + y for x in list1 for y in list2]
print(res)

# 5. iterate both lists simultaneously
''''
Given - list1 = [10, 20, 30, 40] list2 = [100, 200, 300, 400] -> in reverse order
expected output: 
10 400
20 300
30 200
40 100
'''

# Solution
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, list2[::-1]):
    print(x, y)


# 6. Remove empty strings from the list of strings
''''
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
Expected output - ["Mike", "Emma", "Kelly", "Brad"]
'''
# Solution
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)

# 7. Add new item to the list after a specified item
''''
Given - list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
Expected output: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

understand indexing
list1[0] = 10 
list1[1] = 20
list1[2] = [300, 400, [5000, 6000, 7000], 500]
list1[2][2] = [5000, 6000]
list1[2][2][1] = 6000
'''

# Solution
list1[2][2].append(7000)
print(list1)

# 8. Extend nested list by adding the sublist
''''
Given - list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] # sub list to add sub_list = ["h", "i", "j"
Expected output: ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
'''

# Solution
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

# 9. Replace list's item with new value if found
''''
Given - list1 = [5, 10, 15, 20, 25, 50, 20]
Expected output: [5 ,10 ,15 ,200, 25, 50, 20]
'''
# Solution
list1 = [5, 10, 15, 20, 25, 50, 20]
# get the first occurence index
index = list1.index(20)
# update item present at location
list1[index] = 200
print(list1)


# 10. Remove all occurrence of a specific item from a list
''''
Given - list1 = [5, 20, 15, 20, 25, 50, 20]
Expected output - [5, 15, 25, 50]
'''

# Solution1: Use the list comprehension
list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_specific_item(sample_list, val):
    return [i for i in sample_list if i != val]
res = remove_specific_item(list1, 20)
print(res)

# Solution2: While loop
list1 = [5, 20, 15, 20, 25, 50, 20]

while 20 in list1:
    list1.remove(20)
print(list1)


# =================== COMPLETED ===================== #