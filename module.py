import mymodule as mx
from mymodule import person1
import platform

mx.greeting("Daniel")

a = mx.person1["age"]
print(a)

x = platform.system()
print(x)

y = dir(platform)
print(y)

print(person1["name"])
