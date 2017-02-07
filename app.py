from flask import Flask
from braviarc.braviarc import BraviaRC
from wakeonlan import wol
import os


app = Flask(__name__)

try:
    bravia_pin = os.environ['BRAVIA_PIN']
except:
    bravia_pin = '7793'

try:
    bravia_ip = os.environ['BRAVIA_IP']
except:
    bravia_ip = "192.168.1.158"

try:
    bravia_mac_address = os.environ['BRAVIA_MAC']
except:
    bravia_mac_address =  "FC:F1:52:4B:2B:2A"


def bravia_client():
    braviarc = BraviaRC(bravia_ip)
    braviarc.connect(pin, 'my_device_id', 'my device name')
    return braviarc


@app.route('/tv_on')
def tv_on():
    wol.send_magic_packet(bravia_mac_address)
    return 'on'


@app.route('/tv_off')
def tv_off():
    bravia_client().turn_off()
    return 'off!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11111)