This repo contains several versions of the same code.
All versions take set of coordinates from coords.txt and count
amount of points that are inside of pre-defined box.

Check out `bench.py` to see details. Only filtering is timed.
`makefile` makes all the magic btw, but you need to install Cython and pygeos.


Here are results from timing this in seconds (`bench.py` is called, or just use `make`):
```
Timing average time:
Timing average time:
* GEOS and CPP: 0.004952797750047466
* PYGEOS: 0.010572109450004063
* PYGEOS via lib: 0.009557065700028034
* PYGEOS (scalar objects) with GEOS-C: 0.009862124800019956
```

