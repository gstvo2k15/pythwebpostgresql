# app/__init__.py

from .module1 import SomeClass, some_function
from .module2 import AnotherClass, another_function

__all__ = ['SomeClass', 'some_function', 'AnotherClass', 'another_function']

