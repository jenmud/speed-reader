def ReadInFile(file):
    """
    Read the file and return the content of the file as a list.
    """
    with open(file, "r") as f:
        return f.readlines()


def PrintWords(fh, speed=0.5):
    """
    Print the percentage of the progress
    """
    for line in fh:
        last = 0
        for word in line.split():
            print(f"\r{word : <{last}}", end="", flush=True)
            last = len(word)
            time.sleep(speed)


if __name__ == '__main__':
    import time
    import argparse

    parser = argparse.ArgumentParser(description="Speed test")
    parser.add_argument("file", type=argparse.FileType(), help="file to read")
    parser.add_argument("-s", "--speed", type=float, default=0.5, help="speed of the progress")
    ns = parser.parse_args()

    PrintWords(ns.file, ns.speed)
