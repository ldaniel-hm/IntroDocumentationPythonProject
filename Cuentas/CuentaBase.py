"""
Este módulo codifica una cuenta bancaria simple.
Realmente debería ser una clase abstracta.
"""


class CuentaBase:
    """
    Clase para manipular Cuentas en general ¿Debería ser abstracta? ¿En qué métodos?
    """

    def __init__(self, cantidad):
        """
        Constructor de cuentas

        :param cantidad: Cantidad de inicio
        """
        if cantidad < 0:
            cantidad = 0

        self._cantidad = cantidad

    def depositar(self, cantidad):
        """
        Ingresar dinero en la cuenta

        :param cantidad:  Una cantidad positiva
        """
        assert cantidad > 0, "Valor incorrecto"
        self._cantidad += cantidad

    def retirar(self, cantidad):
        """
        Retirar dinero en la cuenta

        :param cantidad:  Una cantidad positiva
        """
        assert cantidad > 0, "Valor incorrecto"
        self._cantidad -= cantidad

    def __str__(self):
        """
        Generará un string legible sobre los objetos cuenta

        :return: un string
        """
        return "::La cantidad de la cuenta::" + str(self._cantidad)


if __name__ == "__main__":
    """Test"""
    cuenta = CuentaBase(200)
    print("Inicialmente", cuenta)
    cuenta.depositar(100)
    print("Añado 100", cuenta)
    cuenta.retirar(300)
    print("Retiro 300", cuenta)
