from libcpp.vector cimport vector
from libcpp cimport bool
from libcpp.memory cimport unique_ptr
from cython.operator cimport dereference

from geos_cpp_defs cimport (
    Coordinate, GeometryFactory, CoordinateSequenceFactory,
    CoordinateSequence, LinearRing, Polygon, Point
)


def filter(coordinates, corner_1, corner_2):
    # Create polygon, using factories and linear ring
    cdef vector[Coordinate]* points = new vector[Coordinate](5)
    dereference(points)[0].x = corner_1[0]
    dereference(points)[0].y = corner_1[1]
    dereference(points)[1].x = corner_1[0]
    dereference(points)[1].y = corner_2[1]
    dereference(points)[2].x = corner_2[0]
    dereference(points)[2].y = corner_2[1]
    dereference(points)[3].x = corner_2[0]
    dereference(points)[3].y = corner_1[1]
    dereference(points)[4].x = corner_1[0]
    dereference(points)[4].y = corner_1[1]

    cdef GeometryFactory.Ptr factory = GeometryFactory.create()
    cdef const CoordinateSequenceFactory* temp = dereference(factory).getCoordinateSequenceFactory()
    cdef unique_ptr[CoordinateSequence] seq = dereference(temp).create(points)

    cdef LinearRing* ring = dereference(factory).createLinearRing(seq.get())

    cdef vector[LinearRing*] empty_holes
    cdef Polygon* polygon = dereference(factory).createPolygon(dereference(ring), empty_holes)  # TODO: try null

    counter = 0
    cdef Coordinate coord_raw
    cdef Point* point
    cdef bool res
    for x, y in coordinates:
        coord_raw.x = x
        coord_raw.y = y

        point = dereference(factory).createPoint(coord_raw)
        res = dereference(polygon).contains(point) 
        del point
        if res:
            counter += 1
    
    del polygon
    return counter

