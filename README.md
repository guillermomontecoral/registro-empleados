# Registro de Empleados (PyQt5 + Pandas)

Este es un mini proyecto de prueba desarrollado en **Python** que permite registrar empleados con sus datos básicos y calcular su **sueldo neto** en base a rangos salariales.  
La aplicación cuenta con una interfaz gráfica hecha en **PyQt5**, y permite **exportar los datos a Excel**.

---

## Funcionalidades

- Registrar empleados con:
  - Nombre
  - Apellido
  - Profesión
  - Sueldo bruto
- Cálculo automático del **sueldo neto**:
  - Sueldos hasta 1000 → 80% neto
  - Sueldos entre 1001 y 4000 → 75% neto
  - Sueldos mayores a 4000 → 65% neto
- Visualización en una **tabla interactiva** (QTableWidget).
- Exportación de los datos a un archivo **Excel (.xlsx)** con marca de tiempo.

---

## Tecnologías utilizadas

- [Python 3](https://www.python.org/)
- [PyQt5](https://pypi.org/project/PyQt5/) → interfaz gráfica
- [Pandas](https://pandas.pydata.org/) → manejo de datos
- [Openpyxl](https://pypi.org/project/openpyxl/) → exportación a Excel

---

## Instalación

Clona este repositorio:

```bash
git clone https://github.com/tu-usuario/registro-empleados.git
cd registro-empleados

## Crea un entorno virtual

```bash
python -m venv venv
source venv/bin/activate   # En Linux/Mac
venv\Scripts\activate      # En Windows

## Instalar dependencias 

```bash
pip install -r requirements.txt

## Ejecución

```bash
python employee_form.py
