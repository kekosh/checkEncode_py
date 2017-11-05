import chardet

def check_encoding(filepath):
    ''' analyze files encoding args[filepath] '''
    detector = chardet.UniversalDetector()
    with open(filepath, mode="rb") as file:
        for binary in file:
            detector.feed(binary)
            #if all bynary data was readed,loop will end
            if detector.done:
                break
    detector.close()

    #detector-feed process result is return dictionaly style data
    print(detector.result, end='')
    print(detector.result['encoding'])

def enumerate_files(directory):
    ''' list of analyze target file '''
    import os
    files = os.listdir(directory)


def main():
    ''' init process nothing arguments '''
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_sjis1.txt")
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_utf-8.txt")


#test
if __name__ == "__main__":
    print("start")
    main()
    input("press any key...")