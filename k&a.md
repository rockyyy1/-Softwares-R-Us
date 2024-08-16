All of the above functions are hash functions. Explain how so - what key properties do they all share?
"A hash function is a function that takes an input (or ‘message’) and returns a fixed-size string of byte"

ssh() returns the output as 1, no matter the input. Technically this is still a hash because the original input cannot be calculated from this hash.

sum_of_ascii_values() returns the sum of the ord value of each character. This is a hash function because it is transforming a string into a different output.

pearson_hash() maps a string of text to return a number between 0 and 255. 

built_in_hash() - Resources: https://www.codecademy.com/resources/docs/python/built-in-functions/hash
Returns the hash value of an object as a fixed sized integer. 
The object can be of various types, including numbers, strings, tuples, or custom objects that have implemented the __hash__() method. 
The hash value is computed using a specific hashing algorithm based on the object’s type.

sha256_hash() 
Returns a hexadecimal number of 64 digits

What are the advantages and disadvantages of each of the above hash functions? 
Evaluate in terms of uniformity, determinism, efficiency, collision resistance, sensitivity to input changes, and security. 
You may need to do some research to answer this question 😱

ssh()
Not unique at all guaranteeing a hash collision!

sum_of_ascii_values() 
While better than ssh(), there is still a high chance of a hash collision for many inputs. For example, given the same size, for inputs "abc" and "bca"  they both return 4.
which is a collision.

pearson_hash()
From what I understand, this isn't that unique because any two inputs can have a 1 in 255 of the same hash.
After skim-reading the paper (https://www.epaperpress.com/vbhash/download/p677-pearson.pdf), Of the 26,662 inputs of dictionary words after hashing a tallying the result 0-255, "the resulting 256 counts were not
all equal, but they are not alarmingly uneven". Also, similar strings are not likely to collide.


built_in_hash()

sha256_hash()

List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.
Your answer here

Which of the above hash functions would you choose to implement the requirements of the task? Why?
Your answer here

In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.
Your answer here

Write pseudocode of how you would store Players in PlayerLists in a hash map.
Your answer here

Reflection
What was the most challenging aspect of this task?
Your answer here

If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?
Your answer here