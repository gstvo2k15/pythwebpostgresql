"""
Este módulo inicializa la aplicación y exporta las clases y funciones de module1 y module2.
"""

from .module1 import SomeClass, some_function
from .module2 import AnotherClass, another_function

__all__ = ['SomeClass', 'some_function', 'AnotherClass', 'another_function']

