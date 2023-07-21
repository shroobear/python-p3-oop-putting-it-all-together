#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    
    def get_size(self):
        print("Getting size")
        return self._size
    
    def set_size(self, size):
        if (type(size) == int):
            self._size = size
        else:
            print("size must be an integer")

    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"