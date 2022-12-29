class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dic = defaultdict(int)
        count = 0
        for num1 in deliciousness:
            power_num = 1
            for _ in range(22): 
                num2 = power_num - num1
                count += dic[num2]
                power_num *= 2 
            dic[num1] += 1
        # print(dic)
        return count % (10**9 + 7)
        