import serial

#thrust, pressure

thrust_point = []
avg_thrust = 0

ser = serial.Serial(port="com4" , baudrate=9600)

def read_serial():
    incoming = ser.readline().decode("utf-8")
    packet = incoming.strip().split(",")
    return packet

