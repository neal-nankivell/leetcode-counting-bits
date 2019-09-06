# Given a non negative integer number num.
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in
# their binary representation and return them as an array.


class Solution:
    def countBits(self, num: int):
        return [self.hammingWeight(n) for n in range(num + 1)]

    def hammingWeight(x):
        x -= (x >> 1) & 0x5555555555555555
        x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
        x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
        return ((x * 0x0101010101010101) & 0xffffffffffffffff) >> 56
