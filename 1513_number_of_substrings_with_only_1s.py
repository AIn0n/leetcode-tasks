class Solution:

    MAX_CAP = 10**9 + 7

    def partition(t, s: str, stopper: str = "0") -> list[str]:
        res = [""]
        stop_adding = False
        for el in s:
            if el == stopper:
                if stop_adding is not True:
                    res.append("")
                stop_adding = True
                continue
            res[-1] += el
            stop_adding = False
        
        return res

    def numSub(self, s: str) -> int:
        substrings = self.partition(s)
        res = 0
        for el in substrings:
            n = len(el)
            if n == 1:
                res += 1
            else:
                res += (n + 1) * n // 2
        return res % MAX_CAP
        