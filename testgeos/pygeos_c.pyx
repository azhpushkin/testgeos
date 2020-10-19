
from pygeos.creation import points, box
from pygeos import lib
from pygeos.predicates import within


cdef void empty_handler(const char *s, ...) nogil:
    pass

cdef extern from "geos_c.h":
    cdef struct GEOSGeometry:
        pass
    
    ctypedef GEOSGeometry GEOSGeometry

    void initGEOS(void (const char *, ...) nogil, void (const char *, ...) nogil)
    void finishGEOS()

    # 2 - exception, 1 - true, 0 - false
    char GEOSWithin(GEOSGeometry* g1, GEOSGeometry* g2)



cdef class GeometryObject:
    cdef GEOSGeometry* ptr



def filter(coordinates, corner_1, corner_2):
    initGEOS(empty_handler, empty_handler)

    source_points = points(coordinates)
    polygon = box(*corner_1, *corner_2)

    cdef GeometryObject polygon_ptr = <GeometryObject>polygon
    cdef GeometryObject point_ptr
    
    cdef char res
    
    counter = 0
    for point in source_points:
        point_ptr = <GeometryObject>point
        res = GEOSWithin((point_ptr).ptr, (polygon_ptr).ptr)
        
        if res == 2:
            raise RuntimeError("Something went wrong!")
        elif res == 1:
            counter += 1
    
    finishGEOS()
    return counter


def filter_pregenerated(source_points, polygon):
    initGEOS(empty_handler, empty_handler)

    cdef GeometryObject polygon_ptr = <GeometryObject>polygon
    cdef GeometryObject point_ptr
    
    cdef char res
    
    counter = 0
    for point in source_points:
        point_ptr = <GeometryObject>point
        res = GEOSWithin((point_ptr).ptr, (polygon_ptr).ptr)
        
        if res == 2:
            raise RuntimeError("Something went wrong!")
        elif res == 1:
            counter += 1
    
    finishGEOS()
    return counter