:index:`Corregir Enlaces`
==========================


Es posible que obtengas un WARNING (aviso) de que ciertos ficheros no se están documentando.
En nuestro proyecto el aviso lo tendrás para el fichero ``Cuentas.CuentasTipos.rst``.

Tendrás entonces que modificar alguno de los ficheros .rst para :index:`incluir ficheros faltantes`.
En nuestro ejemplo, ``Cuentas.CuentasTipos.rst`` se corresponde al contenido de la carpeta
``Cuentas.CuentasTipos``, por lo que modificaremos el contenido del fichero ``Cuentas.rst``::

    Cuentas package
    ===============

    Submodules
    ----------

    .. toctree::
        :maxdepth: 4

        Cuentas.Cuenta
        Cuentas.CuentasTipos

Observa que solo se ha añadido la última línea (el aviso del Warning).

Ejecuta ``make clean html`` quitando y añadiendo la última línea para que veas las diferencias.

---

Es muy posible que para cada fichero .rst tampoco te interese el siguiente contenido.::

    Module contents
    ---------------

    .. automodule:: Clientes
        :members:
        :undoc-members:
        :show-inheritance:

En el ejemplo, este contenido lo encontramos en Clientes.rst, Cuentas.rst, ... Puedes :index:`quitar` esas líneas.
