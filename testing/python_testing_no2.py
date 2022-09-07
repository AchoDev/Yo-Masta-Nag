
class Container:
    def __init__(self, value):
        self.value = value

var1 = Container(10)

var2 = var1.value + 10

print(var2)

var1.value += 10

print(var2)