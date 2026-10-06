# ============================================================
# 1. REMOVE DUPLICATES FROM SORTED ARRAY
# ============================================================
class RemoveDuplicatesSolution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


# ============================================================
# 2. SQUARES OF A SORTED ARRAY
# ============================================================
class SortedSquaresSolution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1

        return result


# ============================================================
# 3. MERGE SORTED ARRAY
# ============================================================
class MergeSortedArraySolution:
    def merge(self, nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1


# ============================================================
# 4. PLUS ONE
# ============================================================
class PlusOneSolution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = len(digits) - 1

        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0
            i -= 1

        return [1] + digits


# ============================================================
# 5. SORT ARRAY BY PARITY
# ============================================================
class SortArrayByParitySolution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            elif nums[right] % 2 != 0:
                right -= 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


# ============================================================
# 6. BEST TIME TO BUY AND SELL STOCK II / MAX PROFIT
# ============================================================
class MaxProfitSolution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit


# ============================================================
# 7. ROTATE IMAGE - 90 DEGREES CLOCKWISE
# ============================================================
class RotateImageSolution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse every row
        for i in range(n):
            matrix[i].reverse()


# ============================================================
# 8. SET MATRIX ZEROES
# O(1) EXTRA SPACE
# ============================================================
class SetZeroesSolution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Mark rows and columns using first row/column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero marked rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero marked columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# ============================================================
# 9. FIND THE DUPLICATE NUMBER
# FLOYD'S CYCLE DETECTION - O(n) TIME, O(1) SPACE
# ============================================================
class FindDuplicateSolution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find the meeting point inside the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find the entrance of the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


# ============================================================
# 10. SPIRAL MATRIX
# CLOCKWISE, OUTSIDE TO INSIDE
# ============================================================
class SpiralMatrixSolution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        if not matrix or not matrix[0]:
            return result

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Top row: left -> right
            for j in range(left, right + 1):
                result.append(matrix[top][j])
            top += 1

            # Right column: top -> bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Bottom row: right -> left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    result.append(matrix[bottom][j])
                bottom -= 1

            # Left column: bottom -> top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result


# ============================================================
# QUICK VERIFICATION TESTS
# ============================================================
if __name__ == "__main__":

    # 1. Remove Duplicates
    nums = [1, 1, 2, 2, 3]
    k = RemoveDuplicatesSolution().removeDuplicates(nums)
    print("1. Remove Duplicates:", k, nums[:k])

    # 2. Sorted Squares
    print("2. Sorted Squares:",
          SortedSquaresSolution().sortedSquares([-4, -1, 0, 3, 10]))

    # 3. Merge Sorted Array
    nums1 = [1, 2, 3, 0, 0, 0]
    MergeSortedArraySolution().merge(nums1, 3, [2, 5, 6], 3)
    print("3. Merge Sorted Array:", nums1)

    # 4. Plus One
    print("4. Plus One:", PlusOneSolution().plusOne([1, 2, 9]))

    # 5. Sort Array by Parity
    print("5. Sort Array by Parity:",
          SortArrayByParitySolution().sortArrayByParity([3, 1, 2, 4]))

    # 6. Max Profit
    print("6. Max Profit:",
          MaxProfitSolution().maxProfit([7, 1, 5, 3, 6, 4]))

    # 7. Rotate Image
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    RotateImageSolution().rotate(matrix)
    print("7. Rotate Image:", matrix)

    # 8. Set Matrix Zeroes
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    SetZeroesSolution().setZeroes(matrix)
    print("8. Set Matrix Zeroes:", matrix)

    # 9. Find Duplicate
    print("9. Find Duplicate:",
          FindDuplicateSolution().findDuplicate([1, 3, 4, 2, 2]))

    # 10. Spiral Matrix
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("10. Spiral Matrix:",
          SpiralMatrixSolution().spiralOrder(matrix))