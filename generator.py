def generatorTest(list):
    for node in list:
        yield node


list = ["one", "two"]

for num in generatorTest(list):
    print("num:", num)
