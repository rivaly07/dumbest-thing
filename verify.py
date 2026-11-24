#!/usr/bin/env python3
import os
import sys
import tempfile
import subprocess

def run_main(output_dir):
    env = os.environ.copy()
    env['MAKEFUN_OUTPUT_DIR'] = output_dir
    result = subprocess.run([sys.executable, 'main.py'], capture_output=True, text=True, env=env, cwd=os.path.dirname(os.path.abspath(__file__)))
    if result.returncode != 0:
        raise RuntimeError(f"main.py failed: {result.stderr}")
    return result.stdout.strip()

def read_entry(output_dir):
    path = os.path.join(output_dir, 'entry.txt')
    with open(path, 'rb') as f:
        return f.read()

def main():
    with tempfile.TemporaryDirectory() as dir1, tempfile.TemporaryDirectory() as dir2:
        out1 = run_main(dir1)
        out2 = run_main(dir2)

        data1 = read_entry(dir1)
        data2 = read_entry(dir2)

        if data1 != data2:
            print("FAIL: outputs are not byte-identical")
            sys.exit(1)

        text = data1.decode('utf-8')
        char_count = len(text)

        if not (1 <= char_count <= 200):
            print(f"FAIL: character count {char_count} not in 1..200")
            sys.exit(1)

        if text.strip() == '' or text.isspace():
            print("FAIL: entry is only whitespace")
            sys.exit(1)

        if '\n' in text:
            print("FAIL: entry contains newline")
            sys.exit(1)

        print("OK: byte-identical")
        print(f"OK: {char_count} characters")
        print("OK: not whitespace-only")
        print("OK: single line")
        print(out1)
        print(out2)

if __name__ == '__main__':
    main()