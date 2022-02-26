import matplotlib.pyplot as plt
import csv


constants = [63.89645429018863, 64.29347252996023, 76.6009590897868, 55.93195802489479, 70.6424099424515]
home24 = [40.55, 40.38, 33.40, 35.81, 46.12]
home27 = [40.75, 40.63, 33.26, 35.38, 46.21]
places = ["seattle", "omaha", "scranton", "barry", "liverpool"]
count = 0
for item in home24:
    print(f"{places[count]} in 2024: {round(item * constants[count] / 100, 2)}")
    count += 1
print("")
count = 0
for item in home27:
    print(f"{places[count]} in 2027: {round(item * constants[count] / 100, 2)}")
    count += 1


