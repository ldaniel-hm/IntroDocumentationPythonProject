:index:`Convertir los Módulos en Paquetes`
===========================================

La generación de la documentación se hace en función de los ``import`` que se encuentran en cada fichero ``.py``
lo que provoca que muchos módulos queden sin documentar. Para evitar esto crea un fichero ``__init__.py`` en cada
carpeta de tu proyecto.

No es la solución más ortodoxa pero te evitará crear algunos documentos.
