import subprocess
import sys
from collections import Counter
from os import listdir
from os.path import isfile, join


def analyze_files(path):
    try:
        files = [f for f in listdir(path) if isfile(join(path, f))]
        results = []

        for file in files:
            proc = subprocess.run(['python', 'lab_4_3_analyze.py'], input=str.encode(path + '/' + file),
                                  capture_output=True)
            output_lines = (proc.stdout.decode('utf-8')).split('\n')

            if len(output_lines) > 1:
                keys = output_lines[0].split(',')
                values = output_lines[1].split(',')
                csv_as_dict = {}

                for i in range(len(keys)):
                    csv_as_dict[keys[i]] = values[i]

                results.append(csv_as_dict)

        analyze_results(results)
    except (FileNotFoundError, NotADirectoryError):
        print('Invalid path')


def analyze_results(results):
    read_files = len(results)
    total_chars = sum(int(r['number of chars']) for r in results)
    total_words = sum(int(r['number of words']) for r in results)
    total_lines = sum(int(r['number of lines']) for r in results)
    most_common_char = get_most_common_char(results)
    most_common_word = get_most_common_word(results)

    print(f'Read files: {read_files}')
    print(f'Total chars: {total_chars}')
    print(f'Total words: {total_words}')
    print(f'Total lines: {total_lines}')
    print(f'Most common char: {most_common_char}')
    print(f'Most common word: {most_common_word}')


def get_most_common_char(results):
    char_counts = Counter()

    for r in results:
        with open(r['path'], "r") as file:
            content = file.read()
            char_counts.update(Counter(content))

    return char_counts.most_common(1)[0][0]


def get_most_common_word(results):
    word_counts = Counter()

    for r in results:
        with open(r['path'], "r") as file:
            content = file.read()
            word_counts.update(Counter(content.split()))

    return word_counts.most_common(1)[0][0]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        analyze_files(sys.argv[1])
    else:
        print('Invalid number of arguments')
