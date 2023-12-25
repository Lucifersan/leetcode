#really cute, redo someday because this code is horrible
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        size = price[len(price)-1] - price[0]
        hi = size//(k-2) + 1 if k > 2 else size + 1
        lo = 0
        mid = 0
        while hi > lo:
            mid = (hi + lo)//2
            basket = list()
            basket.append(price[0])
            for i in price:
                if i - basket[len(basket)-1] >= mid:
                    basket.append(i)
            if len(basket) >= k:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1