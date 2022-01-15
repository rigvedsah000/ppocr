import json
import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser('Convert annotation files from MMOCR to PP-OCR')
    parser.add_argument('input', type=str, help='MMOCR annotation file path')
    parser.add_argument('output', type=str, help='Output folder path')
    args = parser.parse_args()

    return args


def mmocr2ppocr():
    args = parse_args()

    in_file = open(args.input, 'r', encoding='utf8')
    lines = in_file.readlines()
    total = len(lines)

    out_file = open(os.path.join(args.output, 'gt_ppocr.txt'), 'w', encoding='utf8')

    print('Starting...')

    for i, line in enumerate(lines):

        in_json = json.loads(line)
        annotations = []

        for ann in in_json['annotations']:
            seg = ann['segmentation'][0]
            points = [ [seg[0], seg[1]], [seg[2], seg[3]], [seg[4], seg[5]], [seg[6], seg[7]] ]

            annotations.append(dict(transcription="NA", points=points))

        out_file.write(in_json['file_name'] + '\t' + json.dumps(annotations) + '\n')

        if i % 2 == 0:
            print(f'Processed {i}/{total}')

    out_file.close()
    print('Done!')


if __name__ == '__main__':
    mmocr2ppocr()
