import can
import cantools

class CANInterface:
    def __init__(self):
        self.bus = can.Bus(interface='socketcan', channel='vcan0', bitrate=500000)
        # self.bus = can.Bus(interface='pcan', channel='PCAN_USBBUS1', bitrate=500000)
        INPUT_DBC_PATH = '../dbc_files/TVSM_N600.dbc'
        self.db = cantools.db.load_file(INPUT_DBC_PATH)

    def send_msg(self, msg_name, text, data):
        print(f"Sending CAN message from {text}...")
        if(text=="speed"):
            msg = self.db.get_message_by_name(msg_name)
            en_data = msg.encode({'CRC_SPEED':0, 'ALIVE_COUNTER_SPEED':0, 'WHEEL_SPEED_REAR':0, 'WHEEL_SPEED_FRONT':data, 'WHEEL_SPEED_REAR_STATUS':0, 'WHEEL_SPEED_FRONT_STATUS':1, 'LC_STATUS':0, 'NUMBER_OF_LAUNCHES':0,'ABS_STATUS':0, 'RESERVED_SIGNAL':0, 'WHEEL_ACC':0})
        elif(text=="rpm"):
            msg = self.db.get_message_by_name(msg_name)
            en_data = msg.encode({'CRC_ENGINE_DATA_1':0, 'ALIVE_COUNTER_ENGINE_DATA_1':0, 'HANDLE_GRIP_OPEN_PERCENTAGE_1':0, 'CLUTCH_SW_STATUS':0, 'THROTTLE_OPEN_PERCENTAGE_1':0, 'GEAR_POSITION':0, 'ENGINE_RPM':data, 'KILL_STATUS':0,'ES_SWITCH_STATUS':0, 'KL50_STATUS':0, 'CLUTCH_SW_STATUS_2':0})
        elif(text=="joystick"):
            msg = self.db.get_message_by_name(msg_name)
            en_data = msg.encode({'CRC_ENGINE_DATA_1':0, 'ALIVE_COUNTER_ENGINE_DATA_1':0, 'HANDLE_GRIP_OPEN_PERCENTAGE_1':0, 'CLUTCH_SW_STATUS':0, 'THROTTLE_OPEN_PERCENTAGE_1':0, 'GEAR_POSITION':data, 'ENGINE_RPM':0, 'KILL_STATUS':0,'ES_SWITCH_STATUS':0, 'KL50_STATUS':0, 'CLUTCH_SW_STATUS_2':0})
        else:
            print("Incorrect Message....")
        
        try:
            message = can.Message(arbitration_id=msg.frame_id, data=en_data, is_extended_id=False)
            self.bus.send(message)
            print(f"Sent: ID={hex(message.arbitration_id)}, Data={message.data}")
        except can.CanError as e:
            print(f"CAN Error: {e}")
