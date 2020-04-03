<p align="left">
    <a href="https://github.com/Arszilla/BruteZIP/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/Arszilla/BruteZIP.svg?color=green&logo=github">
    </a>
    <a href="https://github.com/Arszilla/BruteZIP/stargazers">
        <img src="https://img.shields.io/github/stars/Arszilla/BruteZIP.svg?color=yellow&logo=github">
    </a>
    <a href="http://www.python.org/download/">
        <img src="https://img.shields.io/badge/Python-3+-yellow.svg?color=blue&logo=python&logoColor=white">
    </a>
</p>

# BruteZIP
A basic script that unzips password protected .zips by performing a brute-force attack using either a word list, 
password list or a dictionary. 

Based on _Violent Python - A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers_ by 
TJ O'Connor.

## Requirements
- Python 3+

## Information
To run the script just launch the .py using `python3 BruteZIP.py -p poolsize -z zip.zip -f file.txt` where:

- `-p poolsize` is optional and specifies the poolsize (How many instances of Python to create to brute-force the 
.zip [More is better but requires more resources]). If you want to use the default amount of processes (8), don't input
`-p` while launching the program.
- `-z zip.zip` is the location and name of the target .zip.
- `-f file.txt` is the location and the name of the word list/password list/dictionary.

Due to the difference in compression methods in 7zip and WinRAR, `zipfile` often has troubles unzipping/cracking WinRAR 
generated .zips. For best results, use this on .zips generated using "deflate" compression method (Preferably generated 
with 7zip).

This project and the files shared along with the project are for educational purposes **ONLY**.

## Acknowledgements
- TJ O'Connor for his code and work in his book _Violent Python - A Cookbook for Hackers, Forensic Analysts, 
Penetration Testers and Security Engineers_.

- [Ayushman "DamianWayne17" Dubey](https://github.com/DamianWayne17).

## Disclaimer
This project and the files shared along with the project are for educational purposes **ONLY**. As the MIT License 
states:

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._