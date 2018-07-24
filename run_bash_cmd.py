#!/usr/bin/python
import argparse
import os.path
from subprocess import call

# cd /home/bc/Desktop/laptics/run_cmd
# python main.py --input_dir=/home/bc/converted_audio/recordings --output_dir=/home/bc/converted_audio/loudest_section

# --input_dir=/home/bc/converted_audio/recordings
# --output_dir=/home/bc/converted_audio/loudest_section

os.chdir("/tmp/extract_loudest_section/gen/bin")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_dir', '-i',
        type=str,
        help="""\
        Where to find the input files.
        """)
    parser.add_argument(
        '--output_dir', '-o',
        type=str,
        help="""\
        Where to save the output files.
        """)

    args = parser.parse_args()

    for file in os.listdir(args.input_dir):
        if file.endswith(".wav") and not os.path.exists(os.path.join(args.input_dir, file)):
            # Function call
            # call(["ls", "-l"])
            # call(["pwd"])
            call(["./extract_loudest_section", os.path.join(args.input_dir, file), args.output_dir])
