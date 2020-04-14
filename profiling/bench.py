import timeit
from memory_profiler import profile

from superstring.superstring import SuperString

with open('big_string.txt') as file:
    text = file.read()

super_string_fp = open('super_string_memory.log', 'w+')
string_fp = open('string_memory.log', 'w+')


@profile(stream=super_string_fp)
def test_superstring():
    splits = []
    string = SuperString(text)
    for i in range(1, len(string)):
        for j in range(0, len(string), i):
            splits.append(string[j:j + i])
    print(len(splits))
    return splits


@profile(stream=string_fp)
def test_string():
    splits = []
    string = text
    for i in range(1, len(string)):
        for j in range(0, len(string), i):
            splits.append(string[j:j + i])
    print(len(splits))
    return splits


test_superstring()
test_string()
