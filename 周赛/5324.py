# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:54:19 2020

@author: Alex

code for windows
"""

class Cashier:

    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.count = n


    def getBill(self, product, amount):
        price = 0
        for i in range(len(product)):
            index = self.products.index(product[i])
            price += self.prices[index] * amount[i]
        self.count -= 1
        if self.count == 0:
            acc = 1 - self.discount / 100
            self.count = self.n
        else:
            acc = 1
        return acc*price
    
# Your Cashier object will be instantiated and called as such:
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // 返回 500.0, 账单金额为 = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // 返回 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // 返回 800.0 ，账单原本为 1600.0 ，但由于该顾客是第三位顾客，他将得到 50% 的折扣，所以实际金额为 1600 - 1600 * (50 / 100) = 800 。
cashier.getBill([4],[10]);                           // 返回 4000.0
cashier.getBill([7,3],[10,10]);                      // 返回 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // 返回 7350.0 ，账单原本为 14700.0 ，但由于系统计数再次达到三，该顾客将得到 50% 的折扣，实际金额为 7350.0 。
cashier.getBill([2,3,5],[5,3,2]);                    // 返回 2500.0
