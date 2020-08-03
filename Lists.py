thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist[2:5])
thislist[3] = "currant"
print(thislist[-4:-1])

'''
for x in thislist:
    if len(x) > 5:
        print(x)
'''
if "apple" in thislist:
    print("Apple is in basket")

thislist.append("blueberry")
print(len(thislist))

thislist.insert(1, "cranberry")
print(thislist)

thislist.remove("banana")
print("banana" not in thislist)

thislist.pop(0)
thislist.pop()
print("apple" not in thislist, "blueberry" not in thislist)

print(thislist)
del thislist[0]
print(thislist)

thislist.clear()
print(thislist)

thislist = ["test", "more", "yes"]
mylist = thislist.copy()  # or use list(thislist)
print(mylist)

combine = thislist + mylist
print(combine)

num_one = [1, 2, 3]
letters = ["a", "b", "c"]
num_one.extend(letters)
print(num_one)

new_list = list(("apple", "banana", "cherry"))
print(new_list)

sort_list = [3, 2, 5, 6, 3, 5]
sort_list.sort()
print(sort_list, sort_list.count(3), "of value 3")
