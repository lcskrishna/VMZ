import os
import sys
import argparse

def parse_log_files(log_file):
    fs = open(log_file, 'r')
    lines = fs.readlines()
    fs.close()

    clips_sec = []
    for j in range(len(lines)):
        line = lines[j].rstrip()
        if 'clips/sec' in line:
            split_line = line.split(' ')
            for i in range(len(split_line)):
                if 'clips/sec' in split_line[i]:
                    val = split_line[i - 1].replace('(', '')
                    clips_sec.append(float(val))

    return clips_sec

def print_clips_sec(clips_sec):
    total_sum = 0
    total_count = 0
    for i in range(1, len(clips_sec)):
        total_sum = total_sum + clips_sec[i]
        total_count = total_count + 1

    print ("INFO: Average Clips/sec value is : {}".format(total_sum/total_count))

def main():
    log_file = args.log_file
    clips_sec = parse_log_files(log_file)
    print_clips_sec(clips_sec)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log-file', type=str, required=True, help="Log file after running training")
    args = parser.parse_args()

    main()
