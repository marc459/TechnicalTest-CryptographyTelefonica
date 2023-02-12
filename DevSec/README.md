## HealthPyProcess

    Programa para detectar de procesos amenaza. Visualización de consumos de los procesos y monitorización de
    acceso a directorios reportados en archivos .log.

## Usage

    python3 HealthPyProcess.py

## Requirements
    
    chmod +x HealthPyProcess.py
    pip3 install psutil numpy


## Project Idea -- HealthPyProcess --

Aplicacion que detecta '*Abuso de recursos del sistema*' para analizar en la maquina local posibles procesos que saturan memoria y cpu asi como uso indebido de ciertas carpetas y acceso a internet.
Road developing:
    - Gráficas en vivo de uso de cpu y memoria ram.
    - Procesos en uso más pesados.
    - Reporte del tráfico en la red de cada proceso en logs.
    - Identificación de procesos maliciosos. (Unknown file signature)

 Updates:
    - Detección mas perfilada de tráfico en la red
    - Hacer uso de herramientas externas y antivirus
    - Interfaz de gestión de los procesos
    - Inteligencia artificial de analisis de los logs generados por la aplicación


