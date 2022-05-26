class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)

        start = -1
        for i in range(n-1):
            if A[i] > A[i+1]:
                start = 1
                break
        
        if start == -1:
            return [-1]

        end = -1
        for i in range(n-1, 0, -1):
            if A[i] < A[i-1]:
                end = i
                break
        min_value = min(A[start:end+1])
        max_value = max(A[start:end+1])

        for i in range(0, start):
            if A[i] > min_value:
                start = i
                break

        for i in range(n-1, end, -1):
            if A[i] < max_value:
                end = i
                break

        return [start, end]