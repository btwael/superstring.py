# superstring.py
**superstring.py** is an efficient library for heavy-text manipulation in Python, that achieves a remarkable memory and CPU optimization.

**superstring.py** uses Rope (data structure) and optimization techniques.

## Performance example

![alt text](https://github.com/btwael/superstring.py/raw/master/misc/comparison.png?raw=true "Comparison of superstring.py and python built-in string")

*The two plots show the comparison  in terms of memory consumption and execution time between **superstring.py** and python build-in string (the comparison  program consists of appending to a list all possible substrings of a 50000 bytes text).*

## Features
- **Fast** and **Memory-optimized**.
- Rich API.
- Similar functionalities to python built-in string
- Easy to embed and  use.
- **MIT Licence**

## Installing

```shell
pip install superstring
```


## How to use
```python
from superstring import SuperString

string1 = SuperString("  This is ")
string2 = SuperString("SuperString!  ")

# concatenation
string = string1 + string2 # "  This is SuperString!  "

# print
print(string)

# length
len(string)
string.length()

# character
string[10] # "S"
string.characterAt(10) # "S"

# substring
string[10:21] # "SuperString"
string.substring(10, 21) # "SuperString"

# strip
string.strip() # "This is SuperString!"

# lower
string.lower() # "  this is superstring!  "

# upper
string.upper() # "  THIS IS SUPERSTRING!  "

```

## Roadmap
- [ ] Optimize even more (I think it's possible :sunglasses:)
- [x] Support for negative indexing
- [ ] More benchmark and memory profiling

## Contribute and support
You have any feature idea, a bug to correct or an improvement, feel free to [open a issue]( https://github.com/btwael/SuperString/issues) or [send your pull request](https://github.com/btwael/SuperString/pulls).
You can also support the author of **superstring.py** via [Paypal](https://www.paypal.me/btwael).

## LICENCE
MIT LICENCE
