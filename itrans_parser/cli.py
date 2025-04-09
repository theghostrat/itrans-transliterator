import argparse
from .transliterator import Transliterator

def main():
    parser = argparse.ArgumentParser(description="ITRANS to Unicode Transliterator")
    parser.add_argument('input', nargs='?', help="Input text or path to input file")
    parser.add_argument('-s', '--script', default='Devanagari', help="Target script (default: Devanagari)")
    parser.add_argument('-f', '--file', action='store_true', help="Treat input as file path")
    parser.add_argument('-o', '--output', help="Output file (default: stdout)")

    args = parser.parse_args()

    # Read input
    if args.file:
        with open(args.input, 'r', encoding='utf-8') as f:
            input_text = f.read()
    else:
        input_text = args.input

    # Transliterate
    transliterator = Transliterator(script=args.script)
    output_text = transliterator.transliterate(input_text)

    # Output result
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_text)
    else:
        print(output_text)

if __name__ == "__main__":
    main()