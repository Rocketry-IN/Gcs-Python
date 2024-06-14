import serial

#thrust, pressure

thrust_point = []
avg_thrust = 0

ser = serial.Serial(port="com1" , baudrate=9600)

def read_serial():
    incoming = ser.read().decode("utf-8")
    packet = incoming.split(",")
    return packet
