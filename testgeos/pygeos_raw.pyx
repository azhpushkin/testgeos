
from pygeos.creation import points, box
from pygeos import lib
from pygeos.predicates import within


def filter(coordinates, corner_1, corner_2):
    source_points = points(coordinates)
    polygon = box(*corner_1, *corner_2)

    counter = 0
    for point in source_points:
        if within(point, polygon):
            counter += 1
    
    return counter


def filter_via_lib(coordinates, corner_1, corner_2):
    source_points = points(coordinates)
    polygon = box(*corner_1, *corner_2)

    counter = 0
    for point in source_points:
        if lib.within(point, polygon):
            counter += 1
    
    return counter


def filter_pregenerated(source_points, polygon):
    counter = 0
    for point in source_points:
        if lib.within(point, polygon):
            counter += 1
    
    return counter