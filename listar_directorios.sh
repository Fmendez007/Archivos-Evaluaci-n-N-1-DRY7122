#!/bin/bash
# Lista contenidos desde /home/devasc y cuenta los archivos

echo "Listando contenidos de /home/devasc..." > contenidoDirectorio.txt
find /home/devasc >> contenidoDirectorio.txt

echo "Contando archivos..."
cantidad=$(find /home/devasc -type f | wc -l)
echo "Total de archivos encontrados: $cantidad" >> contenidoDirectorio.txt

echo "Proceso completado. Revisa contenidoDirectorio.txt"

