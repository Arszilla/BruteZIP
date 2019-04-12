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
A small program that unzips password protected .zips by performing a brute-force attack using either a word list, 
password list or a dictionary. 

Based on _Violent Python - A Cookbook for Hackers, Forensic Analysts, Penetration Testers and Security Engineers_ by 
TJ O'Connor.

## Requirements
- Python 3+

## Information
To run the script just launch the .py using `python BruteZIP.py -p poolsize -z zip.zip -f file.txt` where:

- `-p poolsize` is optional and specifies the poolsize (How many instances of Python to create to brute-force the 
.zip [More is better but requires more resources]). If you want to use the default amount of processes (8), don't input
`-p` while launching the program.
- `-z zip.zip` is the location and name of the target .zip.
- `-f file.txt` is the location and the name of the word list/password list/dictionary.

There was a bug in `zipfile` that is solved in this program. The bug fix was written by [CristiFati]
(https://github.com/CristiFati) in [this](https://github.com/python/cpython/pull/12242) pull/merge request but it was 
rejected/closed since 3.6 is in security-fix-only mode. Thus as a work-around I super'd the function in `BruteZIP.py` 
to make it universal for any user; that way your `zipfile.py` is fixed when using 
`BruteZIP.py`.

Due to the difference in compression methods in 7zip and WinRAR, `zipfile` often has troubles unzipping/cracking WinRAR 
generated .zips. For best results, use this on .zips generated using "deflate" compression method (Preferably generated 
with 7zip).

I have placed 14 word lists/password lists/dictionaries in `Word Lists-Password Lists-Dictionaries.zip`. Majority are 
them are from [Skull Security](skullsecurity.org/)'s wiki; where he has more of these, but I chose a handful of them 
that I find useful. 

This project and the files shared along with the project are for educational purposes **ONLY**.

Written with Python 3.7.

## Acknowledgements
- TJ O'Connor for his code and work in his book _Violent Python - A Cookbook for Hackers, Forensic Analysts, 
Penetration Testers and Security Engineers_.

- [Ayushman "DamianWayne17" Dubey](https://github.com/DamianWayne17) for his amazing debugging skills.

- [CristiFati](https://github.com/python/cpython/pull/12242) for finding a solution to my code breaking bug.

- [Skull Security](skullsecurity.org/) for the word lists/password lists/dictionaries. Majority of the word 
lists/password lists/dictionaries in this project are from his wiki.

## Disclaimer
This project and the files shared along with the project are for educational purposes **ONLY**. As the MIT License 
states:

_THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE._

## Donations
If you'd like to donate to me use one of these two methods please:

**Bitcoin Cash:** [bitcoincash:qppxw4t8zqm4cp8gpvaldx4sur2f4e8wvgqecnl4ld](https://i.imgur.com/rwIhn3b.png)

**Bitcoin:** [1FBGXoAMSEmZwnbzyjQ81eo72EGU8hjV7A](https://i.imgur.com/6wxQ9G0.png)
