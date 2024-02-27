#!/usr/bin/env python3
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from words import words

def main(target_file, baseline_files):
    dictionary = Counter(words(baseline_files))
    word_list = words((target_file,))
    return buzz(word_list, dictionary)

def buzz(word_list, dictionary):
    word_counts = Counter(word_list)
    return [(word, word_counts[word]/dictionary[word]) for word in set(word_list)]

def score(sentence, buzz_words):
    return max(freq for (word,freq) in buzz_words if word in sentence)

def buzz_sentences(target_file, baseline_files):
    dictionary=Counter(words(baseline_files))
    text = target_file.read().lower()
    buzzwords = buzz(word_tokenize(text), dictionary)
    sentences = sent_tokenize(text)
    results = [(sentence, score(sentence, buzzwords), ) for sentence in sentences]
    return results

if __name__ == '__main__':
    from argparse import ArgumentParser, FileType
    from pathlib import Path
    parser = ArgumentParser()
    parser.add_argument(
            "-s", "--sentences",
            dest="fun",
            action="store_const", 
            const=buzz_sentences, 
            default=main
        )
    parser.add_argument("target_file", type=FileType("r"))
    parser.add_argument("baseline", nargs="+", type=FileType("r"))
    args = parser.parse_args()
    results = args.fun(args.target_file, args.baseline)
    for (word, freq) in results:
        print(freq, word)

