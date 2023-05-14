import time

for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            tiempo_actual = time.localtime()
            hora_actual = tiempo_actual.tm_hour
            minuto_actual = tiempo_actual.tm_min
            segundo_actual = tiempo_actual.tm_sec
            print("{:02d}:{:02d}:{:02d}".format(hora_actual, minuto_actual, segundo_actual))
            time.sleep(1)
