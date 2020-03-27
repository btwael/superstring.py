SUPERSTRING_MINIMAL_LENGTH = 48

class SuperStringBase(object):
    def length(self):
        pass

    def lower(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.toPrintable().lower())
        return SuperStringLower(self)

    def upper(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.toPrintable().upper())
        return SuperStringUpper(self)

    def characterAt(self, index):
        pass

    def split(self, separator = " "):
        result = []
        previous = 0
        i = 0
        while i < self.length():
            gonext = False
            j = 0
            while j < len(separator):
                if self.characterAt(i + j) != separator[j]:
                    gonext = True
                    break
                j = j + 1
            if not gonext:
                result.append(self.substring(previous, i))
                previous = i + len(separator)
            i = i + 1
        result.append(self.substring(previous))
        return result

    def substring(self, startIndex, endIndex = None):
        # TODO: if the substring is to short: copy
        if startIndex == None:
            startIndex = 0
        if endIndex == None:
            endIndex = self.length()
        if startIndex == 0 and endIndex == self.length():
            return self
        if endIndex - startIndex < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.toPrintable(startIndex, endIndex = endIndex))
        return SuperStringSubstring(self, startIndex, endIndex)

    def strip(self):
        i = 0
        while self.characterAt(i) == ' ':
            i = i + 1
        startIndex = i
        i = self.length() - 1
        while self.characterAt(i) == ' ':
            i = i - 1
        return self.substring(startIndex, i + 1)

    def toPrintable(self, startIndex = None, endIndex = None):
        pass

    def __len__(self):
        return self.length()

    def __add__(self, right):
        if not issubclass(type(right), SuperStringBase):
            right = SuperString(str(right))
        return SuperStringConcatenation(self, right)

    def __str__(self):
        return self.toPrintable()

    def __getitem__(self, key):
        # TODO: Negative Indexing
        if isinstance(key, slice):
            return self.substring(key.start, endIndex = key.stop)
        return self.characterAt(key)

class SuperString(SuperStringBase):
    def __init__(self, content):
        self._content = content

    def length(self):
        if not hasattr(self,'_length'):
            self._length = len(self._content)
        return self._length

    def characterAt(self, index):
        return self._content[index]

    def toPrintable(self, startIndex = None, endIndex = None):
        if startIndex != None:
            if endIndex == None:
                endIndex = self.length()
            return self._content[startIndex:endIndex]
        elif endIndex != None:
            return self._content[0:endIndex]
        return self._content

class SuperStringConcatenation(SuperStringBase):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def length(self):
        return self._left.length() + self._right.length()

    def characterAt(self, index):
        leftLen = self._left.length()
        if index < leftLen:
            return self._left[index]
        return self._right[index - leftLen]

    def toPrintable(self, startIndex = None, endIndex = None):
        if startIndex == None:
            startIndex = 0
        if endIndex == None:
            endIndex = self.length()
        leftLen = self._left.length()
        if endIndex < leftLen:
            return self._left.toPrintable(startIndex = startIndex, endIndex = endIndex)
        elif startIndex > leftLen:
            return self._right.toPrintable(startIndex = startIndex - leftLen, endIndex = endIndex - leftLen)
        return self._left.toPrintable(startIndex = startIndex) + self._right.toPrintable(endIndex = endIndex - leftLen)

class SuperStringSubstring(SuperStringBase):
    def __init__(self, base, startIndex, endIndex):
        self._base = base
        self._startIndex = startIndex
        self._endIndex = endIndex

    def length(self):
        return self._endIndex - self._startIndex

    def characterAt(self, index):
        return self._base.characterAt(self._startIndex + index)

    def toPrintable(self, startIndex = None, endIndex = None):
        if startIndex == None:
            startIndex = 0
        if endIndex == None:
            endIndex = self.length()
        startIndex += self._startIndex
        endIndex += self._startIndex
        return self._base.toPrintable(startIndex, endIndex = endIndex)

class SuperStringLower(SuperStringBase):
    def __init__(self, base):
        self._base = base

    def length(self):
        return self._base.length()

    def characterAt(self, index):
        return self._base.characterAt(index).lower()

    def toPrintable(self, startIndex = None, endIndex = None):
        return self._base.toPrintable(startIndex, endIndex).lower()

class SuperStringUpper(SuperStringBase):
    def __init__(self, base):
        self._base = base

    def length(self):
        return self._base.length()

    def characterAt(self, index):
        return self._base.characterAt(index).upper()

    def toPrintable(self, startIndex = None, endIndex = None):
        return self._base.toPrintable(startIndex, endIndex).upper()
