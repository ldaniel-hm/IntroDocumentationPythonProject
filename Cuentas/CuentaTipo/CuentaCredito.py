"""
Las cuentas de crédito tienen un depósito disponible si te quedas sin dinero.
"""



from Cuentas.CuentaBase import CuentaBase


class CuentaBaseCredito(CuentaBase):
    """
    Clase para manipular Cuentas de Crédito
    """

    def __init__(self, cantidad, deposito):
        """
        Constructor de cuentas de ahorro

        :param cantidad: Cantidad de inicio
        """
        super().__init__(cantidad)
        self._deposito = deposito

    def __str__(self):
        """
        Generara un string legible sobre los objetos cuenta

        :return: un string
        """
        return super().__str__() + "\n::El depósito de la cuenta::" + str(self._deposito)


if __name__ == "__main__":
    cuenta = CuentaBaseCredito(200, 3000)
    print("Inicialmente\n", cuenta)
    cuenta.depositar(100)
    print("Añado 100\n", cuenta)
    cuenta.retirar(300)
    print("Retiro 300\n", cuenta)