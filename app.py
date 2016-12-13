from flask import Flask
from braviarc.braviarc import BraviaRC
from wakeonlan import wol

app = Flask(__name__)


def bravia_client():
    pin = '7793'
    braviarc = BraviaRC("192.168.1.158")
    braviarc.connect(pin, 'my_device_id', 'my device name')
    return braviarc


@app.route('/tv_on')
def tv_on():
    bravia_mac_address = "FC:F1:52:4B:2B:2A"
    wol.send_magic_packet(bravia_mac_address)
    return 'on'


@app.route('/tv_off')
def tv_off():
    bravia_client().turn_off()
    return 'off!'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=11111)