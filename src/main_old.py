import sys
import can
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class CANWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CAN Controller")
        self.setGeometry(100, 100, 300, 300)

        self.bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=500000)

        layout = QGridLayout()

        # Create buttons
        btn_left = QPushButton("LEFT")
        btn_left.clicked.connect(lambda: self.send_msg("LEFT", [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00]))
        layout.addWidget(btn_left, 1, 0)

        btn_right = QPushButton("RIGHT")
        btn_right.clicked.connect(lambda: self.send_msg("RIGHT", [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x04, 0x00]))
        layout.addWidget(btn_right, 1, 2)

        btn_top = QPushButton("TOP")
        btn_top.clicked.connect(lambda: self.send_msg("TOP", [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x10, 0x00]))
        layout.addWidget(btn_top, 0, 1)

        btn_bottom = QPushButton("BOTTOM")
        btn_bottom.clicked.connect(lambda: self.send_msg("BOTTOM", [0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x40, 0x00]))
        layout.addWidget(btn_bottom, 2, 1)

        btn_center = QPushButton("CENTER")
        btn_center.clicked.connect(lambda: self.send_msg("CENTER", [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01]))
        layout.addWidget(btn_center, 1, 1)

        self.setLayout(layout)

    def send_msg(self, text, data):
        print("Sending CAN message...")
        try:
            message = can.Message(
                arbitration_id=0x01,
                data=data,
                is_extended_id=False
            )
            self.bus.send(message)
            print(f"Message sent by {text}: ID={hex(message.arbitration_id)}, Data={message.data}")
        except can.CanError as e:
            print(f"Failed to send message: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CANWindow()
    window.show()
    sys.exit(app.exec_())
