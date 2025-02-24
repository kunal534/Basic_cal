from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Calculator App")
        
        self.text_box = QLineEdit()
        self.text_box.setReadOnly(True)
        
        self.master_layout = QVBoxLayout()
        self.grid = QGridLayout()
        
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]
        
        for row, row_values in enumerate(buttons):
            for col, value in enumerate(row_values):
                button = QPushButton(value)
                self.grid.addWidget(button, row, col)
                
                if value == "=":
                    button.clicked.connect(self.calculate)
                else:
                    button.clicked.connect(lambda checked, v=value: self.append_text(v))
        
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        
        self.last_ele_button = QPushButton("<")
        self.last_ele_button.clicked.connect(self.del_last_element)
        
        last_row = QHBoxLayout()
        last_row.addWidget(self.clear_button)
        last_row.addWidget(self.last_ele_button)
        
        self.master_layout.addWidget(self.text_box)
        self.master_layout.addLayout(self.grid)
        self.master_layout.addLayout(last_row)
        
        self.setLayout(self.master_layout)
    
    def calculate(self):
        try:
            result = str(eval(self.text_box.text()))
            self.text_box.setText(result)
        except Exception:
            self.text_box.setText("Error")
    
    def clear_text(self):
        self.text_box.clear()
    
    def del_last_element(self):
        self.text_box.setText(self.text_box.text()[:-1])
    
    def append_text(self, value):
        self.text_box.setText(self.text_box.text() + value)
        
if __name__ == "__main__":
    app = QApplication([])
    window = CalculatorApp()
    window.show()
    app.exec_()
