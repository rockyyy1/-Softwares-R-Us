# In your own words, describe what sorting is in general. 
Sorting, in terms of programming is a method or algorithm that is used to order elements in a specified way. For example, sorting can be used to order a list of integers from lowest to highest or highest to lowest. Sorting can also be used to other things such as strings in alphabetical or character count.

# Research sorting algorithms. Describe advantages and disadvantages for at least three different sorting algorithms. Please provide references for external resources
Resources: https://www.geeksforgeeks.org/bubble-sort-algorithm/

https://www.geeksforgeeks.org/quick-sort-algorithm/

https://www.geeksforgeeks.org/bucket-sort-2/

## Bubble Sort
Traverses and compares adjacent items and swaps them if they’re out of order.

Advantages: Requires no additional memory.

Disadvantages: Has a worst-case and average time complexity of O(n2)

## Quicksort
Selects an item (pivot point) and arranges items so smaller items are before the pivot and larger items are after it.

Advantages: Average time complexity is O(n log n).

Disadvantages: It’s unstable and can degrade to O(n2) with poor pivot points.

## Bucket Sort
Distributes elements into buckets based on value ranges, sorts each bucket, and combines them.

Advantages: Fast for uniformly distributed data O(n+k).

Disadvantages: Requires extra memory for buckets.

# In your own words, describe why you generally need comparison operators to successfully sort a list of objects. In addition, describe how you could sort a list of objects without adding comparison operators.
Objects don't know how to arrange themselves or have any way to decide their order, so comparison operators are needed to determine how the algorithm compares and arrange the objects.

To sort without comparison operators, you could sort using the object's properties instead of the object itself. 