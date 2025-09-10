class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            temp = nums1
            nums1 = nums2
            nums2 = temp
            temp = m 
            m = n
            n = temp
        if n == 0:
            if m % 2 == 0:
                return (nums1[m//2] + nums1[m//2 - 1])/2
            else:
                return (nums1[m//2])
        x1, y1 = 0, m - 1
        x2, y2 = 0, n - 1
        maxi = 10 ** 10
        mini = -(10 ** 10)
        while x1 <= y1 and x2 <= y2:
            mid2 = (x2 + y2 + 1) // 2
            mid1 = (n + m + 1)//2 - mid2
            print(x1, y1, x2, y2, mid1, mid2)
            if mid1 < m:
                r1 = nums1[mid1]
            else:
                r1 = maxi
            if mid2 < n:
                r2 = nums2[mid2]
            else:
                r2 = maxi
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            else:
                l1 = mini
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]
            else:
                l2 = mini
            if r1 < l2:
                y2 = mid2 - 1
                x1 = mid1
            elif r2 < l1:
                y1 = mid1 - 1
                x2 = mid2
            else:
                if (n + m) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return min(r1, r2)

        
arr1 = [1, 2]
arr2 = [3, 4, 5, 6, 7, 8, 9, 10, 11]
sol = Solution()
print(sol.findMedianSortedArrays(arr1, arr2))