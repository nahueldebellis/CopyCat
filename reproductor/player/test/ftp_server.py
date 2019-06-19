from ftplib import FTP
import os
import wave
from io import BytesIO

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'europa.wav')

def server():
    ftp = FTP(host='ftp_songs')
    ftp.login(user='copycat', passwd='quetepasaman1234')
    with open(TESTDATA_FILENAME, 'rb') as data:
        binary_data = data.read()
    song = BytesIO(binary_data)
    ftp.storbinary('STOR %s.wav' % 'test_song', song)

server()
