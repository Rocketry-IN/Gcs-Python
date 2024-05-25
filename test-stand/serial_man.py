import serial

# time_stamp,thrust,pressure,impulse,rssi,desg,state

thrust_point = []
avg_thrust = 0

ser = serial.Serial(port="com1" , baudrate=9600)

def read_serial():
    sum_thrust = 0
    impulse = 0
    incoming = ser.read().decode("utf-8")
    packet = incoming.split(",")
    thrust_point.append(packet[1])
    for i in thrust_point:
        sum_thrust = sum_thrust + float(i)
        #print(sum_thrust)
    avg_thrust = sum_thrust/len(thrust_point)
    packet.append(round(avg_thrust,2))
    impulse = avg_thrust*float(packet[1])
    packet[3] = round(impulse,2)

    if int(packet[0]) > 0:
        if int(packet[1]) < 25:
            state = "Idle"
        else:
            state = "Burn"
    else:
        state = "Idle"

    packet.append(state)
    #print(avg_thrust,impulse,state)
    

    return packet

def send_serial(command):
    outgoing = command.encode("utf-8")
    ser.write(outgoing)
