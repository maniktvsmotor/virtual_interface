from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel

class CANWidget5(QWidget):
    def __init__(self, can_interface):
        super().__init__()
        self.can_interface = can_interface
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        buttons = {
            "TT1": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            "TT2": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00],
            "TT3": [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x10, 0x00],
            "TT4": [0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x40, 0x00],
            "TT5": [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01],
        }

        positions = {
            "TT1": (1, 0), "TT2": (1, 1), "TT3": (1, 2),
            "TT4": (2, 0), "TT5": (2, 1)
        }

        self.telltale_label = QLabel(f"telltale")
        layout.addWidget(self.telltale_label, 0, 0, 1, 3)  # Placing label
        for label, data in buttons.items():
            row, col = positions[label]
            button = QPushButton(label)
            arb_id = 0x01
            button.clicked.connect(lambda _, t=label, d=data , id=arb_id: self.can_interface.send_msg(id, t, d))
            layout.addWidget(button, row, col)

        self.setLayout(layout)
