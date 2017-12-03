#!/usr/bin/python3
# encoding: utf-8

"""Simple script to convert pictures to html base64 encoded.
Usage:
  - run this module without arguments --> get help
  - run with '--inputfile' or '-i' --> will select the picture to be converted - Must be set!
  - run with '--outputfile' or '-o' --> will select the outfile to store the results
  - run with '--clipboard' or '-c' --> will copy the result to the clipboard too for easy paste
  - run with '--help' or '-h' --> shows standard help message
"""
import pyperclip
import textwrap
import argparse
import base64
from os import listdir
from os.path import isfile, join

onlyfiles = [files for files in listdir('.') if isfile(join(files))]
print("Lista fisiere din directorul curent: ", onlyfiles)


def main():
    parser = argparse.ArgumentParser(
        prog='pictobase64.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Pic_____      ______                    ____________ __
           __  /_________  /_______ ______________  ___/_  // /
           _  __/  __ \_  __ \  __ `/_  ___/  _ \  __ \_  // /_
           / /_ / /_/ /  /_/ / /_/ /_(__  )/  __/ /_/ //__  __/
           \__/ \____//_.___/\__,_/ /____/ \___/\____/   /_/     by (a) n(o)ob
                 '''),
        epilog='''Simple script to convert pictures to html base64 encoded.''')
    parser.add_argument('-i', '--inputfile', help='select picture', required=True)  # required param
    parser.add_argument('-o', '--outputfile', help='select output file')  # optional param
    parser.add_argument('-c', default=0, help='copy result to clipboard for easy paste')  # optional param
    args = parser.parse_args()

    if args.inputfile:
        print('Input file is -->', args.inputfile)
        with open(args.inputfile, "rb") as f:
            encodedzip = base64.b64encode(f.read())
            if args.outputfile:
                print('Output file is -->', args.outputfile)
                with open(args.outputfile, "a") as newf:
                    newf.write('<img src="data:image/gif;base64, {}" />'.format(encodedzip.decode()))
                    pass
                    if args.c is not 0:
                        pyperclip.copy('<img src="data:image/gif;base64, {}" />'.format(encodedzip.decode()))
            else:
                print('<img src="data:image/gif;base64, ', encodedzip.decode(), '" />')
                if args.c is not 0:
                    pyperclip.copy('<img src="data:image/gif;base64, {}" />'.format(encodedzip.decode()))

if __name__ == "__main__":
    main()