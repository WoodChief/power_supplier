import can
import os
import json
from munch import Munch
import threading


class CAN:
    def __init__(self):
        with open('CAN.json') as f:
            json_dict = json.load(f)['posix']
            self.can_settings = Munch.fromDict(json_dict)

        password = 'woodman'
        os.system(f"echo {password} "
                  f"| sudo -S ip link set can1 up "
                  f"type can bitrate {self.can_settings.bitrate}")

        self.bus = can.ThreadSafeBus(interface=self.can_settings.interface,
                                     channel='can1',
                                     bitrate=self.can_settings.bitrate)
        self.mes = can.Message()
        self.mes.is_extended_id = self.can_settings.extended_id
        self.mes.dlc = self.can_settings.dlc

        with open('settings/power_supply_settings.json') as f:
            self.settings = Munch.fromDict(json.load(f))

        self.receive_thread = threading.Thread(target=self.start_receiver)
        # self.receive_thread.start()

    def start_receiver(self):
        while True:
            mes = self.bus.recv(0.01)
            if mes is not None:
                print(f'MESSAGE GOT: \n MES_ID: {mes.arbitration_id} \t'
                      f' DATA: {mes.data}')

    def can_send(self):
        self.bus.send(self.mes)
        print(f'MESSAGE SENT: \n MES_ID: {self.mes.arbitration_id} \t'
              f'DATA {self.mes.data}')


if __name__ == '__main__':
    con = CAN()
