import csv
import matplotlib.pyplot as plt
import numpy as np

# csv is a library used to help open csv files, we used it to help read the data into a list
# matplotlib allows the flexible plotting of graphs using lists in python
# numpy allowed us to quickly generate lists of numbers of a specified range and interval


# Using Linear regression to find the formula for a line to fit the data
def find_a_coefficient(xMean, yMean, b):
    return yMean - b * xMean


def find_b_coefficient(n, xSum, ySum, xSquaredSum, xySum):
    sxy = xySum - (xSum * ySum) / n
    variance = xSquaredSum - (xSum ** 2) / n
    return sxy / variance

def central_values(data):
    n = len(data[0])
    xSum = 0
    ySum = 0
    xSquaredSum = 0
    xySum = 0
    for item in data[0]:
        xSum += item
        xSquaredSum += item ** 2
    for item in data[1]:
        ySum += item
    xMean = xSum / n
    yMean = ySum / n
    for number in range(n):
        xySum += data[0][number] * data[1][number]
    return n, xMean, yMean, xSum, ySum, xSquaredSum, xySum


colours = ["r", "g", "darkgreen", "c", "m", "y", "orange", "b", "indigo", "gray", "darkslategrey"]
# These are the values we calculated for the percent of workers that can
# work from home in each sector
sectorProportion = [0.31, 0.21, 0.013, 0.843, 0.783, 0.71, 0.355, 0.34, 0.563, 0.467]
places = ["seattle", "omaha", "scranton", "barry", "liverpool"]
expectedHome = []
for city in ["seattle", "omaha", "scranton", "barry", "liverpool"]:
    data = []
    expectedHome.append([])
    with open(f"{city}.csv") as csvfile:
        fileReader = csv.reader(csvfile, delimiter=",")
        for row in fileReader:
            data.append([])
            for item in row:
                try:
                    data[-1].append(int(item))
                except ValueError:
                    data[-1].append(item)

    count = -1
    # xVales = years for known data
    xValues = data[0][1:]
    # predictedX = years we want to predict
    predictedX = np.arange(2000, 2030, 1)
    # yValues = population data from data set 1
    yValues = [data[1:]]
    # yearPopulations = the total working population for each year
    yearPopulations = [0 for x in range(len(xValues))]
    for years in yValues[0]:
        for x in range(1, len(years)):
            yearPopulations[x - 1] += years[x]

    # Find the linear regression of the yearPopulations in order to predict populations
    # of future years
    n, xMean, yMean, xSum, ySum, xSquaredSum, xySum = central_values([xValues, yearPopulations])
    b = find_b_coefficient(n, xSum, ySum, xSquaredSum, xySum)
    a = find_a_coefficient(xMean, yMean, b)
    predictedPopulations = []
    for value in predictedX:
        predictedPopulations.append(round(b * value + a, 5))

    # set containing % of the population that can work from home
    final = [0 for x in range(len(predictedX))]

    # For each working sector
    for set in yValues[0]:
        count += 1
        # find the linear regression of the number of people in this sector
        n, xMean, yMean, xSum, ySum, xSquaredSum, xySum = central_values([xValues, set[1:]])
        b = find_b_coefficient(n, xSum, ySum, xSquaredSum, xySum)
        a = find_a_coefficient(xMean, yMean, b)
        predictedY = []
        # For each year we want to predict
        for year in range(len(predictedX)):
            # create a set of the predicted values for this sector based on the linear regression
            predictedY.append(round(b * predictedX[year] + a, 5))
            # Add the people in this sector that can work from home to the final value
            final[year] += predictedY[-1] * sectorProportion[yValues[0].index(set)]

    # Number of people ready to work from home / Total people working = % of working people ready to work from home
    for x in range(len(final)):
        final[x] /= predictedPopulations[x] / 100

    # Percentage of people working from home in 2020 / predicted % of jobs that are remote ready in 2020
    proportion = (37629 / 146254 * 100) / final[20] * 100
    # Calculate the expected % of people working from home each year after 2022 up to 2030
    for item in final[22:]:
        expectedHome[-1].append(round(item * proportion / 100, 2))


# Read in the values from spreadsheet 4 for the % of people working exclusively from home
# data[0] = years
# data[1] = % of people working exclusively from home
data = [[], []]
with open("expected.csv") as csvfile:
    fileReader = csv.reader(csvfile, delimiter=",")
    for row in fileReader:
        try:
            data[0].append(float(row[0]))
            data[1].append(float(row[1]))
        except ValueError:
            pass

# Plot these values from 2000 to 2021
plt.xlabel("Year")
plt.ylabel("% of Population working from home")
plt.title("% working population expected to work from home")
plt.plot(data[0], data[1], "r-", label="Known Percent of workers working from home")
# Plot the expected % of people working from home for each region
for x in range(5):
    plt.plot(np.arange(2022, 2030, 1), expectedHome[x], "--", color = colours[x], label=places[x])
plt.legend()
plt.show()

