#!/usr/bin/env python3
from nltk.tokenize import sent_tokenize

if __name__ == '__main__':
        from argparse import ArgumentParser, FileType
        from pathlib import Path
        parser = ArgumentParser()
        parser.add_argument("file", nargs="+", type=FileType("r"))
        args = parser.parse_args()
        print(
                *sent_tokenize("".join(file.read().lower() for file in args.file)), 
                sep="\n", 
                end=""
        )
