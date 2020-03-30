class MergeSort:
    def mergeSort(self, arr):
        if len(arr) > 1:
            middle = len(arr) // 2
            left = arr[:middle]
            right = arr[middle:]

            # Sort the first half
            self.mergeSort(left)

            # Sort the second half
            self.mergeSort(right)

            # Merge the two lists
            left_pointer = 0
            right_pointer = 0

            for i in range(0, 2 * max(len(left), len(right))):
                if left_pointer < len(left) and right_pointer < len(right):
                    if left[left_pointer] <= right[right_pointer]:
                        arr[i] = left[left_pointer]
                        left_pointer += 1
                    else:
                        arr[i] = right[right_pointer]
                        right_pointer += 1
                elif left_pointer < len(left):
                    arr[i] = left[left_pointer]
                    left_pointer += 1
                elif right_pointer < len(right):
                    arr[i] = right[right_pointer]
                    right_pointer += 1
                else:
                    break
        return arr

# Example Use    
sol = MergeSort()
a = [9, -9, -8, 1, 2, 3, 4, 5, -5, -4, -3, -99, 267, 1/2]
sorted_list = sol.mergeSort(a)
