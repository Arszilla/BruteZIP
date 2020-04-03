import argparse
import multiprocessing
import os
import shutil
import tempfile
from zipfile import ZipInfo, ZipFile

parser = argparse.ArgumentParser(description="Unzips a password protected .zip by performing a brute-force attack "
                                             "using either a word list, password list or a dictionary.",
                                 usage="BruteZIP.py -p poolsize -z zip.zip -f file.txt")
# Creates -p arg
parser.add_argument("-p", "--poolsize", metavar="", required=False, type=int, default=8, help="Determines how many "
                                                                                              "instances of Python to "
                                                                                              "be created. More is "
                                                                                              "better but will use "
                                                                                              "more CPU and memory.")
# Creates -z arg
parser.add_argument("-z", "--zip", metavar="", required=True, help="Location and the name of the .zip file.")
# Creates -f arg
parser.add_argument("-f", "--file", metavar="", required=True, help="Location and the name of the word list/password "
                                                                    "list/dictionary.")
args = parser.parse_args()


class Zipped(ZipFile):
    def _extract_member(self, member, targetpath, pwd):
        # Extract the ZipInfo object 'member' to a physical  file on the path targetpath.

        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        # Build the destination pathname, replacing forward slashes to platform specific separators.
        arcname = member.filename.replace('/', os.path.sep)

        if os.path.altsep:
            arcname = arcname.replace(os.path.altsep, os.path.sep)
        # Interpret absolute pathname as relative, remove drive letter or UNC path, redundant separators,
        # "." and ".." components.
        arcname = os.path.splitdrive(arcname)[1]
        invalid_path_parts = ('', os.path.curdir, os.path.pardir)
        arcname = os.path.sep.join(x for x in arcname.split(os.path.sep)
                                   if x not in invalid_path_parts)
        if os.path.sep == '\\':
            # Filter illegal characters on Windows
            arcname = self._sanitize_windows_name(arcname, os.path.sep)

        targetpath = os.path.join(targetpath, arcname)
        targetpath = os.path.normpath(targetpath)

        # Create all upper directories if necessary.
        upperdirs = os.path.dirname(targetpath)
        if upperdirs and not os.path.exists(upperdirs):
            os.makedirs(upperdirs)

        if member.is_dir():
            if not os.path.isdir(targetpath):
                os.mkdir(targetpath)
            return targetpath

        with self.open(member, pwd=pwd) as source:
            if pwd:
                dirname = os.path.dirname(targetpath)
                basename = os.path.basename(targetpath)
                idx = basename.rfind(".")
                if idx != -1:
                    prefix, suffix = basename[:idx], basename[idx:]
                else:
                    prefix, suffix = basename, ""
                fid, tmptargetpath = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=dirname)
                with open(fid, "wb") as target:
                    try:
                        shutil.copyfileobj(source, target)
                    except:
                        target.close()
                        os.unlink(tmptargetpath)
                        raise
                shutil.move(tmptargetpath, targetpath)
            else:
                with open(targetpath, "wb") as target:
                    shutil.copyfileobj(source, target)
        return targetpath


def extract_zip(zip_filename, password):
    try:
        zip_file = Zipped(zip_filename)
        zip_file.extractall('Extracted', pwd=password)
        print(f"[+] Password for the .zip: {password.decode('utf-8')}")
    except:
        # If a password fails, it moves to the next password without notifying the user.
        # If all passwords fail, it will print nothing in the command prompt.
        pass


def main(poolsize, zip, file):
    if (zip == None) | (file == None):
        # If the args are not used, it displays how to use them to the user.
        print(parser.usage)
        exit(0)
    # Opens the word list/password list/dictionary in "read binary" mode.
    txt_file = open(file, "rb")
    # Allows 8 or more instances of Python to be ran simultaneously.
    with multiprocessing.Pool(poolsize) as pool:
        # "starmap" expands the tuples as 2 separate arguments to fit "extract_zip"
        pool.starmap(extract_zip, [(zip, line.strip()) for line in txt_file])


if __name__ == '__main__':
    # BruteZIP.py -p poolsize -z zip.zip -f file.txt.
    main(args.poolsize, args.zip, args.file)
