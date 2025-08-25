#!/usr/bin/env python3

# lib/shoe.py

class Shoe:
    def __init__(self, brand: str, size: int):
        self._brand = None
        self._size = None
        self._condition = "New"

        self.brand = brand
        self.size = size

    # ----- brand -----
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        if not isinstance(value, str):
            raise Exception("brand must be a string")
        self._brand = value

    # ----- size -----
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value: int):
        
        if not isinstance(value, int):
            print("size must be an integer")
            return
        if value <= 0:
            # optional extra guard; tests don't check this
            raise Exception("size must be positive")
        self._size = value


    # ----- condition -----
    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, value: str):
        if not isinstance(value, str):
            raise Exception("condition must be a string")
        self._condition = value

    # ----- instance method -----
    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def __repr__(self):
        return f"Shoe(brand={self.brand!r}, size={self.size}, condition={self.condition!r})"
