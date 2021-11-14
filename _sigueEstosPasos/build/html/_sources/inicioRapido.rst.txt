:index:`Inicio Rápido`
======================

Sphinx proporciona el script ``sphinx-quickstart`` para empezar a generar la documentación.

1. Crea la carpeta ``doc`` justo en la primera carpeta del proyecto

    ``documentationPythonProject > doc``

2. Abre un terminal y muévete a la carpeta ``doc`` con la instrucción  ``cd``.
3. Ejecuta el script ``sphinx-quickstart``::

    Bienvenido a la utilidad de inicio rápido de Sphinx 4.2.0.

    Ingrese los valores para las siguientes configuraciones (solo presione Entrar para
    aceptar un valor predeterminado, si se da uno entre paréntesis).

    Ruta raíz seleccionada: .

    Tiene dos opciones para colocar el directorio de compilación para la salida de Sphinx.
    O usas un directorio "_build" dentro de la ruta raíz, o separas
    directorios "fuente" y "compilación" dentro de la ruta raíz.
    > Separar directorios fuente y compilado (y/n) [n]:

    El nombre del proyecto aparecerá en varios lugares en la documentación construida.
    > Nombre de proyecto: Clientes y Cuentas
    > Autor(es): Pon tu nombre
    > Liberación del proyecto []: 0.1

    Si los documentos deben escribirse en un idioma que no sea inglés,
    puede seleccionar un idioma aquí por su código de idioma. Sphinx entonces
    traducir el texto que genera a ese idioma.

    Para obtener una lista de códigos compatibles, vea
    https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
    > Lenguaje del proyecto [en]: es

    Creando archivo ../documentationPythonProject/doc/conf.py.
    Creando archivo ../documentationPythonProject/doc/index.rst.
    Creando archivo ../documentationPythonProject/doc/Makefile.
    Creando archivo ../documentationPythonProject/doc/make.bat.

    Terminado: se ha creado una estructura de directorio inicial.

    Ahora debe completar su archivo maestro ../doc/index.rst y crear otros archivos fuente
    de documentación.Use el archivo Makefile para compilar los documentos, así ejecute el comando:
       make builder
    donde "builder" es uno de los constructores compatibles, por ejemplo, html, latex o linkcheck.


