from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr

    def query(self, left: int, right: int, value: int) -> int:
        sub_arr = self.arr[left:right + 1]
        sub_arr.sort()

        arr_set = set(sub_arr)
        arr_appear = []

        for num in arr_set:
            arr_appear.append(sub_arr.index(num))
        l, r = 0, len(sub_arr) - 1
        i = (l + r) // 2
        while l <= r:
            if sub_arr[i] <= value:
                l = i
                i = (l + r) // 2
            elif sub_arr[i] > value:
                r = i
                i = (l + r) // 2
            elif sub_arr[l] == value and sub_arr[r] == value:
                break
        return r - l + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)

if __name__ == '__main__':
    rangeFreqQuery = RangeFreqQuery([1, 1, 1, 2, 2])
    print(rangeFreqQuery.query(2, 4, 2))
