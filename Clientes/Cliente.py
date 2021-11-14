"""
Este módulo codifica un único tipo de cliente.
El cliente se caracteriza por su DNI y su Cuenta Bancaria.
"""


from Identificadores.DNI import DNI
from Cuentas.CuentaBase import CuentaBase


class Cliente:
    """
    Clase que modela los clientes de un banco
    """

    def __init__(self, dni: DNI, cuenta: CuentaBase):
        """
        Constructor de clientes de un banco.

        :param dni: Documento identificativo.
        :param cuenta: Cuentas del banco.
        """

        self.__dni: DNI = dni
        self.__cuenta: CuentaBase = cuenta

    def _metodo_oculto(self):
        """
        Un método oculto para poner a prueba a Sphinx
        """
        print("Estoy oculto.", self.__dni)

    def __str__(self):
        """
          Generara un string legible sobre los objetos Clientes

          :return: un string
          """

        return "\n\n::Los datos del cliente son::\n" + str(self.__dni) + "\n" + str(self.__cuenta) + "\n"


if __name__ == "__main__":
    """Test"""
    cliente = Cliente(DNI("un nombre", "una dirección", 30), CuentaBase(500))
    print(cliente)
