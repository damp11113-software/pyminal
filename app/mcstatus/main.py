import logging
logging.basicConfig(level=logging.DEBUG)
logging.info('waitting')

try:
    from PyQt5 import uic
    from PyQt5.QtWidgets import QWidget, QApplication
    import sys
    from damp11113.minecraft import mcstatus
    logging.info('import success')
except Exception as e:
    logging.info('import failed')
    logging.info('installing')
    import os
    os.system('pip install PyQt5')
    logging.info('install success')
    raise e




logging.info('start')

class Status(QWidget):
    def __init__(self):
        super(Status, self).__init__()
        uic.loadUi('./app/mcstatus/ui/status.ui', self)
        self.setWindowTitle(f'Server Status - status - {ip}')
        self.show()
        logging.info('check status')
        self.check()
        self.more.clicked.connect(self._show)
        self.refresh.clicked.connect(self.check)
        self.exit.clicked.connect(self._exit)

    def _show(self):
        logging.info('show')
        ex2.show()
        self.close()

    def _exit(self):
        logging.info('exit')
        QApplication.quit()

    def check(self):
        self.status.setText('Checking...')
        logging.info('checking...')
        try:
            xs = mcstatus(ip)
            xs.raw()
            logging.info('checked')
            self.status.setText('Server Online')
            self.connect.setText('<--->')
            self.setWindowTitle(f'Server Status - status - {ip} - online')
            self.ip.setText(f'IP: {ip}')

            logging.info('server online')
        except:
            logging.info('checked')
            self.status.setText('Server Offline')
            self.connect.setText('<-X->')
            self.setWindowTitle(f'Server Status - status - {ip} - offline')
            self.ip.setText(f'IP: {ip}')
            logging.info('server offline')

class details(QWidget):
    def __init__(self):
        super(details, self).__init__()
        uic.loadUi('./app/mcstatus/ui/details.ui', self)
        self.setWindowTitle(f'Server Status - details - {ip}')
        self.check()
        self.back.clicked.connect(self._back)
        self.refresh.clicked.connect(self.check)

    def _back(self):
        logging.info('back')
        ex.show()
        self.close()

    def check(self):
        try:
            logging.info('checking...')
            s = mcstatus(ip)
            self.des.setText(f'Description: {s.description()}')
            self.player.setText(f'Player: {s.players().online}/{s.players().max}')
            self.ping.setText(f'Ping {s.ping()} ms')
            self.favicon.setText(f'Favicon: {s.favicon()}')
            self.version.setText(f'Version: {s.version().name}')
            self.proversion.setText(f'Protocol Version: {s.version().protocol}')
            self.ip.setText(f'IP: {ip}')
            self.status.setText(f'Server Online')
            self.setWindowTitle(f'Server Status - details - {ip} - online')
            logging.info('checked')
            logging.info('server online')
        except Exception as e:
            logging.info('checked')
            self.des.setText('')
            self.player.setText('')
            self.ping.setText('')
            self.favicon.setText('')
            self.version.setText('')
            self.proversion.setText('')
            self.ip.setText(f'IP: {ip}')
            self.status.setText('Server Offline')
            self.setWindowTitle(f'Server Status - details - {ip} - offline')
            logging.info('server offline')
            logging.info(e)

if __name__ == '__main__':
    print('')
    print('------------------------')
    print('Server Status V1.5')
    print('Developed by: damp11113')
    print('------------------------')
    print('')
    print('------------------------')
    ip = input("Enter server ip: ")
    print('------------------------')
    print('')
    print('starting...')
    app = QApplication(sys.argv)
    ex = Status()
    ex2 = details()
    logging.info('started')
    sys.exit(app.exec_())