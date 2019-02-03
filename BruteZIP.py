import argparse
from threading import Thread
import zipfile

parser = argparse.ArgumentParser(description="Unzips a password protected .zip by performing a brute-force attack using either a word list, password list or a dictionary.", usage="BruteZIP.py -z zip.zip -f file.txt")
parser.add_argument("-z", "--zip", metavar="", required=True, help="Location and the name of the .zip file.")  # Creates -z arg
parser.add_argument("-f", "--file", metavar="", required=True, help="Location and the name of the word list/password list/dictionary.")  # Creates -f arg
args = parser.parse_args()


def extract_zip(zip_file, password):
    try:
        zip_file.extractall(pwd=password)
        print("[+] Password for the .zip: {0}".format(password.decode("utf-8")) + "\n")
    except:
        pass  # If a password fails, it moves to the next password without notifying the user. If all passwords fail, it will print nothing in the command prompt.


def main(zip, file):
    if (zip == None) | (file == None):
        print(parser.usage)  # If the args are not used, it displays how to use them to the user.
        exit(0)
    zip_file = zipfile.ZipFile(zip)
    txt_file = open(file, "rb")  # Opens the word list/password list/dictionary in "read binary" mode.
    for line in txt_file:
        password = line.strip()
        t = Thread(target=extract_zip, args=(zip_file, password))
        t.start()


if __name__ == '__main__':
    main(args.zip, args.file)  # BruteZIP.py -z zip.zip -f file.txt.