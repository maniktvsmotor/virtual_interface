from PyQt5.QtWidgets import QWidget, QHBoxLayout
from can_interface import CANInterface
from widget1 import CANWidget1
from widget2 import CANWidget2
from widget3 import CANWidget3
from widget4 import CANWidget4
from widget5 import CANWidget5

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Control Panel")
        self.setGeometry(100, 100, 1200, 150)

        layout = QHBoxLayout()

        self.can_interface = CANInterface()
        layout.addWidget(CANWidget1(self.can_interface))
        # layout.addWidget(CANWidget2(self.can_interface))
        layout.addWidget(CANWidget3(self.can_interface))
        layout.addWidget(CANWidget4(self.can_interface))
        layout.addWidget(CANWidget5(self.can_interface))

        self.setLayout(layout)
