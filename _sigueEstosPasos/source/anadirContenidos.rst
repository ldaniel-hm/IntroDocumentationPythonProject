:index:`Añadir y Quitar Contenidos`
-------------------------------------


En teoría no es necesario añadir más información sobre las clases, módulos o paquetes, pues todo lo que se muestra son los miembros públicos de cada módulo.

Pero ya que vuestro documento será evaluado, los profesores necesitamos saber cómo se han construido todas vuestras clases.
Para ello tendrás que añadir las siguientes directivas para :index:`mostrar los miembros privados`::

    :members:
    :private-members:

Por ejemplo, el fichero ``Clientes.Cliente.rst`` debes modificarlo con el siguiente contenido::

    Clientes.Cliente module
    -----------------------

    .. automodule:: Clientes.Cliente
       :members:
       :private-members:  # <<< Incluye esto
       :special-members:  # <<< Incluye esto
       :undoc-members:
       :show-inheritance:


Vuelve a ejecutar ``make clean html`` para comprobar cómo la información sobre Cliente.py ha cambiado.

Si tuvieras problemas usa la extensión Napoleon::

    extensions = [
        'sphinx.ext.autodoc',    # docString de los .py
        'sphinx.ext.napoleon',   # Resaltar algunas palabras
        'sphinx.ext.viewcode',   # Mostrar el código fuente
    ]

    # Napoleon settings
    napoleon_google_docstring = True
    napoleon_numpy_docstring = True
    napoleon_include_private_with_doc = True
    napoleon_include_special_with_doc = True
    napoleon_use_admonition_for_examples = True
    napoleon_use_admonition_for_notes = True
    napoleon_use_admonition_for_references = True
    napoleon_use_ivar = True
    napoleon_use_param = True
    napoleon_use_rtype = True

Para conocer más: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html


También deberías :index:`mostrar el enunciado` del ejercicio y
:index:`mostrar una explicación` de aquellos aspectos que se indiquen en los criterios de evaluación.
Todo esto tendrás que añadirlo en el fichero ``index.rst``. ::

    Documentación de  Clientes y Cuentas
    =====================================

    .. toctree::
        :maxdepth: 2
        :caption: Contents:

        enunciado   # Crea el fichero enunciado.rst con el enunciado.
        # Añade aquí cuantos ficheros .rst necesites. Haz pocos.
        # Es mejor una estructura jerárquica como los módulos.
        # proyecto.rst, proyecto.enunciado.rst, proyecto.niveles.rst, etc ...

        # A continuación pon la documentación de la API
        modules

También te puede interesar :index:`quitar contenidos`. Por ejemplo, de cada fichero .rst puedes quitar el siguiente
contenido que genera el script ``sphinx-apidoc``::

    Indices and tables
    ==================

    * :ref:`genindex`
    * :ref:`modindex`
    * :ref:`search`





