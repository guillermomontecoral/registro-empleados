{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww29740\viewh16340\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Registro de Empleados (PyQt5 + Pandas)\
\
Este es un proyecto de prueba desarrollado en **Python** que permite registrar empleados con sus datos b\'e1sicos y calcular su **sueldo neto** en base a rangos salariales.  \
La aplicaci\'f3n cuenta con una interfaz gr\'e1fica hecha en **PyQt5**, y permite **exportar los datos a Excel**.\
\
---\
\
## Funcionalidades\
\
- Registrar empleados con:\
  - Nombre\
  - Apellido\
  - Profesi\'f3n\
  - Sueldo bruto\
- C\'e1lculo autom\'e1tico del **sueldo neto**:\
  - Sueldos hasta 1000 \uc0\u8594  80% neto\
  - Sueldos entre 1001 y 4000 \uc0\u8594  75% neto\
  - Sueldos mayores a 4000 \uc0\u8594  65% neto\
- Visualizaci\'f3n en una **tabla interactiva** (QTableWidget).\
- Exportaci\'f3n de los datos a un archivo **Excel (.xlsx)** con marca de tiempo.\
\
---\
\
## Tecnolog\'edas utilizadas\
\
- [Python 3](https://www.python.org/)\
- [PyQt5](https://pypi.org/project/PyQt5/) \uc0\u8594  interfaz gr\'e1fica\
- [Pandas](https://pandas.pydata.org/) \uc0\u8594  manejo de datos\
- [Openpyxl](https://pypi.org/project/openpyxl/) \uc0\u8594  exportaci\'f3n a Excel\
\
---\
\
## Instalaci\'f3n\
\
Clona este repositorio:\
\
```bash\
git clone [https://github.com/tu-usuario/registro-empleados.git](https://github.com/guillermomontecoral/registro-empleados)\
cd registro-empleados\
\
## \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Crea un entorno virtual\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 ```bash\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 python -m venv venv\
source venv/bin/activate   # En Linux/Mac\
venv\\Scripts\\activate      # En Windows\
\
## Instalar dependencias \
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 ```bash\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 pip install -r requirements.txt\
\
## Ejecuci\'f3n\
\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 ```bash\
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0
\cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 python employee_form.py\
}
