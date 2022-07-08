class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandie = max(candies)
        for idx, val in enumerate(candies):
            
            candies[idx] =  not (val + extraCandies) < maxCandie
        
        return candies
