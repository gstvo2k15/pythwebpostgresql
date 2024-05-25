"""
Este módulo contiene la clase AnotherClass y la función another_function.
"""

class AnotherClass:
    """
    Clase que contiene un nombre y puede saludar.
    """
    def __init__(self, name):
        self.name = name

    def greet(self):
        """
        Retorna un saludo utilizando el nombre almacenado.
        """
        return f"Hello, {self.name}!"

def another_function(a, b):
    """
    Multiplica dos valores y retorna el resultado.
    """
    return a * b

