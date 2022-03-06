class RobotByteCom:

    START_BYTE = 0x7E
    ESCAPE_BYTE = 0x7D
    ESCAPE_XOR = 0x20

    COMMAND_ID_NUMBER = 0x01
    COMMAND_ID_STRING = 0x02

    def __init__(self, serial_object, team_number):
        self.ser = serial_object
        self.team_number = team_number
        self.crc = 0
    
    def send_string_command(self, string_to_send):
        self.send_start_byte()
        self.send_length_byte(len(string_to_send) + 2)
        self.send_team_number_byte()
        self.send_command_byte(RobotByteCom.COMMAND_ID_STRING)
        self.send_byte_array(string_to_send.encode())
        self.send_crc()
    
    def send_number_command(self, number_to_send):
        self.send_start_byte()
        self.send_length_byte(6)
        self.send_team_number_byte()
        self.send_command_byte(RobotByteCom.COMMAND_ID_NUMBER)
        self.send_byte_array(number_to_send.to_bytes(4, 'big'))
        self.send_crc()

    def send_start_byte(self):
        self.ser.write(RobotByteCom.START_BYTE.to_bytes(1, 'big')) # does not get escaped
        self.crc = 0

    def send_length_byte(self, length_byte):
        self.send_one_byte(length_byte, crc_ignore=True)

    def send_team_number_byte(self):
        self.send_one_byte(self.team_number)

    def send_command_byte(self, command_id):
        self.send_one_byte(command_id)

    def send_one_byte(self, one_byte, crc_ignore=False):
        if not crc_ignore:
            self.crc -= one_byte
        if one_byte == RobotByteCom.START_BYTE or one_byte == RobotByteCom.ESCAPE_BYTE:
            self.ser.write(RobotByteCom.ESCAPE_BYTE.to_bytes(1, 'big'))
            one_byte = one_byte ^ RobotByteCom.ESCAPE_XOR
        self.ser.write(one_byte.to_bytes(1, 'big'))
    
    def send_byte_array(self, byte_array):
        for one_byte in byte_array:
            self.send_one_byte(one_byte)
    
    def send_crc(self):
        self.crc = self.crc % 256
        self.send_one_byte(self.crc, crc_ignore=True)
        

        

