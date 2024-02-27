#!/usr/bin/env python3
from nltk.tokenize import word_tokenize

if __name__ == '__main__':
        from sys import stdin, argv
        print(
                *word_tokenize("".join(argv.get(0, stdin).read().lower() for file in args.file)), 
                sep="\n", 
                end=""
        )
