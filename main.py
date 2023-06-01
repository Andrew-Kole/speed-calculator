from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, \
    QLabel, QPushButton, QLineEdit, QComboBox
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()
        self.distance_combo_box = QComboBox()
        self.distance_combo_box.addItems(["Metric: (km)", "Imperial: (miles)"])

        hours_label = QLabel("Time (hours)")
        self.hours_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_average_speed)
        self.output_label = QLabel("")

        # Adding to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.distance_combo_box, 0, 2)

        grid.addWidget(hours_label, 1, 0)
        grid.addWidget(self.hours_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        self.setLayout(grid)

    def calculate_average_speed(self):
        distance = self.distance_line_edit.text()
        hours = self.hours_line_edit.text()
        average = int(distance) / int(hours)
        if self.distance_combo_box.currentText() == "Metric: (km)":
            self.output_label.setText(f"Average speed is {average} km/h")
        elif self.distance_combo_box.currentText() == "Imperial: (miles)":
            self.output_label.setText(f"Average speed is {average} miles/h")



app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
