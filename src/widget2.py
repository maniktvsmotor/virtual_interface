from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton

class CANWidget2(QWidget):
    def __init__(self, can_interface):
        super().__init__()
        self.can_interface = can_interface
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        buttons = {
            "LEFT2": [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            "RIGHT2": [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00],
            "TOP2": [0x10, 0x00, 0x00, 0x00, 0x00, 0x01, 0x10, 0x00],
            "BOTTOM2": [0x10, 0x00, 0x00, 0x01, 0x00, 0x00, 0x40, 0x00],
            "CENTER2": [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01],
        }

        positions = {
            "TOP2": (0, 1), "LEFT2": (1, 0), "CENTER2": (1, 1),
            "RIGHT2": (1, 2), "BOTTOM2": (2, 1)
        }

        for label, data in buttons.items():
            row, col = positions[label]
            button = QPushButton(label)
            button.clicked.connect(lambda _, t=label, d=data: self.can_interface.send_msg(t, d))
            layout.addWidget(button, row, col)

        self.setLayout(layout)
