b = 5
a = 2

if b > a:
    print("b greater than a")
else:
    print("a greater than b")

print(bool("Hello"))
print(bool(15))
print(bool(a), bool(0), bool([]))  # empty is false


class MyClass():
    def __len__(self):
        return 0


myobj = MyClass()
print(bool(myobj))


def MyFunc():
    return True


if MyFunc():
    print("YES!")
else:
    print("NO!")

print(isinstance(b, int))
