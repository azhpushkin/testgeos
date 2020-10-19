import testgeos_cpp
import testgeos_pygeos
from timeit import timeit

box_point_1 = (12.3046875, 52.90890204777026) 
box_point_2 = (14.4140625, 52.05249047600099)

coordinates = []
with open('coords.txt') as file:
    for line in file:
        coords = line.rstrip().split(' ')
        coordinates.append((float(coords[0]), float(coords[1])))

print('Total coordinates:', len(coordinates), '\n')

def time_function(func):
    RUNS = 20
    total_time = timeit(lambda: func(coordinates, box_point_1, box_point_2), number=RUNS)
    return total_time / RUNS

EXPECTED = 5423
assert testgeos_cpp.filter(coordinates, box_point_1, box_point_2) == EXPECTED
assert testgeos_pygeos.filter(coordinates, box_point_1, box_point_2) == EXPECTED
assert testgeos_pygeos.filter_via_lib(coordinates, box_point_1, box_point_2) == EXPECTED

print('Timing average time:')
print('* GEOS and CPP:', time_function(testgeos_cpp.filter))
print('* PYGEOS:', time_function(testgeos_pygeos.filter))
print('* PYGEOS via lib:', time_function(testgeos_pygeos.filter_via_lib))



