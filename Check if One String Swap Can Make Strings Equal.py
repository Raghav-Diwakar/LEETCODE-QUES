class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if sorted(s1) == sorted(s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
                    if cnt > 2:
                        return 0  
            return 1
        return 0