class Solution:
    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        result, c, q = 0, Counter([0]), 0
        for v in a:
            q += v%2
            c[q] += 1
            result += c[q-k]

        return result