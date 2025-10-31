"""
GeoLIPI: A DSL for Implicit Geometric Modelling

GeoLIPI is a domain-specific language for modeling 2D and 3D geometric objects
using implicit representations (signed distance fields). It provides:

- A symbolic layer for defining geometric primitives and operations
- Multiple execution backends (PyTorch, Blender Geometry Nodes)
- Support for procedural geometry generation and parameterized designs

Main subpackages:
    - geolipi.symbolic: Symbolic DSL for geometric expressions
    - geolipi.torch_compute: PyTorch-based execution engine
    - geolipi.geometry_nodes: Blender integration via geometry nodes

Example:
    >>> import geolipi.symbolic as gls
    >>> from geolipi.torch_compute import recursive_evaluate
    >>>
    >>> # Create a simple 2D circle
    >>> circle = gls.Circle2D(radius=1.0)
    >>>
    >>> # Evaluate on a grid
    >>> result = recursive_evaluate(circle, canvas_width=512)
"""

__version__ = "0.1.0"
__author__ = "Aditya Ganeshan"
__license__ = "MIT"

# Make version available at package level
__all__ = ["__version__", "__author__", "__license__"]
