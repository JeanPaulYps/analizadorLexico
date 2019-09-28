## Tarea curso lenguajes y compiladores
Para usar el analizador lexico, se debe usar el archivo entrada.txt, que es apartir de este archivo que el analizdor generará los tokens.

Los tokens que es capaz de leer son: _if, _main, _while, numeros binarios (e.g. 0b01010101), octales (e.g. 0241412), hexadecimales (e.g. 0x0101412), simbolos (una letra seguida de mas letras o numeros), comentarios multilinea con (* *) o comentarios de una linea (//).

Una vez ingresado la entrada en el archivo deberá ejecutar una de las siguientes instrucciones, que dependiendo de su sistema operativo:

´´´
python3 tarea.py
py tarea.py
´´´

La salida sera una tabla con todos los tokens encontrados.

´´´
+---------------------------------------------+
| Tipo                 |                 Valor|
|---------------------------------------------|
| comentario           |        ///comentario |
| decimal              |            241241241 |
| binario              |           0b01010101 |
| hexadecimal          |             0x241241 |
| decimal              |                    0 |
| reservada            |                  _if |
| reservada            |                _main |
| reservada            |               _while |
+---------------------------------------------+
´´´