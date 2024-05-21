import serial



ser = serial.Serial(port="com1" , baudrate=9600)

def read_serial():
    incoming = ser.read().decode("utf-8")
    packet = incoming.split(",")
    return packet

def send_serial(command):
    outgoing = command.encode("utf-8")
    ser.write(outgoing)