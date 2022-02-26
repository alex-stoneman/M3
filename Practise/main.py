import random
import matplotlib.pyplot as plt
import numpy as np
import math


# SIR - Information spread over time
# Linear fit
# Gaussian Fit


def blobs():
    # Uses numpy arrays to define position, size and colour of circles with relation to the normal distribution
    # np.arrange(low, high, increment)
    # np.random.randn(number of items in the list randomly taken from the normal distribution)
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100
    # plt.scatter(x, y, colours, size, ?)
    plt.scatter('a', 'b', c='c', s='d', data=data)
    plt.xlabel('entry a')
    plt.ylabel('entry b')
    plt.show()


def equation(x):
    # one way to implement an equation
    return -1 * x ** 2 + 100

def regular():
    # plt.plot(x, y, "type and colour")
    # "type and colour" e.g. "ro" means red circles, "b-" means a blue line and "b--" means a blue dashed line
    plt.plot([2,7,3,9], [5, 72, 2, 8], "r--")
    yValues = []
    for x in range(9):
        yValues.append(equation(x))
    plt.plot(yValues, "bo")
    plt.show()


def categoric():
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]
    plt.figure(figsize=(9, 3))
    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()


def gaussian_curve(set, x):
    sum = 0
    squareSum = 0
    n = len(set)
    for number in set:
        sum += number
        squareSum += number ** 2
    mean = sum / n
    variance = (squareSum - n * mean ** 2) / (n - 1)
    a = max(set)
    b = set.index(a) - 10
    c = math.sqrt(variance)
    return 100 - a * np.exp(-((x - b) ** 2) / (2 * (c ** 2)))


def gaussian_attempt():
    xValues = np.arange(-10, 10, 1)
    set = []
    for x in xValues:
        set.append(equation(x))
    plt.plot(xValues, set, "ro")
    newSet = []
    for x in set:
        newSet.append(gaussian_curve(set, x))
    plt.plot(xValues, newSet, "b-")
    plt.show()


def pure_gaussian(x):
    return 8 * np.exp(-((x - 4) ** 2) / (2 *67.2))


def more_gaussian():
    xValues = np.arange(-25, 25, 0.2)
    yValues = []
    for x in xValues:
        yValues.append(pure_gaussian(x))
    plt.plot(xValues, yValues, "b-")
    plt.show()

    gaussian_attempt()


def normailse(set):
    range = max(set) - min(set)
    newSet = []
    for item in set:
        newSet.append((item - min(set)) / range)

plt.plot([1, 2], "r-")
plt.show()
more_gaussian()