#!/usr/bin/env python3
from nltk.tokenize import word_tokenize
from collections import Counter

def count(files):
    return [f"{count}\t{word}" for (word, count) in Counter(words(files)).items()]

def words(files):
    return word_tokenize("".join(file.read().lower() for file in files))

if __name__ == '__main__':
    from argparse import ArgumentParser, FileType
    from pathlib import Path
    parser = ArgumentParser()
    parser.add_argument(
            "--count", "-c", dest="fun", action="store_const", default=words, const=count
    )
    parser.add_argument("file", nargs="+", type=FileType("r"))
    args = parser.parse_args()
    print(
            *args.fun(args.file),
            sep="\n", 
            end=""
    )
