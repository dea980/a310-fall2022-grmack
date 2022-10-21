# To install numpy, type in terminal (or cmd):
# pip install numpy
# pip3 install numpy

import numpy as np 

# Basic two-dimensional array arithmetic

a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
# b = np.array([[1, 2], [3, 4]])
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(a+b)
# print(a * b)
# print(a - b)

# Functions

# print(np.max(c)) #8
# print(np.min(c)) #1
# print(np.average(a)) #2.0

# 3-4 Taxation problem

alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]

salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                    [0.4, 0.5, 0.5],
                    [0.1, 0.2, 0.1]])

# one-liner
# print(salaries - salaries * taxation)
max_income = np.max(salaries - salaries * taxation)

# Working with NumPy Arrays: Slicing, Broadcasting and Array Types

mylist = [1, 2, 3, 4, 5]

a = np.array([55, 56, 57, 58, 59, 60, 61])

#a[:-1] # every element of the array except the last
#a[1] # first element
#a[:] # array
# print(a[::2])

a = np.array([[0, 1, 2, 3],
 [4, 5, 6, 7],
 [8, 9, 10, 11],
 [12, 13, 14, 15]])


# print(a[:, 1:])
#[[ 1  2  3]
# [ 5  6  7]
# [ 9 10 11]
# [13 14 15]]

a = np.array([1, 2, 3, 4])
# print(a.ndim) #1
# a.shape #(4,)
b = np.array([[2, 1, 2], [3, 2, 3], [4, 3, 4]])
# print(b.ndim) #2
# b.shape # (3, 3)

# print(a.shape)
# print(b.shape)

dataScientist =     [130, 132, 137]
productManager =    [127, 140, 145]
designer =          [118, 118, 127]
softwareEngineer =  [129, 131, 137]

employees = np.array([dataScientist, productManager, designer, softwareEngineer])

## One-liner
# print(employees[0,::2])
# print(employees[0, ::2] * 1.1)
employees[0,::2] = employees[0,::2] * 1.1
# [130, 137] * 1.1
# [130, 137] * [1.1, 1.1]


# Conditional Array Search, Filtering, and Broadcasting to Detect Outliers

X = np.array([[1, 0, 0], [0, 2, 2], [3, 0, 0]])
# print(np.nonzero(X))
# (array([0, 1, 1, 2], dtype=int64), array([0, 1, 2, 0], dtype=int64))
# print(X == 2)

X = np.array([
 [ 42, 40, 41, 43, 44, 43 ],    # Hong Kong
 [ 30, 31, 29, 29, 29, 30 ],    # New York
 [ 8, 13, 31, 11, 11, 9 ],      # Berlin
 [ 11, 11, 12, 13, 11, 12 ]])   # Montreal
cities = np.array(["Hong Kong", "New York", "Berlin", "Montreal"])

# One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

#print(np.average(X)) #24.333333333333332
# print(np.nonzero(X > np.average(X))) 
# (array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2], dtype=int64), array([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 2], dtype=int64))
# print(np.nonzero(X > np.average(X))[0]) # [0 0 0 0 0 0 1 1 1 1 1 1 2]
# print(cities[np.nonzero(X > np.average(X))[0]])

# print(polluted)

# Boolean Indexing to Filter Two-Dimensional Arrays
inst = np.array([[232, "@instagram"],
                [133, "@selenagomez"],
                [59, "@victoriassecret"],
                [120, "@cristiano"],
                [111, "@beyonce"],
                [76, "@nike"]])

# One-liner
superstars = inst[inst[:, 0].astype(float) > 100, 1]

# print(inst[:,0]) # ['232' '133' '59' '120' '111' '76'], they are not floats/int
# print(inst[:,0].astype(float)) # [232. 133.  59. 120. 111.  76.], now they are floats

# print(superstars)


# Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element
a = np.array([4] * 10)
# print(a) # [4 4 4 4 4 4 4 4 4 4]

a[1::] = [42] * 9 
# print(a) #[ 4 42 42 42 42 42 42 42 42 42]

a = np.array([1, 2, 3, 4, 5, 6])
# One-dimensional, [1, 2, 3, 4, 5, 6]

# Two-dimensional, [[1, 2, 3] [4, 5, 6]]
# print(a.reshape(2, 3))

solar_x = np.array([[1, 2, 3], [2, 2, 5]])
# print(np.average(solar_x, axis=0))

tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                      5, 3, 3, 4, 3, 4, 6,
                      6, 5, 5, 5, 4, 5, 5])

## One-liner
tmp[6::7] = np.average(tmp.reshape((-1,7)), axis=1)

# print(tmp.reshape(-1, 7)) 

# print(tmp.reshape(-1, 7))

# When to use the sort() function and when to use the argsort() function in numpy

a = np.array([10, 6, 8, 2, 5, 4, 9, 1])

# print(np.sort(a)) # [ 1  2  4  5  6  8  9 10]
# print(np.argsort(a)

a = np.array([[1, 6, 2],
            [5, 1, 1],
            [8, 0, 1]])

# print(np.sort(a, axis = 0))

sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(["John", "Bob", "Alice", "Joe", "Jane", "Frank", "Carl"])

# One-liner
top_3 = students[np.argsort(sat_scores)][:-4:-1]

#print(np.argsort(sat_scores))
#print(students[np.argsort(sat_scores)]) # Ascending order [Jane, Joe, ..., Frank, Alice]

#print(students[np.argsort(sat_scores)][:-4:-1]) 
# print(top_3)


# How to use Lambda Functions and Boolean Indexing to Filter Arrays
books = np.array([['Coffee Break NumPy', 4.6],
                ['Lord of the Rings', 5.0],
                ['Harry Potter', 4.3],
                ['Winnie-the-Pooh', 3.9],
                ['The Clown of God', 2.2],
                ['Coffee Break Python', 4.7]])

# One-liner 
predict_bestseller = lambda x, y: x[x[:,1].astype(float) > y]

# lambda x, y: 
    # x[x[:,1].astype(float) > y]

# print(predict_bestseller(books, 3.9))


# How to Create Advanced Array Filters with Statistics, Math, and Logic
import matplotlib.pyplot as plt 
                            #mean, sd  n
sequence = np.random.normal(10.0, 1.0, 500)
# print(sequence)

# plt.xkcd()
# plt.hist(sequence)
# plt.savefig("plot.jpg")
# plt.show()

# Absolute value function
a = np.array([-1, 1, -2, 2])
# print(np.abs(a)) # 1, 1, 2, 2

a = np.array([True, True, False, False])
b = np.array([True, False, True, False])

#print(np.logical_and(a, b)) # True, False, False, False
#print(np.logical_or(a, b)) # True, True, True, False

# col = users, bounce, duration
a = np.array([  [815, 70, 115],
                [767, 80, 50],
                [912, 74, 77],
                [554, 88, 70],
                [1008, 65, 128]])

mean = np.mean(a, axis=0)
stdev = np.std(a, axis=0)

print(f"mean: {mean}, sd: {stdev}")

# One-liner
outliers = (
    (np.abs(a[:,0] - mean[0]) > stdev[0])
 * (np.abs(a[:,1] - mean[1]) > stdev[1])
 * (np.abs(a[:,2] - mean[2]) > stdev[2])
 )

print((np.abs(a[:,0] - mean[0]) > stdev[0])) # False False False True True
print(np.abs(a[:,1] - mean[1]) > stdev[1])   # False False False True True
print((np.abs(a[:,2] - mean[2]) > stdev[2])) # False True False False True

# print(outliers) False, False, False, False, True
# print(a[outliers]) # [[1008   65  128]]


