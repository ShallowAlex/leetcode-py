# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 10:56:52 2020

@author: Alex

code for windows
"""

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxsize = maxSize
        self.arr = []
        self.lengh = len(self.arr)


    def push(self, x: int) -> None:
        if self.lengh <= self.maxsize:
            self.arr.append(x)
            self.lengh += 1


    def pop(self) -> int:
        if self.lengh:
            return self.arr.pop()
            self.lengh -= 1
        else:
            return -1


    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < self.lengh-1:
                self.arr[i] += val
            else:
                break
if __name__ == "__main__":
    s = CustomStack(3)
    s.push(1)
    s.push(2)
    s.pop()
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.arr)
    s.increment(5, 100)
    s.increment(2, 100)
    print("***")
    