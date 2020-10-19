import testpygeos
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
    total_time = timeit(lambda: func(coordinates, box_point_1, box_point_2), number=100)
    return total_time / 100

EXPECTED = 5423
assert testpygeos.filter_via_geos_cpp(coordinates, box_point_1, box_point_2) == EXPECTED

print('Timing average time:')
print('* GEOS and CPP:', time_function(testpygeos.filter_via_geos_cpp))
# res = timeit.timeit(lambda: testpygeos.filter_via_geos_cpp(coordinates, box_point_1, box_point_2), number=20)

# print(res)


