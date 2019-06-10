from ftplib import FTP
from wave import open as open_wav

def server():
    ftp = FTP(host='ftp_songs')
    login_status = ftp.login(user='copycat', passwd='quetepasaman1234')
    with open_wav('europa.wav', 'rb') as data:
        binary_data = data.readframes(data.getnframes())
    ftp.storbinary('STOR %s' % os.path.basename("europa.wav"), binary_data, 1024)
    fp.close()

server()
