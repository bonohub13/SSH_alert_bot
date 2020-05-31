#!/usr/bin/python3

import requests
import subprocess
from time import sleep

class InformSSH:
    def __init__(self, accessToken, ip_addr: str, setFreq=180):
        self.url = 'https://notify-api.line.me/api/notify'
        self.headers = {'Authorization': 'Bearer '+accessToken}

        self.freq = setFreq
        self.counter = 0
        self.ssh_counter = 0

    def dataToSend(self, message, image=None, sticker_pkg_id=None, sticker_id=None):
        self.payload = {'message': message,
                   'stickerPackageId': sticker_pkg_id,
                   'stickerId': sticker_id}
        self.files = {}
        if image != None:
            self.files = {'imgFile': open(image, 'rb')}

    def run(self):
        while True:
            check_ssh = subprocess.Popen('ss | grep -i ssh | grep -i {}'.format(self.ip), stdout=subprocess.PIPE, shell=True)
            check_ssh_stdout = check_ssh.stdout.read().decode('utf-8').split()
            if 'ESTAB' in check_ssh_stdout:
                self.ssh_counter += 1
                if self.ssh_counter != 0 and self.counter%6 == 0:
                    self.dataToSend('Your computer has been accessed through SSH!\n\nSSH established:\n\t[{} -> {}]'.format(check_ssh_stdout[-2], check_ssh_stdout[-1]))
                    request = requests.post(self.url, headers=self.headers,
                                            data=self.payload,
                                            files=self.files)
                    self.ssh_counter = 0
            self.counter += 0
            sleep(30)

if __name__ == '__main__':
    access_token = 'Your access token here!'
    bot = InformSSH(access_token)

    bot.run()
