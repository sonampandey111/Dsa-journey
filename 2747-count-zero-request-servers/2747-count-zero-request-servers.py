
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda a: a[1])
        q = sorted((time, i) for i, time in enumerate(queries))
        
        freq = [0] * (n + 1)

        ans = [0] * len(queries)

        l = r = 0
        active = 0
        m = len(logs)

        for time, idx in q:
            while r < m and logs[r][1] <= time:
                server = logs[r][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                r += 1
            while l < m and logs[l][1] < time - x:
                server = logs[l][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                l += 1
            ans[idx] = n - active

        return ans

        