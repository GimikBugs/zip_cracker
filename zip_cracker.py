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
    parser = optparse.OptionParser("Usage: -f <zipfile> -d <dictionary>")

    parser.add_option('-f', dest='zip_file', type='string', help='specify the zip file')
    parser.add_option('-d', dest='dictionary', type='string', help='specify the dictionary file')
    (options, arg) = parser.parse_args()
    if (options.zip_file == None) | (options.dictionary == None):
        print(parser.usage)
        exit(0)
    else:
        zip_file = options.zip_file
        dictionary = options.ditionary

    zFile = zipfile.ZipFile(zip_file)
    passFile = open(dictionary)

    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extract_zip, args=(zFile, password))
        t.start()

print('f')
if __name__ == '__main__':
    Main()
