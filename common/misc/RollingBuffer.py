class RollingBuffer(object):
    def __init__(self, size):
        assert size > 0

        self._size = size
        self.reset()

    def reset(self):
        self._list = [None] * self._size
        self._cursor = -1
        self._append_count = 0

    def count(self):
        return len(self.get_last_n(self._size))

    def add(self, obj, fn_overwrite_callback = None):
        # assert self._cursor < self._size
        old_cursor = self._cursor + 1
        if old_cursor < 0:
            old_cursor += self._size
        old_cursor = old_cursor % self._size

        if self._list[old_cursor] is not None:
            old_Info = self._list[old_cursor]

            if fn_overwrite_callback is not None:
                fn_overwrite_callback(old_Info)

        self._append_count += 1

        self._cursor += 1
        self._cursor = self._cursor % self._size



        self._list[self._cursor] = obj

    def get_next_index(self):
        cursor = self._cursor
        cursor -= 1
        if cursor < 0:
            cursor = cursor + self._size
        return cursor


    def get_last_n(self, n):
        # assert n <= self._size
        assert n >= 0

        count = min (n, self._append_count)
        reverse_list = []
        cursor = self._cursor
        while count > 0 and self._list[cursor] is not None:
            reverse_list.append(self._list[cursor])
            cursor = self.get_next_index()
            count -= 1

        return reverse_list