def quickSort(arr):
    # Step 1: Choose the pivot
    p = arr[0]  # The pivot is the first element of the array
    
    # Step 2: Partition the array into three parts: left, equal, right
    left = [x for x in arr if x < p]   # Elements less than pivot
    equal = [x for x in arr if x == p] # Elements equal to pivot
    right = [x for x in arr if x > p]  # Elements greater than pivot
    
    # Step 3: Concatenate the partitions and return
    return left + equal + right

# Example usage
if __name__ == "__main__":
    n = int(input().strip())  # Read the size of the array
    arr = list(map(int, input().strip().split()))  # Read the array elements
    result = quickSort(arr)  # Applying quickSort to partition the array
    print(" ".join(map(str, result)))  # Print the result as space-separated integers
