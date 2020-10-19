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

def time_function(func):
    return time_lambda(lambda: func(coordinates, box_point_1, box_point_2))



assert testgeos_cpp.filter(coordinates, box_point_1, box_point_2) == EXPECTED

assert testgeos_pygeos.filter(coordinates, box_point_1, box_point_2) == EXPECTED
assert testgeos_pygeos.filter_via_lib(coordinates, box_point_1, box_point_2) == EXPECTED
assert testgeos_pygeos.filter_pregenerated(np_coordinates, polygon) == EXPECTED

assert testgeos_pygeos_c.filter_pregenerated(np_coordinates, polygon) == EXPECTED
assert testgeos_pygeos_c.filter(coordinates, box_point_1, box_point_2) == EXPECTED




print('Timing average time:')
print('* GEOS and CPP:', time_function(testgeos_cpp.filter))
# print('* PYGEOS:', time_function(testgeos_pygeos.filter))
print('* PYGEOS via lib:', time_function(testgeos_pygeos.filter_via_lib))
print('* PYGEOS via GEOS_C:', time_function(testgeos_pygeos_c.filter))

print('* PYGEOS pregenerated via lib:', time_lambda(
    lambda: testgeos_pygeos.filter_pregenerated(np_coordinates, polygon)
))
print('* PYGEOS pregenerated via GEOS_C:', time_lambda(
    lambda: testgeos_pygeos_c.filter_pregenerated(np_coordinates, polygon)
))



