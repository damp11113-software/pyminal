import logging
import time
from cryptography.fernet import Fernet
logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s] [%(levelname)s] %(message)s')

logging.info('starting pyminal')

logging.info('starting module')
logging.info('start file tools')
from damp11113.file import *
logging.info('start network tools')
from damp11113.network import *
logging.info('start cmd tools')
from damp11113.cmd import *
logging.info('start minecraft tools')
from damp11113.minecraft import *
logging.info('start media tools')
from damp11113.media import *
logging.info('start randoms tools')
from damp11113.randoms import *
logging.info('start sdk_check tools')
from damp11113.check import *
logging.info('start tools')
from damp11113 import *
logging.info('done')

c = color()
p = vlc_player()

def _exit():
    clear()
    c.white()
    logging.info('stop pyminal')
    logging.info('stop module')
    logging.info('stop file tools')
    del sys.modules['damp11113.file']
    logging.info('stop network tools')
    del sys.modules['damp11113.network']
    logging.info('stop cmd tools')
    del sys.modules['damp11113.cmd']
    logging.info('stop minecraft tools')
    del sys.modules['damp11113.minecraft']
    logging.info('stop media tools')
    del sys.modules['damp11113.media']
    logging.info('stop randoms tools')
    del sys.modules['damp11113.randoms']
    logging.info('stop check tools')
    del sys.modules['damp11113.check']
    logging.info('stop tools')
    del sys.modules['damp11113']
    logging.info('done')
    exit()

title('pyminal')
clear()


def main():

    d = input('> ')

    if d == '':
        pass

    #--------------------random---------------------------

    elif d.startswith('rd'):
        command = d.split(' ')[1]
        if command == 'num':
            x = d.split(' ')[2]
            y = d.split(' ')[3]
            print(f'output: {rannum(x, y)}')
        elif command == 'str':
            x = d.split(' ')[2]
            print(f'output: {ranstr(x)}')
        else:
            print("'rd num' to random number"
                  "\n'rd str' to random string")

    #--------------------color---------------------------

    elif d.startswith('color'):
        if d.endswith(' green'):
            c.green()
        elif d.endswith(' red'):
            c.red()
        elif d.endswith(' yellow'):
            c.yellow()
        elif d.endswith(' blue'):
            c.blue()
        elif d.endswith(' purple'):
            c.purple()
        elif d.endswith(' white'):
            c.white()
        elif d.endswith(' black'):
            c.black()
        elif d.endswith(' gray'):
            c.gray()
        else:
            print("'color green' to green"
                  "\n'color red' to red"
                  "\n'color yellow' to yellow"
                  "\n'color blue' to blue"
                  "\n'color purple' to purple"
                  "\n'color white' to white"
                  "\n'color black' to black"
                  "\n'color gray' to gray")

    #--------------------convert---------------------------

    elif d.startswith('cv'):
        command = d.split(' ')[1]
        if command == 'bin2str':
            i = d.split(' ')[2]
            print(f'output: {bin2str(i)}')
        elif command == 'str2bin':
            i = d.split(' ')[2]
            print(f'output: {str2bin(i)}')
        elif command == 'byte2str':
            i = d.split(' ')[2]
            print(f'output: {byte2str(i)}')
        elif command == 'str2int':
            i = d.split(' ')[2]
            print(f'output: {str2int(i)}')
        else:
            print("'convert bin2str' to binary to string"
                  "\n'convert str2bin' to string to binary"
                  "\n'convert byte2str' to byte to string"
                  "\n'convert str2int' to string to int")

    #--------------------------app------------------------

    elif d.startswith('mcstatus'):
        try:
            runpy('./app/mcstatus/main.py')
        except:
            print('fail to open minecraft status')

    elif d.startswith('ytloader'):
        try:
            runpy('./app/ytloader.py')
        except:
            print('fail to open youtube downloader')

    #--------------------encrypt-decrypt--------------------

    elif d.startswith('encrypt'):
        command = d.split(' ')[1]
        if command == 'text':
            i = input('please input text: ')
            try:
                r = Fernet.generate_key()
                e = encryptext(i, r)
                print('output:'
                      f'\ntext: {i}'
                      f'\nto: {byte2str(e)}'
                      f'\nkey: {byte2str(r)}')
            except Exception as e:
                print(e)
        elif command == 'file':
            i = input('please input file path: ')
            try:
                r = Fernet.generate_key()
                e = encrypt(i, r)
                print('output:'
                      f'\nfile: {i}'
                      f'\nto: {byte2str(e)}'
                      f'\nkey: {byte2str(r)}')
            except Exception as e:
                print(e)
        else:
            print("'encrypt text' to encrypt text"
                  "\n'encrypt file' to encrypt file")

    elif d.startswith('decrypt'):
        command = d.split(' ')[1]
        if command == 'text':
            i = input('please input text: ')
            try:
                r = ranstr(25)
                e = decryptext(bytes(i), r)
                print('output:'
                      f'\ntext: {i}'
                      f'\nto: {byte2str(e)}'
                      f'\nkey: {byte2str(r)}')
            except Exception as e:
                print(e)
        elif command == 'file':
            i = input('please input file path: ')
            try:
                r = ranstr(25)
                e = decrypt(i, r)
                print('output:'
                      f'\nfile: {i}'
                      f'\nto: {byte2str(e)}'
                      f'\nkey: {byte2str(r)}')
            except Exception as e:
                print(e)
        else:
            print("'decrypt text' to decrypt text"
                  "\n'decrypt file' to decrypt file")

    #--------------------media---------------------------

    elif d.startswith('media'):
        command = d.split(' ')[1]
        if command == 'play':
            i = d.split(' ')[2]
            try:
                p.load(i)
                p.play()
            except Exception as e:
                print(e)
        elif command == 'playyt':
            i = d.split(' ')[2]
            pf = d.split(' ')[3]
            if i == '':
                print('please input youtube url')
            elif pf == '':
                print('type (best|audio|video)')
            try:
                yt = youtube_stream(i)
                if pf == 'best':
                    p.load(yt.best_stream())
                    p.play()
                elif pf == 'audio':
                    p.load(yt.audio_stream())
                    p.play()
                elif pf == 'video':
                    p.load(yt.video_stream())
                    p.play()
            except Exception as e:
                print(e)
        elif d.endswith(' pause'):
            p.pause()
        elif d.endswith(' stop'):
            p.stop()
        else:
            print("'media play' to load media"
                  "\n'media playyt' to load youtube media"
                  "\n'media pause' to pause and unpause media"
                  "\n'media stop' to stop media")

    #-------------------system---------------------------

    elif d.startswith('time'):
        print(f'output: {clock()}')

    elif d.startswith('cmd'):
        cmd(d.endswith('  '))

    elif d == 'clear':
        clear()

    elif d.startswith('title'):
        t = d.split(' ')[1]
        title(t)

    elif d == 'exit':
        logging.info('exit pyminal')
        time.sleep(1)
        _exit()

    elif d == 'info':
        print('------------------------------------------')
        print('| pyminal')
        print('| version: 2.1')
        print('| author: damp11113')
        print(f'| platform: {osversion(fullversion=True)}')
        print(f'| python version: {pyversion()}')
        print(f"| cpu: {osversion(processor=True)}")
        print('------------------------------------------')

    elif d == 'help':
        print('-----------------decrypt--encrypt-------------------')
        print('| encrypt (text|file)')
        print('| decrypt (text|file)')
        print('-----------------media------------------------------')
        print('| media (play|playyt|pause|stop)')
        print('---------------------app----------------------------')
        print('| mcstatus')
        print('| ytloader')
        print('---------------------random-------------------------')
        print('| rd (str|num)')
        print('---------------------convert-------------------------')
        print('| cv (str2int|byte2str|str2bin|bin2str)')
        print('------------------system----------------------------')
        print('| time')
        print('| cmd')
        print('| color')
        print('| clear')
        print('| title')
        print('| exit')
        print('| info')
        print('-----------------------------------------------------')

    else:
        print(f"command '{d}' not found")

while True:
    main()