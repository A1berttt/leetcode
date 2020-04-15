class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = l1
        k = (l1 + l2 + 1) // 2
        while left < right:
            m1 = (left + right) // 2
            m2 = k - m1
            if nums1[m1] < nums2[m2 - 1]:
                left = m1 + 1
            else:
                right = m1
        m1 = left
        m2 = k - m1
        c1 = max(nums1[m1 - 1] if m1 > 0 else float('-inf'), nums2[m2 - 1] if m2 > 0 else float('-inf'))
        if (l1 + l2) % 2 == 1:
            return c1
        c2 = min(nums1[m1] if m1 < l1 else float('inf'), nums2[m2] if m2 < l2 else float('inf'))
        return (c1 + c2) / 2
