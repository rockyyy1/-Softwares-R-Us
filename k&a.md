# All of the above functions are hash functions. Explain how so - what key properties do they all share?
Resources: https://www.geeksforgeeks.org/hash-functions-and-list-types-of-hash-functions/

"A hash function is a function that takes an input (or ‘message’) and returns a fixed-size string of byte"

ssh() returns the output as 1, no matter the input. It's not a really good hashing function because every input returns the same output but is technically still a hash because each input returns a fixed value.

sum_of_ascii_values() iterates over each character of the string input, gets that character's ASCII value and adds that value to the running total. The resulting total value is the hash value.

pearson_hash() maps a string of text and returns a number between 0 and 255. It uses a pearson table (an array of 256 random integers, each between 0 and 255). 
Starting at value of 0, The function iterates over each character of the string and then performs a Bitwise XOR operation of that value with the ASCII value of the character. 
e.g with string "h" _hash is 0 to start and ord('h') gives the ASCII value of 'h', which is 104.
0 ^ 104 (0 XOR 104) performs a bitwise XOR operation between 0 and 104, resulting in 104
then it goes to index 104 of the pearson_table (which is random number generated earlier)
The loop continues with that random value becomiing _hash to be XOR'ed with the next character's ASCII value
After iterating over the characters, the final hash value hash_ modulo size to ensure it falls within the desired range.

built_in_hash() \
Resources: 
https://www.codecademy.com/resources/docs/python/built-in-functions/hash
https://ioflood.com/blog/python-hash/

This function calculates a hash value for an object using the object's __hash__() method. 
The object can be numbers, strings, tuples, or custom objects that have implemented the __hash__() method. 
Strings: Hashes the string's characters using a polynomial rolling hash function.
Integers: Returns the integer value as its hash value. 
Tuples: Combines the hash values of its elements using a combination of bitwise XOR and addition.
So, the hash value is computed using specific hashing algorithms based on the object’s type.

sha256_hash()\
Resource: https://www.educative.io/answers/what-are-the-different-steps-in-sha-256

Returns a hexadecimal number of 64 digits
It involves adding bits to ensure input data is a multiple of 64 bytes.
The padded data is divided into 64-byte chunks, processed using a series of bitwise operations (AND, OR, XOR, ROTATE, etc.), and mixed with constants and variables to produce a 256-bit hash value.
The hash value is further mixed and transformed to produce the final 256-bit SHA-256 hash value.

The key propertes all these function share are:
- Given the same input, they always produce the same output hash value.
- All the functions produce a different output to their input in a consistent way. 
- It is infeasible to produce the input given the output. 


# What are the advantages and disadvantages of each of the above hash functions?

## ssh()

Advantages:\
Determinism - This function consistently returns the same output for a given input

Disadvantages:\
uniformity - since the functions returns 1 for every input, there is no probability that any given input distrubutes over a range of possible hash values.

collision resistance - The function has no collision resistance as every input collides with every other input

sensitivity to input changes - Altering the input has no effect on the output, so it is not sensitive to input changes.

security - Outputs are not random and are predictable. 

efficiency - While this function doesn't perform any actual hashing or transformation (it just ignores the input and returns 1), it's time complexitity is constant and is fast to compute. However, in the context of hash functions, efficiency implies a balance between computational speed and utilization of the architecture of the computer effectively, while maintaining things like collision resistance and uniformity. This function doesn't really balance coll.resistance and uniformity, I'd say the effieciency of this function is a disadvantage since it balances too much on speed and not the security aspect.

## sum_of_ascii_values() 

Advantages:\
Determinism- always returns the same output for a given input

Sensitivity to Input Changes: modifying characters affects the sum so it is sensitive to input changes

Disadvantages:\
Uniformity - May not distribute outputs uniformly e.g. given the same size, for inputs "abc" and "bca"  they both return 4.

Collision Resistance - low collision resistance due to two inputs producing equal sums

Security - it is computationally feasible to find an input key that produces a specific hash because the function itself is simple and there is still a high chance of a hash collision for many inputs.

Effieciency - While the computational speed is high due to simple operations (sum, ord), in the context of hash functions, this function is not considered effecient because it lacks effective utilization of computer architecture, collision resistance and uniformity.

## pearson_hash()
Resources: https://www.epaperpress.com/vbhash/download/p677-pearson.pdf


Advantages:\
uniformity - produces a relatively uniform distribution of hash values. "Of the 26,662 inputs of dictionary words after hashing a tallying the result 0-255, "the resulting 256 counts were not all equal, but they are not alarmingly uneven".

determinism - produces the same hash value for a given input.

efficiency - this function is fast to compute and utilizes the architecture of the computer effectively

sensitivity to input changes - small changes in the input produce large changes in the output.

security - In the context of using this function for hash tables, the randomness and unpredictability provides reasonable security. 

Disadvantages:\
Collision resistance - each input has a result between 0 and 255. for larger input sets, the probability of collision gets higher


## built_in_hash()
Resource: https://realpython.com/python-hash-table/

uniformity - while not perfect, the built-in function is good at distributing hash values

efficiency - calculating a hash value is fast to compute even for very big inputs

sensitivity to input changes - small changes in the input produce large changes in the output.

security -  the output appear random and it is infeasible to find an input key from the hash

determinism - At first, when i ran the code, the hash value is different when invoked each time, so I thought it was non-determistic, a common error as talked about in the resources.
```
print(built_in_hash('hello',10))
8
```
```
print(built_in_hash('hello',10))
9
```
This is because the function applies a random seed. This was implemented in python for security and it is possible to disable randomization, though, by setting a fixed seed value.

In the resources i've looked at, the hash() function is indeed determinitic because hash values are immutable and don’t change throughout an object’s lifetime

When you call hash() with the same argument within an existing interpreter session, then you’ll keep getting the same result:
```
print(built_in_hash('hello',10))
print(built_in_hash('hello',10))
print(built_in_hash('hello',10))
1
1
1
```

collision resistance - because the hashes are somewhat uniformly distributed, there is a high collision resistance. Though as the sets get larger, collisions are a unavoidable. 

Disadvantages 
none

## sha256_hash()

Advantages:\
determinism - A given input will always produce the same output.

collision Resistance - Low probability of collisions.

sensitivity to input changes - A small change will completely change the output.

security -  Computationally infeasible to find an input key that produces a specific hash value and output hash values appear random and unpredictable.

uniformity - The outputs are uniformly distibuted and the probability of any given hash value within the range of possible hash values should be approximately equal.

Resource:
https://hackmd.io/@mcaradec/hash_distribution

efficiency -  SHA-256 requires lots of steps including padding and 64 rounds of operations, which can be computationally expensive for very large datasets, however modern CPUs can compute SHA-256 relatively quickly. Not sure but i'd say this function is efficient.  


Disadvantages:\
none

# List the three most important attributes (arranged from most to least) in the context of a hash map? Justify your answer.
Resources: https://medium.com/@Faris_PY/hash-map-in-python-collision-load-factor-rehashing-1484ea7d4bc0
1. The hashing function, which determines the index where the value can be found. The function ensures uniform distribution of values minimizing hash collisions.
2. The Load Factor, which is defined as m/n where m is the number of elements that can be occupied in the hashmap before incrementing its size and n is the size of the hashmap.
Load factor is important because it is a measure that decides when to increase the size of the hashmap to maintain the searching & insertion as low as possible O(1).
3. Collision handling - When inserting data and a key is already being occupied, a collision occurs, and they can be handled using methods such as separate chaining and open addressing.  

# Which of the above hash functions would you choose to implement the requirements of the task? Why?
I chose not to use:
* ssh() had all the index go to 1, so not a good hashing function. 
* sum_of_ascii_values() has a higher chance of collisions and there could be an uneven distribution of indexes.
* sha256() does offer a high security, but the number of hashing operations and it's very large output is over the scope for my needs and could use more memory than needed.

It came down to the pearson_hash() and built_in_hash(). Both are suitable and generate enough randomness but I've decided to choose the pearson_hash because built_in_hash() generates a random seed each run time, producing a different output. 
While I can  disable randomization by setting a fixed seed value through the PYTHONHASHSEED, I'd have to set the seed in the command line first:
```
PYTHONHASHSEED=1 python some_script.py
```
While its possible, if I were to have others use/review my code, they'd also have to use the same seed and run that command in their terminal which is a bit more inconvenient.

I'm going to use the pearson hash because my PlayerHashMap doesn't require that much security when hashing the keys and while the chance of collisions are higher than the built_in, it is more convenient and generates enough randomness to fit my needs.
# In your own words, explain each line in the pearson hash function above in terms of the criteria you listed in question 2.
```
import random

random.seed(42)
```
The first line import that random module to generate random numbers. The second line sets the seed to ensure a predictable sequence of random numbers when random.randdint is called.
This helps achieve determinism because the pearson_table will always be the same with a fixed seed.

```
pearson_table = [random.randint(0, 255) for _ in range(256)]
```
This line creates a table of 256 random values between 0 and 255. These values will be used in the hashing process.
This helps achieve Uniformity because each hash value has an equal chance of being produced.

```
def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
```
setting the hash_ to 0 initializes the first value to be used to XOR with.  This helps achieve determinism, as it sets the starting point for the hash calculation.

```
for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
```
This is main operation of the hashing algorithm. The first line starts to iterate through each character in the input string. ord() converts the character to ASCII value. The initial value (0) is then XOR'd with that character. The result of that operation gives an index to look up in the pearson table. The value  in that index is then used as the next hash_ value to be XOR'd with the next character's ASCII  value.\
This helps achieve criteria for sensitivity for input changes and security, because a change in any character remaps to an entirely different index during the loop. This will cause an avalanche effect as the value produced will remap to even more different indexes as the loop continues.

```
    return hash_ % size
```
This line returns the final hashed value. But because we want the value to be in specific range (depending on the size of the hash table), a modulo operation  is performed. 

# Write pseudocode of how you would store Players in PlayerLists in a hash map.
1. Initialize the hashmap as a list of PlayerLists with SIZE (number of PlayerLists)
2. Implement a hash function in the Player class that returns an index
3. in the HashMap class, create a method that will:
4. take a 'key' and 'name' as strings 
5. create a new PlayerNode with the key as the uid and name as player_name 
6. hash the key using the hash function get an index 
7. the index will correspond to a Playerlist position in the hashmap 
8. FOR each node of that PlayerList (doubly linked list)\
IF a node's uid is equal to the key, replace the name\
ELSE insert the new node to the tail of the PlayerList


# Reflection
The most challenging for me was researching and learning about the key dimensions of hash functions.
It was challenging as well to categorize as an advantage or disadvantage e.g. the efficiency of the hash function. Because most modern computers can all process the functions quickly, they are all efficient.

Efficiency would matter as the data sets get larger but there is not a lot of research out there on which function performs better. Not that I could find.

# If you didn't have to use a PlayerList, how would you have changed them implementation of the hash map and why?
instead of PlayerLists, I'd use python's built in data type - dictionary {}
```
class HashMap:
    def __init__(self):
        self.hashmap = {}
```
to store a player, the key would the uid and the value would be the name:
```
def put(self, key, name):
    self.hashmap[key] = name
```
I learned that the python dictionary hashes the key using python built in ```hash``` function.

Originally, i thought to use Arrays. So the hashmap would be an array(hashmap) of arrays(buckets) of arrays(uid, name). Both of these are changeable/mutable whilst sets and tuples are not.
The reason i chose dictionaries over arrays:
* dictionaries have built-in hash() function to hash keys
* automatic collision handling 

