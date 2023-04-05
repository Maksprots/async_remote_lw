import subprocess

number_of_cores = 1
main_key = ["Quartus Prime Programmer was successful. 0 errors"]
Quartus_pgm_path = ''


class Fgpa:
    def __init__(self, number_of_cores):
        # поиск квартуса (пути) Quartus_pgm_path
        # todo  поиск плисины через квартус

        curent_FPGA = subprocess.run(Quartus_pgm_path + " -l", stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                     shell=True, text=True)
        print(curent_FPGA.stdout, "\n")  # Вывод консоли
        fpga_list = curent_FPGA.stdout.split("Info: Processing started:", 2)[0]
        # # Получаем номер той платы, которую в данный момент необходимо прошивать
        FPGA_num = 1
        str = "{}) ".format(FPGA_num)
        # # TODO  номер плисины тут
        # # В случае, если плата с заданным номером существует, определяем порт её подключения как основной
        if curent_FPGA.stdout.find(str) != -1:
            curent_port = curent_FPGA.stdout.split(str, 2)[1]
            self.curent_port = curent_port.split('\n', 1)[0]
            print(curent_port)
        # Если такой платы не существует, выводим соответствую ошибку
        else:

            raise Exception('плата не нашлась')



    def load_to_plis(self, firmware_path):
        # много ядер
        # прошивка
        i = 0
        if number_of_cores != 1:
            result = subprocess.run(
                '{0} -m JTAG -c "{1}" -o p;{2}@{3}'.format(Quartus_pgm_path,
                                                           self.curent_port,
                                                           firmware_path,
                                                           i),
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True, text=True)
            fpga_flashed = result.stdout.split("Info: Processing started:", 2)[1]
            # Обрабатываем 2 состояния завершения прошивки платы
            if result.stdout.count(main_key[0]):
                print("Прошивка платы ПЛИС окончена")
                return ("OK")
            else:
                print("Прошивка платы ПЛИС заверщилась неудачей")
                return ("Neok")
        # одно ядро
        one_core_cmd = '{0} -m JTAG -c "{1}" -o p;{2}'
        result = subprocess.run(one_core_cmd.format(Quartus_pgm_path,
                                                    self.curent_port,
                                                    firmware_path),
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                shell=True,
                                text=True)
        if result.stdout.count(main_key[0]):

            return "OK"
        else:
            return "Прошить плату не удалось"

