import subprocess as sub
from config import Config as Cf

TEST_FIRMWARE = ''


class Plic:
    def __init__(self):
        quartus = sub.run(Cf.quartus_pgm_path + " -l",
                          stdout=sub.PIPE,
                          stderr=sub.PIPE,
                          shell=True,
                          text=True)

        print(quartus.stdout, "\n")
        # fpga_list = quartus.stdout.split("Info: Processing started:", 2)[0]
        if quartus.stdout.find(f"{Cf.plic_number}) ") != -1:
            current_port = quartus.stdout\
                .decode('utf-8').split(f"{Cf.plic_number}) ", 2)[1]
            self.current_port = current_port.split('\n', 1)[0]
            print(current_port)
        else:
            raise Exception('плата не нашлась')

    def load_to_plic(self, firmware_path):
        result = sub.run(Cf.command_to_load_firmware_1.
                         format(Cf.quartus_pgm_path,
                                self.current_port,
                                firmware_path),
                         stdin=sub.PIPE,
                         stdout=sub.PIPE,
                         stderr=sub.PIPE,
                         shell=True,
                         text=True)

        return True if result.stdout\
            .decode('utf-8').count(Cf.main_key) else False


if __name__ == '__main__':
    c = Plic()
    print(c.load_to_plic(TEST_FIRMWARE))
