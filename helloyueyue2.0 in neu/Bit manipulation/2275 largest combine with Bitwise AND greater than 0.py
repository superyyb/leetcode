class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        #Why 24? Because the question says max(candidates) <= 10^7, which is < 2^24
        #Check easily next time by print(bin(10000000))
        bit_counts = [0] * 24

        # Count the number of times each bit position is set to 1 across all numbers
        for number in candidates:
            for i in range(24):
                if number & (1 << i):  # Check if the i-th bit is set to 1
                    bit_counts[i] += 1

        # The result is the maximum count found in any bit position
        return max(bit_counts)

    """
if number & (1 << i):  # Check if the i-th bit is set to 1
if number & (1 << 1):  # Check if the 1-th bit is set to 1

candidates = [16,17,71,62,12,24,14]
  candidate         bit6 bit5 bit4 bit3 bit2 bit1 bit0
16   0010000         0    0    1    0    0    0    0
17   0010001         0    0    1    0    0    0    1
71   1000111         1    0    0    0    1    1    1
62   0111110         0    1    1    1    1    1    0
12   0001100         0    0    0    1    1    0    0
24   0011000         0    0    1    1    0    0    0
14   0001110         0    0    0    1    1    1    0

•   bit0: 2
•	bit1: 3
•	bit2: 4
•	bit3: 4
•	bit4: 4
•	bit5: 1
•	bit6: 1. max_count = 4
    """