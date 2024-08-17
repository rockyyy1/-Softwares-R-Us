import hashlib
import random

random.seed(42)

pearson_table = [random.randint(0, 255) for _ in range(256)]


def ssh(key):
    return 1


def sum_of_ascii_values(key: str, size: int) -> int:
    return sum(ord(char) for char in key) % size


def pearson_hash(key: str, size: int) -> int:
    hash_ = 0
    for char in key:
        hash_ = pearson_table[hash_ ^ ord(char)]
    return hash_ % size


def built_in_hash(key: str, size: int) -> int:
    return hash(key) % size


def sha256_hash(key: str, size: int) -> int:
    return int(hashlib.sha256(key.encode()).hexdigest(), 16) % size


print(built_in_hash("helloo", 100))
