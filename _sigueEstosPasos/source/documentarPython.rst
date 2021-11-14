:index:`Documentar programas Python`
====================================

Sphinx usa reStructuredText como lenguaje de marcas, por lo que así deberán de comentarse los programas en PyCharm.

1. PyCharm > Preferences > Tools > Python Integrates Tools
2. En DocString > DocString Format seleccionar ``reStructuredText``
3. En cada fichero .py del proyecto realizar:
    * Generar un :index:`docstring` al principio del fichero (Comentarios sobre el módulo, autor, fecha de modificación, ..)
    * Generar un docstring en la línea siguiente de cada clase, explicando el objetivo de la clase.
    * Generar un docstring en la línea siguiente de cada módulo, indicando precondiciones y postcondiciones.


Un `docstring` es un texto que ocupa varias líneas. La primera línea empieza por tres comillas dobles consecutivas y
la última línea consta de tres comillas dobles consecutivas.

En PyCharm, cuando escribas tres comillas dobles consecutivas completará parte del contenido cuando lo hagas
en la línea siguiente de un módulo.
