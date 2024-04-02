class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        res = t
        mapped = []
        for c1, c2 in zip(t, s):
            if c2 not in mapped:
                res = res.replace(c1, c2)
                mapped.append(c2)
            print(res)
        return res == s
    
sol = Solution()

print(sol.isIsomorphic("foo", "bar"))