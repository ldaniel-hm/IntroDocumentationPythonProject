:index:`Modificar Configuración e Índice Inicial`
=================================================

1. Editar el fichero ``conf.py`` (el fichero de configuración de la documentación) y cambia las líneas adecuadas con este contenido.::

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..')) # El lugar donde están los fuentes

    extensions = [
        'sphinx.ext.autodoc',    # docString de los .py
        'sphinx.ext.napoleon',   # Resaltar algunas palabras
        'sphinx.ext.viewcode',   # Mostrar el código fuente
    ]

    html_theme = 'sphinx_rtd_theme' # 'sphinxdoc' 'nature' 'alabaster'

2. Editar el fichero ``index.rst`` (el fichero de inicio de la documentación) y modificar el contenido a este otro.::

    .. toctree::
        :maxdepth: 2
        :caption: Contenidos:

        modules



