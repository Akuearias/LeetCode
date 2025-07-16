def countInversions(arr):
    def MergeSort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = MergeSort(arr[:mid])
        right, inv_right = MergeSort(arr[mid:])
        merged, inv_split = merge_and_count(left, right)
        return merged, inv_left + inv_right + inv_split

    def merge_and_count(left, right):
        merged = []
        i = j = inv_count = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged += left[i:]
        merged += right[j:]
        return merged, inv_count

    return MergeSort(arr)[1]