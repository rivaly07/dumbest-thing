#!/usr/bin/env python3
import os
import sys
import hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

LINE = "It retried the make.fun kit endpoint for forty straight minutes printing \u201ckit pending\u201d, then marked the bounty hopeless \u2014 two minutes before it finally answered."

def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, 'entry.txt')

    with open(output_path, 'w', encoding='utf-8', newline='') as f:
        f.write(LINE)

    char_count = len(LINE)
    sha256 = hashlib.sha256(LINE.encode('utf-8')).hexdigest()
    print(f"chars: {char_count}")
    print(f"sha256: {sha256}")

if __name__ == '__main__':
    main()