from dataclasses import dataclass


@dataclass
class Config:
    plic_number = 1
    main_key = "Quartus Prime Programmer was successful. 0 errors"
    command_to_load_firmware_1 = '{0} -m JTAG -c "{1}" -o p;{2}'
    quartus_pgm_path = ''
