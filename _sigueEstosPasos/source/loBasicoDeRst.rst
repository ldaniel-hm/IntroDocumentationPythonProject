Escribir en reStructuredText
============================

Se dan unas nociones muy básicas sobre :index:`sintaxis del lenguaje` de marcas ``rst``

:index:`Estructura del documento`
---------------------------------

* Cabecera::

    El Título
    ---------

* Subcabecera (subtítulo o sección)::

    Subtítulo
    =========

* Subsubcabecera (sección o subsección)::

    Subsubtítulo
    ^^^^^^^^^^^^

* Párrafo::

    Una línea en blanco crea un párrafo nuevo.

    Inicio de otro párrafo.

* Toda indentación, si fuera necesaria, será de 4 espacios.


:index:`Estilos de letra`
------------------------------------

- **Negrita**::

    **negrita**

- *Cursiva*::

    *cursiva*

- `Texto interpretado`::

    `Texto interpretado`

- ``Literal inline``::

    ``Literal inline``

- Literal en párrafos.
    Inicia o finaliza un párrafo con ``::``.
    Después, empieza otro párrafo pero tabula su contenido.
    Si quieres varios párrafos tabula cada párrafo.
    ::

        ::

            Texto literal

            En varios párrafos



:index:`Listas`
----------------

Listas no Enumeradas
^^^^^^^^^^^^^^^^^^^^

- Todo elemento de la lista empieza con `-`, `*` o `+`.
- Este es el segundo item.
    - Que tiene un lista anidada.
    - Se puede anidar más
        - Tercer nivel ;)
- Elemento final.

La lista anterior se ha creado con este código: ::

    - Todo elemento de la lista empieza con `-`, `*` o `+`.
    - Este es el segundo item.
        - Que tiene un lista anidada.
        - Se puede anidar más.
            - Tercer nivel ;)
    - Elemento final.


Listas Enumeradas
^^^^^^^^^^^^^^^^^

1. Todo elemento de la lista empezará con un número seguido de un punto: P.e. ``1.``
#. Alternativamente puedes usar ``#.`` para auto-enumeración.
    #. Puedes anidar cualquier tipo de lista.
    #. Puede ser **no** enumerada o enumerada
        * Tercer nivel ;)
#. Elemento final.

La lista anterior se ha creado con este código: ::

    1. Todo elemento de la lista empezará con un número seguido de un punto: P.e. ``1.``
    #. Alternativamente puedes usar ``#.`` para auto-enumeración.
        #. Puedes anidar cualquier tipo de lista.
        #. Puede ser **no** enumerada o enumerada
            * Tercer nivel ;)
    #. Elemento final.


Quiero saber más
----------------

Para el proyecto no necesitas saber más. No obstante,

* Si quieres saber más, tienes una referencia rápida `aquí <https://docutils.sourceforge.io/docs/user/rst/quickref.html>`_.
* Si quieres saber mucho más, siempre te queda la página oficial de Sphinx_.

.. _Sphinx: https://www.sphinx-doc.org/es/master/usage/restructuredtext/