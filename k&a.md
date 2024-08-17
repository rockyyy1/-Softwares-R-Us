All of the above functions are hash functions. Explain how so - what key properties do they all share?
Resources: https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/

"A hash function is a function that takes an input (or ‘message’) and returns a fixed-size string of byte"

ssh() returns the output as 1, no matter the input. It's not a really good hashing function because every input returns the same output but is technically still a hash because each input returns a fixed value.

sum_of_ascii_values() iterates over each character of the string input, gets that character's ASCII value and adds that value to the running total. The resulting total value is the hash value.

pearson_hash() maps a string of text and returns a number between 0 and 255. 
It uses a pearson table (an array of 256 random integers, each between 0 and 255). 
Starting at value of 0, The function iterates over each character of the string and then performs a Bitwise XOR operation of that value with the ASCII value of the character. 
e.g with string "h"
_hash is 0 to start and ord('h') gives the ASCII value of 'h', which is 104.
0 ^ 104 (0 XOR 104) performs a bitwise XOR operation between 0 and 104, resulting in 104
then it goes to index 104 of the pearson_table (which is random number generated earlier)
The loop continues with that random value becomiing _hash to be XOR'ed with the next character's ASCII value
After iterating over the characters, the final hash value hash_ modulo size to ensure it falls within the desired range.

built_in_hash() - Resources: https://www.codecademy.com/resources/docs/python/built-in-functions/hash
This function calculates a hash value for an object using the object's __hash__() method. 
The object can be numbers, strings, tuples, or custom objects that have implemented the __hash__() method. 
Strings: Hashes the string's characters using a polynomial rolling hash function.
Integers: Returns the integer value as its hash value. 
Tuples: Combines the hash values of its elements using a combination of bitwise XOR and addition.
So, the hash value is computed using specific hashing algorithms based on the object’s type.

sha256_hash() 
Resource: https://www.educative.io/answers/what-are-the-different-steps-in-sha-256
Returns a hexadecimal number of 64 digits
It involves adding bits to ensure input data is a multiple of 64 bytes.
The padded data is divided into 64-byte chunks, processed using a series of bitwise operations (AND, OR, XOR, ROTATE, etc.), and mixed with constants and variables to produce a 256-bit hash value.
The hash value is further mixed and transformed to produce the final 256-bit SHA-256 hash value.

The key propertes all these function share are:
Determinism: Given the same input, they always produce the same output hash value.



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