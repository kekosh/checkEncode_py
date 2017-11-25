""" check file Encode """
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

def enumerate_filepath(directory):
    ''' list of analyze target file '''
    import os
    objects = os.listdir(directory)
    files = []
    for path in objects:
        file_absolutepath = os.path.join(directory, path)
        if os.path.isfile(file_absolutepath) == True:
            files.append(os.path.join(directory + path))
    return files


def main():
    ''' init process nothing arguments '''
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_sjis1.txt")
    check_encoding(r"C:\Anaconda3\envs\checkEncode_py\@testfile\test_utf-8.txt")


#test
if __name__ == "__main__":
    print("start")

    #test
    #main()

    #test
    filepathlist =  enumerate_filepath(r"C:\Anaconda3\envs\checkEncode_py\@testfile")
    for x in range(len(filepathlist)):
        print(filepathlist[x])
    
    input("press any key...")
