import subprocess

from config import Config as cf
import serial.tools.list_ports


class Helper:
    def __init__(self):
        pass

    def test_path(self):
        assert (cf.avrdude_cf_path != '' or cf.avrdude_exe_path != ''
                or cf.quartus_pgm_path != ''), 'вы не заполнили необходимые пути'

    def print_plic(self):
        curent_FPGA = subprocess.run(cf.quartus_pgm_path + ' -l',
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     shell=True, text=True)
        fpga_list = curent_FPGA.stdout.split("Info: Processing started:", 2)[0]

        print('вам необходимо выбрать номер платы и заполнить plic_number')
        print('а так же plic_qunt_cores -- количество ядер у платы')
        print('список доступных плат')
        print(fpga_list)

    def print_arduino(self):
        print('заполняем port')
        print('в спске подключенных ком портов выбирете тот к '
              'которому подключена плата ардуино для данного стенда')
        for pt in serial.tools.list_ports.comports():
            print(pt.device + ' ' + pt.description + '  ' +
                  pt.serial_number)

    def main(self):
        print('Вам необходимо вручную заполнить адреса:')
        print('avrdude_exe_path')
        print('avrdude_cf_path')
        print('quartus_pgm_path')
        self.test_path()
        self.print_plic()
        self.print_arduino()


if __name__ == '__main__':
    h = Helper()
    h.main()
