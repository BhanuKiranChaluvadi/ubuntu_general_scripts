#!/usr/bin/python
import csv
import re  # for case insensitivity search
import argparse
import os.path
from subprocess import call

# Example run
# cd Desktop/laptics/find_audio/
"""
python main.py \
--input_csv_path=/home/bc/Downloads/dataset/tatoeba_audio_eng/sentences_with_audio.csv \
--audio_file_path=/home/bc/Downloads/dataset/tatoeba_audio_eng/audio/CK \
--search_word=save \
--copy_path=/home/bc/Downloads/dataset

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

        # search_word = args.search_word
        search_word = " ?"+search_word+"\W"   # To avoid other strings containing this string.
        saved_path = os.path.join(args.copy_path, args.search_word)
        call(["mkdir", "-p", saved_path])

        # header = ['id', 'username', 'text']
        for row in audio_files_reader:
            sentence = row[2]
            if re.search(search_word, sentence, re.IGNORECASE):
                file_name = row[0] + ".mp3"                
                call(["cp", os.path.join(args.audio_file_path, file_name), saved_path])
                
