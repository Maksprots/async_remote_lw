import subprocess as sub
from config import Config as Cf

TEST_FIRMWARE = ''


class Plic:
    def __init__(self, plic_number=Cf.plic_number):
        quartus = sub.run(Cf.quartus_pgm_path + " -l",
                          stdout=sub.PIPE,
                          stderr=sub.PIPE,
                          shell=True,
                          text=True)

        if quartus.stdout.find(f"{plic_number}) ") != -1:
            current_port = quartus.stdout.split(f"{Cf.plic_number}) ", 2)[1]
            self.current_port = current_port.split('\n', 1)[0]
            print(current_port)
        else:
            raise Exception('плата не нашлась')

    def download_to_plic(self, firmware_path: str) -> bool:
        result = sub.run(Cf.command_to_load_firmware_1.
                         format(Cf.quartus_pgm_path,
                                self.current_port,
                                firmware_path),
                         stdin=sub.PIPE,
                         stdout=sub.PIPE,
                         stderr=sub.PIPE,
                         shell=True,
                         text=True)

        return True if result.stdout.count(Cf.success_quartus_msg) else False


if __name__ == '__main__':
    c = Plic()
    print(c.download_to_plic(TEST_FIRMWARE))
