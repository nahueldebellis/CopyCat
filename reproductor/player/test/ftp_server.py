from ftplib import FTP
import os
import wave
from io import BytesIO

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'europa.wav')

def server():
    print(TESTDATA_FILENAME)
    ftp = FTP()
    ftp.set_debuglevel(2)
    ftp.connect('ftp', 21)
    ftp.set_pasv(False)
    ftp.login('username','mypass')
    binary_data = b''
    
    
    with open(TESTDATA_FILENAME, 'rb') as data:
        binary_data = data.read()
    song = BytesIO(binary_data)
    ftp.storbinary('STOR %s.wav' % 'europa', song)

server()
