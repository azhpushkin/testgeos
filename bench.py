import testgeos_cpp
import testgeos_pygeos
import testgeos_pygeos_c
from timeit import timeit

from pygeos.creation import points, box


# This is a pre-defined set of coordinates and polygon for filtering

coordinates = []
with open('coords.txt') as file:
    for line in file:
        coords = line.rstrip().split(' ')
        coordinates.append((float(coords[0]), float(coords[1])))

box_point_1 = (12.3046875, 52.90890204777026) 
box_point_2 = (14.4140625, 52.05249047600099)
EXPECTED = 5423

np_coordinates = points(coordinates)
polygon = box(*box_point_1, *box_point_2)

print('Total coordinates:', len(coordinates), '\n')

def time_lambda(lmbda):
    RUNS = 20
    total_time = timeit(lmbda, number=RUNS)
    return total_time / RUNS

def time_pygeos(func):
    return time_lambda(lambda: func(np_coordinates, polygon))



assert testgeos_cpp.filter(coordinates, box_point_1, box_point_2) == EXPECTED

assert testgeos_pygeos.filter(np_coordinates, polygon) == EXPECTED
assert testgeos_pygeos.filter_via_lib(np_coordinates, polygon) == EXPECTED

assert testgeos_pygeos_c.filter(np_coordinates, polygon) == EXPECTED




print('Timing average time:')
print('* GEOS and CPP:', time_lambda(lambda: testgeos_cpp.filter(coordinates, box_point_1, box_point_2)))
print('* PYGEOS:', time_pygeos(testgeos_pygeos.filter))
print('* PYGEOS via lib:', time_pygeos(testgeos_pygeos.filter_via_lib))
print('* PYGEOS (scalar objects) with GEOS-C:', time_pygeos(testgeos_pygeos_c.filter))
