from ftplib import FTP
import os
from wave import open as open_wav

def server():
    ftp = FTP(host='ftp_songs')
    ftp.login(user='copycat', passwd='quetepasaman1234')
    with open_wav('europa.wav', 'rb') as data:
        binary_data = data.readframes(data.getnframes())
    ftp.storbinary('STOR %s' % '/home.ftpusers/copycat/song', binary_data, 1024)

server()
