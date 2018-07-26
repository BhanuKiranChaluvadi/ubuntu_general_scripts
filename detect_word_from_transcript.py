#!/usr/bin/python

import csv
import re  # for case insensitivity search
import argparse
import os.path
from subprocess import call

# Example run
"""
python main.py \
--input_csv_path=/home/bc/Downloads/dataset/tatoeba_audio_eng/sentences_with_audio.csv \
--search_word=save \
--audio_file_path=/home/bc/Downloads/dataset/tatoeba_audio_eng/audio/CK \
--copy_path=/home/bc/Downloads/dataset/save

"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_csv_path', '-i',
        type=str,
        help="""\
        Where to find the input csv file.
        """)
    parser.add_argument(
        '--search_word', '-s',
        type=str,
        help="""\
        What search word to find.
        """)
    parser.add_argument(
        '--audio_file_path', '-a',
        type=str,
        help="""\
        Where the source audio files exist.
        """)
    parser.add_argument(
        '--copy_path', '-c',
        type=str,
        help="""\
        Where to copy the audio files.
        """)

    args = parser.parse_args()

    # mainer
    with open(args.input_csv_path, 'rb') as csvfile:
        audio_files_reader = csv.reader(csvfile, delimiter='\t')

        # header = ['id', 'username', 'text']
        for row in audio_files_reader:
            sentence = row[2]
            if re.search(args.search_word, sentence, re.IGNORECASE):
                file_name = row[0] + ".mp3"
                call(["cp", os.path.join(args.audio_file_path, file_name), args.copy_path])
