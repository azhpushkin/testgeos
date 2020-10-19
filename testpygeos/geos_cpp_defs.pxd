from libcpp.vector cimport vector
from libcpp.memory cimport unique_ptr
from libcpp cimport bool


"""
Declarations for Geos classes that are required to calculate centroids.
Only used methods are defined

TODO: worth thinking about changing GeometryFactory to accept SRID
https://geos.osgeo.org/doxygen/classgeos_1_1geom_1_1GeometryFactory.html#ae9099381789bdf714157906fdf1001a2
"""


cdef extern from "<geos/geom/Coordinate.h>" namespace "geos::geom":
    cdef cppclass Coordinate:
        double x
        double y
        double distance(const Coordinate& )


cdef extern from "<geos/geom/Point.h>" namespace "geos::geom":
    cdef cppclass Point:
        pass


cdef extern from "<geos/geom/CoordinateSequence.h>" namespace "geos::geom":
    cdef cppclass CoordinateSequence:
        pass


cdef extern from "<geos/geom/CoordinateSequenceFactory.h>" namespace "geos::geom":
    cdef cppclass CoordinateSequenceFactory:
        unique_ptr[CoordinateSequence] create(vector[Coordinate]* )

cdef extern from "<geos/geom/LinearRing.h>" namespace "geos::geom":
    cdef cppclass LinearRing:
        pass

        
cdef extern from "<geos/geom/Polygon.h>" namespace "geos::geom":
    cdef cppclass Polygon:
        double getArea()
        bool contains(Point*)
        Polygon* clone()


cdef extern from "<geos/geom/GeometryFactory.h>" namespace "geos::geom":
    cdef cppclass GeometryFactory:
        ctypedef unique_ptr[GeometryFactory] Ptr
        
        # Factory itself is created via factory ::create() method
        @staticmethod
        Ptr create()

        const CoordinateSequenceFactory* getCoordinateSequenceFactory()
        LinearRing* createLinearRing(CoordinateSequence*)
        Polygon* createPolygon(const LinearRing&, const vector[LinearRing*]&)
        Point* createPoint(Coordinate&)


