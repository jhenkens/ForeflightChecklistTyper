import csv

import sys
from websocket import create_connection
import time

with open('data.csv', mode='r') as infile:
    datas = [row for row in csv.DictReader(infile)]
host = "ws://192.168.11.204:8307/service"


def send_data(str):
    i_try = 0
    ws = None
    while i_try < 3000:
        try:
            ws = create_connection("ws://192.168.11.204:8307/service", 10000)
            break
        except:
            i_try += 1
            if i_try % 50 == 0:
                print("still trying to connect")
            time.sleep(0.25)
            continue

    time.sleep(0.1)
    ws.recv()
    time.sleep(0.1)
    if str:
        ws.send(str)
        result = ws.recv()
        if result != 'ok':
            raise "Received not ok! " + result
    while ws.connected:
        try:
            ws.ping()
            time.sleep(0.25)

        except:
            time.sleep(1)
            break


ready = False
for data in datas:
    if data["challenge"] == 'Alternator Belt':
        ready = True
        continue
    if not ready:
        continue
    if not data["challenge"]:
        continue
    print("starting " + str(data))
    if data["challenge"] == "section":
        print("Starting new section... Press Enter when ready")
        sys.stdin.readline()
        send_data(data["response"])
        print("Back to check item... Press Enter when ready")
        sys.stdin.readline()
        continue

    send_data(data["challenge"])
    send_data(data["response"])
    send_data(data["notes"])
    # print("ready?")
    # sys.stdin.readline()
