#!/usr/bin/env python3

import requests
import subprocess
from time import sleep

class InformSSH:
    def __init__(self, accessToken, setFreq=180):
        self.url = 'https://notify-api.line.me/api/notify'
        self.headers = {'Authorization': 'Bearer '+accessToken}

        self.freq = setFreq

    def dataToSend(self, message, image=None, sticker_pkg_id=None, sticker_id=None):
        self.payload = {'message': message,
                   'stickerPackageId': sticker_pkg_id,
                   'stickerId': sticker_id}
        self.files = {}
        if image != None:
            self.files = {'imgFile': open(image, 'rb')}

    def run(self):
        while True:
            check_ssh = subprocess.Popen('netstat | grep ssh', stdout=subprocess.PIPE, shell=True)
            check_ssh_stdout = str(check_ssh.stdout.read())
        if 'ESTABLISHED' in check_ssh_stdout:
                self.dataToSend('Your computer has been accessed through SSH!')
                request = requests.post(self.url, headers=self.headers,
                                          data=self.payload,
                                          files=self.files)
            sleep(self.freq)

if __name__ == '__main__':
    access_token = 'Your access token here!'
    bot = InformSSH(access_token)

    bot.run()
