import time
import serial
import subprocess as sub
from config import Config as cf


class Arduino:
    commands_to_values = {
        'but': '0',
        'sw': '1',
        'dl': '2',
    }

    def __init__(self, port):
        self._board = serial.Serial(
            port=port,
            baudrate=9600,
            timeout=.1)

    def download_firmware(
            self,
            avrdude_exe_path: str,
            avrdude_cf_path: str,
            port: str,
            firmware_path: str) -> bool:
        flashing_ps = sub. \
            run(cf.command_to_flash_arduino.
                format(avrdude_exe_path,
                       avrdude_cf_path,
                       port,
                       firmware_path),
                stdout=sub.PIPE,
                stderr=sub.PIPE,
                text=True)
        return True if 'done' in flashing_ps.stderr else False

    def send_command(self, command_and_pin: str):
        command, pin = command_and_pin.split()
        if 'dl' in command:
            time_to_wait = pin
            time.sleep(time_to_wait)
            return True
        command_for_send = self.commands_to_values[command] + pin
        self._board.write(bytes(command_for_send, 'utf-8'))
        time.sleep(cf.time_delta_arduino_msg)
        arduino_out = str(self._board.
                          readline().
                          decode().strip('\r\n'))
        return True if arduino_out == 'ok' else False


if __name__ == '__main__':
    ard = Arduino()
    ard.send_command('sw 1')
