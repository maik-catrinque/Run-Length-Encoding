from re import sub
import argparse

def encode(text):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),text)

def decode(text):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Lenth Encoding.')
    parser.add_argument('-f','--file', dest="file", type=str,required=True,
                        help="Indicate the file to encode")
    parser.add_argument('-e','--encode', dest="encode",action='store_true',
                        help="Indicate to encode the file")
    parser.add_argument('-d','--decode', dest="decode",action='store_true',
                        help="Indicate to decode the file")
    args = parser.parse_args()


    if args.encode:
        file = open(args.file,'r')
        text = file.read()
        file_out = open(args.file + '.encoded','w')
        file_out.write(encode(text))

    elif args.decode:
        file = open(args.file,'r')
        text = file.read()
        file_out = open(args.file + '.decoded','w')
        file_out.write(decode(text))
