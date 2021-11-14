:index:`Generar la Documentación`
==================================

Sphinx proporciona el script ``sphinx-apidoc`` para generar los ficheros ``.rst`` de la documentación.
Cada fichero ``.rst`` se corresponde con un fichero ``.py`` de tu proyecto. Tendrás que ejecutar la siguiente instrucción.::

    sphinx-apidoc -f -e directorioProyecto -o directorioProyecto/doc


Lo mejor es usar trayectorias relativas.::

    sphinx-apidoc -f -e . -o doc/   # Si estamos en documentationPythonProject
    sphinx-apidoc -f -e .. -o .     # Si estamos en documentationPythonProject/doc


En nuestro ejemplo se generará lo siguiente.::

    ➜ sphinx-apidoc -f -e .. -o .
    Creando archivo ./main.rst.
    Creando archivo ./Clientes.rst.
    Creando archivo ./Clientes.Cliente.rst.
    Creando archivo ./Cuentas.rst.
    Creando archivo ./Cuentas.CuentaBase.rst.
    Creando archivo ./Cuentas.CuentasTipo.rst.
    Creando archivo ./Cuentas.CuentasTipo.CuentaAhorro.rst.
    Creando archivo ./Cuentas.CuentasTipo.CuentaCredito.rst.
    Creando archivo ./Identificadores.rst.
    Creando archivo ./Identificadores.DNI.rst.
    Creando archivo ./modules.rst.

Cada vez que modifiques un fichero ``.py`` deberá de usar el script ``sphinx-apidoc``.

Generados los ficheros ``.rst`` generamos la documentación HTML, LaTeX, ...::

    make clean html

El primer parámetro limpiar el contenido del directorio ``build`` el segundo lo que hace es generar la documentación en formato HTML.


