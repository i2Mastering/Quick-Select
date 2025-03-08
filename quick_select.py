#project7
"""
Quick Select Algorithm Implementation

This Python module implements the Quick Select algorithm, which efficiently finds the k-th smallest element in an unsorted list.

Features:
- Uses the Quick Select algorithm to partition and find elements efficiently.
- Generates a random list of integers for testing.
- Includes an interactive user input system to select k.

Classes:
    - Solution: Contains Quick Select algorithm methods.

Example Usage:
    ```python
    python quick_select.py
    ```
    Output:
    ```
    Enter the value of k. Please choose a number between 1 and 1000: 5
    The array that has been generated with the total of one thousand numbers is: [...]
    The 5th smallest element is 42
    ```

Author: Ike Iloegbu
License: MIT
"""

import random

class Solution:
    """
    Implements the Quick Select algorithm to find the k-th smallest element in an array.
    """
    
    @staticmethod
    def arrSplit(nums, l, r):
        """Splits the array around a pivot, placing smaller elements on the left and larger on the right.
        
        Args:
            nums (list): Array of numbers.
            l (int): Left boundary index.
            r (int): Right boundary index.
        
        Returns:
            int: Partition index.
        """
        pivot = nums[l]
        i = l
        for j in range(l + 1, r + 1):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i], nums[l] = nums[l], nums[i]
        return i
    
    @staticmethod
    def quick_select(nums, l, r, k):
        """Finds the k-th smallest element in an unsorted list using Quick Select.
        
        Args:
            nums (list): The unsorted array.
            l (int): Left boundary index.
            r (int): Right boundary index.
            k (int): The k-th position to find.
        
        Returns:
            int: The k-th smallest element.
        """
        if l == r:
            return nums[l]
        pivot_index = Solution.arrSplit(nums, l, r)
        if k == pivot_index:
            return nums[k]
        elif k < pivot_index:
            return Solution.quick_select(nums, l, pivot_index - 1, k)
        else:
            return Solution.quick_select(nums, pivot_index + 1, r, k)

def main():
    """Main function that generates a random list and finds the k-th smallest element."""
    len_array = 1000    
    array = [random.randint(1, 1000) for _ in range(len_array)]
    
    while True:
        try:
            k = int(input("Enter the value of k. Please choose a number between 1 and 1000: "))
            if 1 <= k <= len_array:
                break
            print("Input invalid. Please enter a number between 1 and 1000.")
        except ValueError:
            print("Input invalid. Please enter a valid integer.")
    
    result = Solution.quick_select(array, 0, len_array - 1, k - 1)
    print(f"The array that has been generated with the total of one thousand numbers is: {array}")
    print(f"The {k}th smallest element is {result}")

if __name__ == "__main__":
    main()

            
