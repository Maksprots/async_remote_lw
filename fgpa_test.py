import subprocess
from config import Config as cf


class Plic:
    def __init__(self, number_of_cores):
        self.flow = open('d', 'w')
        quartus = subprocess.run(cf.quartus_pgm_path + " -l",
                                 stdout=self.flow,
                                 stderr=self.flow,
                                 shell=True,
                                 text=True)

        print(quartus.stdout, "\n")
        fpga_list = quartus.stdout.split("Info: Processing started:", 2)[0]
        if quartus.stdout.find(f"{cf.plic_number}) ") != -1:
            current_port = quartus.stdout.split(f"{cf.plic_number}) ", 2)[1]
            self.current_port = current_port.split('\n', 1)[0]
            print(current_port)
        else:
            raise Exception('плата не нашлась')

    def load_to_plic(self, firmware_path):
        # одно ядро

        result = subprocess.run(cf.command_to_load_firmware_1.
                                format(cf.quartus_pgm_path,
                                       self.current_port,
                                       firmware_path),
                                stdin=self.flow,
                                stdout=self.flow,
                                stderr=self.flow,
                                shell=True,
                                text=True)
        if result.stdout.count(cf.main_key):

            return "OK"
        else:
            return "Прошить плату не удалось"
