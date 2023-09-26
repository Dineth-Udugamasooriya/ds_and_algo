# Python program to demonstrate working of HashTable 

hashTable = [[],] * 10

def checkPrime(n):
    if n == 1 or n == 0:
        return 0

    for i in range(2, n//2):
        if n % i == 0:
            return 0

    return 1


def getPrime(n):
    if n % 2 == 0:
        n = n + 1

    while not checkPrime(n): #In each iteration of the while loop, the value of n is incremented by 2. This is because even numbers greater than 2 cannot be prime, so we only need to check odd numbers.
        n += 2

    return n


def hashFunction(key):
    capacity = getPrime(10)
    return key % capacity


def insertData(key, data):
    index = hashFunction(key)
    hashTable[index] = [key, data]

def removeData(key):
    index = hashFunction(key)
    hashTable[index] = 0

#search function
def searchData(key):
    index = hashFunction(key)
    if hashTable[index] and hashTable[index][0] == key:
        return hashTable[index][1]
    else:
        return None

insertData(123, "apple")
insertData(432, "mango")
insertData(213, "banana")
insertData(654, "guava")

print(hashTable)

result = searchData(213)
if result is not None:
    print("Found:", result)
else:
    print("Key not found")


removeData(123)

print(hashTable)