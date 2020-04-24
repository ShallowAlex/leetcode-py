class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x * y == 0:
            return x + y == z or z == 0
        a = max(x,y)
        b = min(x,y)
        while b != 0:
            tmp = b
            b = a % b
            a = tmp
        return z % a == 0


# class Solution:
#     def canMeasureWater(self, x: int, y: int, z: int) -> bool:
#         if z == 0:
#             return True
#         visited = set()
#         stack = [(0, 0)]
#         while stack:
#             cur_x, cur_y = stack.pop()
#             if cur_x == z or cur_y == z or cur_x + cur_y == z:
#                 return True
#             if (cur_x, cur_y) in visited:
#                 continue
#             visited.add((cur_x, cur_y))
            
#             stack.append((x, cur_y)) #给x加满
#             stack.append((cur_x, y)) #给y加满
#             stack.append((0, cur_y)) #将x倒空
#             stack.append((cur_x, 0)) #将y倒空
#             stack.append((max(0,x - y + cur_y), min(y, cur_y + cur_x))) #将x倒给y
#             stack.append((min(x,cur_x + cur_y), max(0, y - x + cur_x))) #将y倒给x
#             #x给y倒，y可倒(y-cur_y),x有cur_x,倒了max(cur_x, y - cur_y)
#             #x给y倒，y = min(y, cur_y+cur_x)
#         return False