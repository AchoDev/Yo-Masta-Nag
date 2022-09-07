import math, asyncio

def raise_test(value, power):
    first_value = value
    for i in range(power - 1):
        value *= first_value    
    return value

class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def say_hello(self):
        print("hello!")


class child(parent):
    def __init__(self, name, age, fav_candy):
        super().__init__(name, age)
        self.fav_candy = fav_candy

    def say_hello(self):
        super().say_hello()
        print("i am a child!!")


kid = child("okan", 2, "taco")

print(kid.get_age())
print(kid.name)

kid.say_hello()

# print(11 // 5 + 11 % 5)
print(math.ceil(5 / 3))

async def head():
    t1 = asyncio.create_task(test1())
    asyncio.create_task(test2())

    await t1

    print("end")

async def test1():
    while(True):
        print("hello")
        await asyncio.sleep(0.25)

async def test2():
    while(True):
        print("hey")
        await asyncio.sleep(0.5)

# asyncio.run(head())