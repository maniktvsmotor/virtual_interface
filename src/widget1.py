from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel

class CANWidget1(QWidget):
    def __init__(self, can_interface):
        super().__init__()
        self.can_interface = can_interface
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        buttons = {
            "LEFT": 0,
            "RIGHT": 1,
            "TOP": 2,
            "BOTTOM": 3,
            "CENTER": 4,
        }

        positions = {
            "TOP": (1, 1), "LEFT": (2, 0), "CENTER": (2, 1),
            "RIGHT": (2, 2), "BOTTOM": (3, 1)
        }

        self.joystick_label = QLabel(f"Joystick")
        layout.addWidget(self.joystick_label, 0, 0, 1, 3)  # Placing label
        for label, data in buttons.items():
            row, col = positions[label]
            button = QPushButton(label)
            msg_name = "ENGINE_DATA_1"
            button.clicked.connect(lambda _, t="joystick", d=data , msg_name=msg_name : self.can_interface.send_msg(msg_name, t, d))
            layout.addWidget(button, row, col)

        self.setLayout(layout)
