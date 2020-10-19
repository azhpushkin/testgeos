
from pygeos.creation import points, box
from pygeos import lib
from pygeos.predicates import within


def filter(np_coordinates, polygon):
    matches = within(source_points, polygon)
    
    return matches.sum()


def filter_batch(source_points, polygon):
    matches = lib.within(source_points, polygon)
    
    return matches.sum()