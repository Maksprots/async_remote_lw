from dataclasses import dataclass


@dataclass
class Config:
    plic_number = 1
    plic_qunt_cores = 1
    success_quartus_msg = "0 errors"
    command_to_load_firmware_1 = '{0} -m JTAG -c "{1}" -o p;{2}'
    command_to_flash_arduino = '"{0}" -C"{1}" -v -patmega328p' \
                               ' -carduino -P{2} -b57600 -D -Uflash:w:"{3}":i'
    quartus_pgm_path = ''
    fps = 24
    time_delta_arduino_msg = 0, 5
    avrdude_exe_path = ''
    avrdude_cf_path = ''
    port = ''
