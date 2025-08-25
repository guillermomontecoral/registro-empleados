
from datetime import datetime
import pandas as pd
import sys
import os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)

df = pd.DataFrame(
    columns=[
        "Nombre", 
        "Apellido", 
        "Profesion", 
        "Sueldo", 
        "Sueldo Neto"
    ]
)

def create_app():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("Registro de empleados")
    window.resize(800, 600)

    layout_main = QVBoxLayout()
    layout_main.addSpacing(20)

    layout_form = QHBoxLayout()

    name_input = QLineEdit()
    name_input.setPlaceholderText("Nombre")
    layout_form.addWidget(name_input)
    
    lastname_input = QLineEdit()
    lastname_input.setFixedHeight(30)
    lastname_input.setPlaceholderText("Apellido")
    layout_form.addWidget(lastname_input)

    profession_input = QLineEdit()
    profession_input.setFixedHeight(30)
    profession_input.setPlaceholderText("Profesión")
    layout_form.addWidget(profession_input)

    salary_input = QLineEdit()
    salary_input.setFixedHeight(30)
    salary_input.setPlaceholderText("Sueldo")
    layout_form.addWidget(salary_input)

    layout_main.addLayout(layout_form)

    layout_button = QHBoxLayout()

    add_button = QPushButton("Agregar")
    add_button.setFixedHeight(35)
    layout_button.addWidget(add_button)

    export_button = QPushButton("Exportar Excel")
    export_button.setFixedHeight(35)
    layout_button.addWidget(export_button)

    layout_main.addLayout(layout_button)

    table = QTableWidget()
    table.setColumnCount(5)
    table.setHorizontalHeaderLabels(
        [
            "Nombre", 
            "Apellido", 
            "Profesion", 
            "Sueldo", 
            "Sueldo Neto"
        ]
    )
    table.horizontalHeader().setStretchLastSection(True)
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    layout_main.addWidget(table)

    window.setLayout(layout_main)
    window.show()

    def add_data():
        name = name_input.text() 
        lastname = lastname_input.text()
        profession = profession_input.text()
        salary = float(salary_input.text())

        if salary > 0 and salary <= 1000:
            net_salary = salary * 0.8
        elif salary > 1000 and salary <= 4000:
            net_salary = salary * 0.75
        else:
            net_salary = salary * 0.65
        
        new_row = {
            "Nombre": name, 
            "Apellido": lastname, 
            "Profesion": profession, 
            "Sueldo": salary, 
            "Sueldo Neto": net_salary
        }

        global df
        df.loc[len(df)] = new_row
        row = table.rowCount()
        table.insertRow(row)
        table.setItem(row, 0, QTableWidgetItem(name))
        table.setItem(row, 1, QTableWidgetItem(lastname))
        table.setItem(row, 2, QTableWidgetItem(profession))
        table.setItem(row, 3, QTableWidgetItem(f"{salary:.2f}"))
        table.setItem(row, 4, QTableWidgetItem(f"{net_salary:.2f}"))
        table.resizeRowsToContents()

        name_input.clear()
        lastname_input.clear()
        profession_input.clear()
        salary_input.clear()

    def export_excel():
        # if os.path.exists('data_employees.xlsx'):
        #     os.remove('data_employees.xlsx')
        timestamp = datetime.now().strftime('%d%m%Y-%H%M%S')
        df.to_excel(f'data_employees_{timestamp}.xlsx', index=False, engine='openpyxl')

    add_button.clicked.connect(add_data)
    export_button.clicked.connect(export_excel)
    sys.exit(app.exec_())

create_app()