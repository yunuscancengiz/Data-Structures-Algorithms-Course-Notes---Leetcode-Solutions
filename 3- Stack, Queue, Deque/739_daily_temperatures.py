''' 
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append([temp, idx])
        return result
    

    def alternative_solution(self, temperatures):
        # tek liste üzerinde tüm işlemleri halleder space complexity O(1)
        # Ancak her eleman için listedeki geri kalan tüm elemanları gezer (worst scenario)
        # Bu yüzden time complexity O(n^2)
        # Üstteki çözümün space complexity = o(n) olsa da time complexity = O(n) o yüzden daha efektif

        index = 0
        counter = 1

        while index < len(temperatures):
            if index + counter >= len(temperatures):
                temperatures[index] = 0
                index += 1
                counter = 1
                continue

            if temperatures[index] < temperatures[index + counter]:
                temperatures[index] = counter
                index += 1
                counter = 1

            else:
                counter += 1
        return temperatures
    

if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    #temperatures = [1,2,3,4,5,6,7,8,9]
    #temperatures = [30, 40, 50, 60]
    temperatures = [34,34,34,34,34,34,34,34,34,34,34,34,34,34,34]
    #print(Solution().dailyTemperatures(temperatures=temperatures))
    #print(Solution().alternative_solution(temperatures=temperatures))