class Solution:
    def reverseBits(self, n: int) -> int:
        n_bits = list(bin(n)[2:])
        l = len(n_bits)
        n_bits = ['0' for _ in range(32 - l)] + n_bits
        for i in range(len(n_bits) // 2):
            n_bits[i], n_bits[len(n_bits) - i - 1] = n_bits[len(n_bits) - i - 1], n_bits[i]

        S = int(''.join(n_bits), base=2)
        return S
