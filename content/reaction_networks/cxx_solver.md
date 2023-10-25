# C++ Solver for Stiff Nonlinear System

Here's an implementation of a first-order backward-Euler solver for
the same nonlinear stiff system.


This uses a two-dimensional multidimensional array class, ``Array`` defined
in the header ``array.H``.  This allows us to do things like:

```c++
Array A{{{1, 1, 1},
         {-1, 2, 0},
         {2, 0, 1}}};
```

to initialize a 2-d array.  We can then get the number of rows and
columns via ``A.nrows()`` and ``A.ncols()``.  We can also index the
array using ``A(i,j)`` to get the ``i``-th row and ``j``-th column.

Here's the class header ``array.H``:

```{literalinclude} ../../examples/cxx_stiff_network/array.H
:language: c++
```

The Gaussian elimination function is in the header ``gauss.H``:

```{literalinclude} ../../examples/cxx_stiff_network/gauss.H
:language: c++
```

and the full solver is in ``stiff_system.cpp``:

```{literalinclude} ../../examples/cxx_stiff_network/stiff_system.cpp
:language: c++
```

This can be compiled as:

```bash
g++ -std=c++17 -I. -o stiff_system stiff_system.cpp
```


