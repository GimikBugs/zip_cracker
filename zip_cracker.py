import optparse
import zipfile
from threading import Thread


def extract_zip(filename, password):
    with zip(filename) as zFile:
        try:
            password_encoded = bytes(password.encode('utf-8'))
            zFile.setpassword(password_encoded)
            zFile.testzip()
            print("[+] Password Found: " + password + '\n')
        except:
            pass


def Main():
    parser = optparse.OptionParser("usage & prog " + \
                                   "-f <zipfile> -d <dictionary>")

    parser.add_option('-f', dest='zname', type='string', \
                      help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', \
                      help='specify dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print(parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()


if __name__ == '__main__':
    Main()
