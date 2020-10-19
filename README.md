This repo contains several versions of the same code.
All versions take set of coordinates from coords.txt and count
amount of points that are inside of pre-defined box.

Check out `bench.py` to see details. Only filtering is timed.
`makefile` makes all the magic btw, but you need to install Cython and pygeos.

There are 4 versions, that use
* GEOS cpp API directly, via Cython .pxd file and library linkage. By far the biggest
in terms of code and compications due to manual memory management and factories fuss
* simple PyGEOS `within` usage
* simple PyGEOS, but with `pygeos.lib.within` instead of `pygeos.predicate.within`. 
This one is interesting, as such a small change gives guite a big improvement ( due to Cython
avoiding Python overhead).
* PyGEOS for creation of objects, but triggers GEOSWithin`` from libgeos_c directly with the pointers,
extracted from PyGEOS data structures


Here are results from timing this in seconds (`bench.py` is called, or just use `make`):
```
Timing average time:
* GEOS and CPP: 0.004923459050041856
* PYGEOS: 0.5081557491999774
* PYGEOS via lib: 0.3773863481499575
* PYGEOS with direct GEOS-C call: 0.10000255404993368
```


Some notes:
* I'm not sure memory management is 100% fine in CPP version now, but it seems legit enough
for test purposes
* There is no GEOSInit call in CPP version, which is strange. I suspect factories do that
inside, but did not verified it yet. However filtering works just fine.
* PYGEOS-GEOS-C version is several times faster that using PYGEOS wrappers. Probably
wrapping gives this overhead.
* `pygeos.creation.points` generates numpy array, but Cython uyses it as a plain
Python collection. Gonna try some hints and typedefs to use numpy C API, I think that can speed
things up a lot.
* CPP version is times ahead compared to other functions, no idea why it is SO significant.
My guess would be reusage of memory and static allocation for Coordinates, but I still think
it should not be SO crucial.