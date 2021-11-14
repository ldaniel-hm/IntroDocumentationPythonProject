"""
Modulo Principal del Proyecto

Este programa es un ejemplo de cómo usar la asociación y la herencia.
"""

from Identificadores.DNI import DNI
from Clientes.Cliente import Cliente
from Cuentas.CuentaBase import CuentaBase
from Cuentas.CuentaTipo.CuentaCredito import CuentaBaseCredito
from Cuentas.CuentaTipo.CuentaAhorro import CuentaBaseAhorro


if __name__ == "__main__":
    luis: Cliente = Cliente(DNI("Luis", "Murcia", 30), CuentaBase(500))
    daniel: Cliente = Cliente(DNI("Daniel", "Cartagena", 24), CuentaBaseAhorro(100, 2))
    juan: Cliente = Cliente(DNI("Juan", "Jaén", 45), CuentaBaseCredito(300, 2000))
    print(luis, daniel, juan)
