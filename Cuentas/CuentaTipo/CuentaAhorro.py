"""
Las cuentas de ahorro se caracterizan porque generan intereses a partir de cierta cantidad.
"""

from Cuentas.CuentaBase import CuentaBase


class CuentaBaseAhorro(CuentaBase):
    """
    Clase para manipular Cuentas de Ahorro
    """

    def __init__(self, cantidad, interes):
        """
        Constructor de cuentas de ahorro

        :param cantidad: Cantidad de inicio
        """
        super().__init__(cantidad)
        self._interes = interes

    def __str__(self):
        """
        Generara un string legible sobre los objetos cuenta

        :return: un string
        """
        return super().__str__() + "\n::El interés de la cuenta::" + str(self._interes)


if __name__ == "__main__":
    cuenta = CuentaBaseAhorro(200, 2)
    print("Inicialmente\n", cuenta)
    cuenta.depositar(100)
    print("Añado 100\n", cuenta)
    cuenta.retirar(300)
    print("Retiro 300\n", cuenta)
