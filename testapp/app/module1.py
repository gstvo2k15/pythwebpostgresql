"""
Este módulo contiene la clase SomeClass y la función some_function.
"""

class SomeClass:
    """
    Clase que contiene un valor y puede mostrarlo.
    """
    def __init__(self, value):
        self.value = value

    def display_value(self):
        """
        Muestra el valor almacenado.
        """
        print(f"The value is: {self.value}")

def some_function(x, y):
    """
    Suma dos valores y retorna el resultado.
    """
    return x + y

