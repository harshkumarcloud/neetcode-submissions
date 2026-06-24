class DynamicArray:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._size = 0
        self._data = [0] * self._capacity

    def get(self, i: int) -> int:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        return self._data[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self._size:
            raise IndexError("Index out of range")
        self._data[i] = n

    def pushback(self, n: int) -> None:
        if self._size >= self._capacity:
            self.resize()
        self._data[self._size] = n
        self._size += 1

    def popback(self) -> int:
        if self._size == 0:
            raise IndexError("Pop from empty array")
        value = self._data[self._size - 1]
        self._size -= 1
        return value

    def resize(self) -> None:
        new_capacity = self._capacity * 2
        new_data = [0] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._size

    def getCapacity(self) -> int:
        return self._capacity
