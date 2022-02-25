import random
import matplotlib.pyplot as plt
import numpy as np


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

# plt.plot(x, y, "type and colour")
# "type and colour" e.g. "ro" means red circles, "b-" means a blue line and "b--" means a blue dashed line

def catergoric():
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