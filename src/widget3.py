from PyQt5.QtWidgets import QWidget, QGridLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

class CANWidget3(QWidget):
    def __init__(self, can_interface):
        super().__init__()
        self.can_interface = can_interface
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Adding slider for speed (0 to 200 km/h)
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setMinimum(0)
        self.speed_slider.setMaximum(200)  # 0 to 200 km/h
        self.speed_slider.setTickInterval(10)
        self.speed_slider.setTickPosition(QSlider.TicksBelow)
        self.speed_slider.valueChanged.connect(self.update_speed)

        # Speed label
        self.speed_label = QLabel(f"Speed: 0 km/h")
        layout.addWidget(self.speed_label, 0, 0, 1, 3)  # Placing label
        layout.addWidget(self.speed_slider, 1, 0, 1, 3)  # Placing slider below label

        self.setLayout(layout)

    def update_speed(self):
        speed = self.speed_slider.value()
        self.speed_label.setText(f"Speed: {speed} km/h")

        # Update CAN message data with speed in the last byte
        # hex_speed = speed & 0xFF
        # data = [0xFF, 0xFF, 0xFF, 0xFF, 0x00, 0x00, 0x03, 0x00]
        msg_name = "ABS_DATA_3"
        self.can_interface.send_msg(msg_name, "speed", speed)
