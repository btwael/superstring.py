SUPERSTRING_MINIMAL_LENGTH = 48


class SuperStringBase(object):
    def length(self):
        pass

    def lower(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.to_printable().lower())
        return SuperStringLower(self)

    def upper(self):
        if self.length() < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.to_printable().upper())
        return SuperStringUpper(self)

    def character_at(self, index):
        pass

    def split(self, separator=" "):
        result = []
        previous = 0
        i = 0
        while i < self.length():
            for j in range(len(separator)):
                if self.character_at(i + j) != separator[j]:
                    break
            else:
                result.append(self.substring(previous, i))
                previous = i + len(separator)
            i = i + 1
        result.append(self.substring(previous))
        return result

    def substring(self, start_index, end_index=None):
        # TODO: if the substring is to short: copys
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        if start_index == 0 and end_index == self.length():
            return self
        if end_index - start_index < SUPERSTRING_MINIMAL_LENGTH:
            return SuperString(self.to_printable(start_index, end_index=end_index))
        return SuperStringSubstring(self, start_index, end_index)

    def strip(self):
        i = 0
        while self.character_at(i) == ' ':
            i = i + 1
        start_index = i
        i = self.length() - 1
        while self.character_at(i) == ' ':
            i = i - 1
        return self.substring(start_index, i + 1)

    def to_printable(self, start_index=None, end_index=None):
        pass

    def __len__(self):
        return self.length()

    def __add__(self, right):
        if not issubclass(type(right), SuperStringBase):
            right = SuperString(str(right))
        return SuperStringConcatenation(self, right)

    def __str__(self):
        return self.to_printable()

    def __getitem__(self, key):
        if isinstance(key, slice):
            start = key.start if key.start > 0 else self.length() + key.start
            stop = key.stop if key.stop > 0 else self.length() + key.stop
            return self.substring(start, end_index=stop)
        return self.character_at(key)


class SuperString(SuperStringBase):
    def __init__(self, content):
        self._content = content

    def length(self):
        if not hasattr(self, '_length'):
            self._length = len(self._content)
        return self._length

    def character_at(self, index):
        return self._content[index]

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        return self._content[start_index:end_index]


class SuperStringConcatenation(SuperStringBase):
    def __init__(self, left, right):
        self._left = left
        self._right = right

    def length(self):
        return self._left.length() + self._right.length()

    def character_at(self, index):
        left_len = self._left.length()
        if index < left_len:
            return self._left[index]
        return self._right[index - left_len]

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        left_len = self._left.length()
        if end_index < left_len:
            return self._left.to_printable(start_index=start_index, end_index=end_index)
        elif start_index > left_len:
            return self._right.to_printable(start_index=start_index - left_len, end_index=end_index - left_len)
        return self._left.to_printable(start_index=start_index) + self._right.to_printable(
            end_index=end_index - left_len)


class SuperStringSubstring(SuperStringBase):
    def __init__(self, base, start_index, end_index):
        self._base = base
        self._start_index = start_index
        self._end_index = end_index

    def length(self):
        return self._end_index - self._start_index

    def character_at(self, index):
        return self._base.character_at(self._start_index + index)

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        start_index += self._start_index
        end_index += self._start_index
        return self._base.to_printable(start_index, end_index=end_index)


class SuperStringLower(SuperStringBase):
    def __init__(self, base):
        self._base = base

    def length(self):
        return self._base.length()

    def character_at(self, index):
        return self._base.character_at(index).lower()

    def to_printable(self, start_index=None, end_index=None):
        return self._base.to_printable(start_index, end_index).lower()


class SuperStringUpper(SuperStringBase):
    def __init__(self, base):
        self._base = base

    def length(self):
        return self._base.length()

    def character_at(self, index):
        return self._base.character_at(index).upper()

    def to_printable(self, start_index=None, end_index=None):
        return self._base.to_printable(start_index, end_index).upper()
