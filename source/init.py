import chardet

def check_encoding(filepath):
    detector = chardet.UniversalDetector()
    with open(filepath, mode="rb") as f:
        for binary in f:
            detector.feed(binary)
            if detector.done:
                break
    detector.close()
    print(detector.result, end='')
    print(detector.result['encoding'])

def main():
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_sjis1.txt")
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_utf-8.txt")


#test
if __name__ == "__main__":
    print("start")
    main()
    input("press any key...")