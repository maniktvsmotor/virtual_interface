from PyQt5.QtWidgets import QWidget, QGridLayout, QSlider, QLabel
from PyQt5.QtCore import Qt

class CANWidget4(QWidget):
    def __init__(self, can_interface):
        super().__init__()
        self.can_interface = can_interface
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Adding slider for speed (0 to 200 km/h)
        self.rpm_slider = QSlider(Qt.Horizontal)
        self.rpm_slider.setMinimum(0)
        self.rpm_slider.setMaximum(12000)  # 0 to 200 
        self.rpm_slider.setTickInterval(10)
        self.rpm_slider.setTickPosition(QSlider.TicksBelow)
        self.rpm_slider.valueChanged.connect(self.update_rpm)

        # rpm label
        self.rpm_label = QLabel(f"rpm: 0")
        layout.addWidget(self.rpm_label, 0, 0, 1, 3)  # Placing label
        layout.addWidget(self.rpm_slider, 1, 0, 1, 3)  # Placing slider below label

        self.setLayout(layout)

    def update_rpm(self):
        rpm = self.rpm_slider.value()
        self.rpm_label.setText(f"rpm: {rpm}")

        # Update CAN message data with rpm in the last byte
        # hex_rpm = rpm & 0xFF
        # data = [0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, hex_rpm]
        msg_name = "ENGINE_DATA_1"
        self.can_interface.send_msg(msg_name, "rpm", rpm)
