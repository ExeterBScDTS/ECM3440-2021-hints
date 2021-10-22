# Application for manual testing of the CounterFit user interface
#
from counterfit_connection import CounterFitConnection
from counterfit_shims_grove.adc import ADC
from counterfit_shims_grove.grove_relay import GroveRelay

adc = None
relay = None

def connect_to_ui() ->None:
    global adc, relay
    CounterFitConnection.init('127.0.0.1', 5000)
    adc = ADC()
    relay = GroveRelay(5)

def check_relay() ->bool:
    global relay
    relay.on()
    resp = input("confirm actuator relay pin 5 is on -> (y/n) ")
    if resp == "n":
        return False
    relay.off()
    resp = input("confirm actuator relay pin 5 is off -> (y/n) ")
    if resp == "n":
        return False
    else:
        return True

def check_sensor() ->bool:
    global adc
    resp = input("set value of ADC 0 to 1000. Press return when ready > ")
    if adc.read(0) == 1000:
        return True
    else:
        return False

if __name__ == '__main__':
    connect_to_ui()
    if check_relay():
        print("Actuator output correct")
    else:
        print("Actuator check failed")
    if check_sensor():
        print("Sensor input correct")
    else:
        print("Sensor check failed")

