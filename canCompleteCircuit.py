class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        i = 0
        while i < n:
            total_gas = total_cost = 0
            dummy = 0
            while dummy < n:
                j = (i + dummy) % n
                total_gas += gas[j]
                total_cost += cost[j]
                if total_gas < total_cost:
                    break
                dummy += 1
            if dummy == n:
                return i

            else:
                i += dummy + 1
        return -1
