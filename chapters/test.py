from typing import List

'''
输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #corner case check
        if amount == 0:
            return 0
        