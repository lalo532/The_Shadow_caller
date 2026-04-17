@echo off
:: UTF-8 para ñ y tildes
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Define la salida en la carpeta de arriba (game)
set "output=..\images.rpy"

:: Escribir el encabezado (usa > para crear/sobrescribir)
echo # ========================================== > "%output%"
echo # Imagenes autogeneradas >> "%output%"
echo # ========================================== >> "%output%"
echo. >> "%output%"

:: Recorrer archivos en la carpeta actual
for %%F in (*.png *.jpg *.jpeg *.webp) do (
    set "nombre_imagen=%%~nF"
    
    :: Reemplazar espacios por guiones bajos
    set "nombre_imagen=!nombre_imagen: =_!"
    
    :: Escribir la linea con la ruta relativa 'images/archivo.png'
    echo image !nombre_imagen! = "images/%%F" >> "%output%"
)

echo Proceso terminado. Archivo creado en: %output%
pause