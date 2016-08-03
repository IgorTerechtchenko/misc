#! /usr/bin/python
import os
import re
import argparse
import sys
import time
from multiprocessing import Pool


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print str(te - ts)
        return result

    return timed


class Image:
    def __init__(self, name, hash):
        self.name = name
        self.hash = hash

    def __str__(self):
        return self.name

    def __cmp__(self, other):
        if self.hash == other.hash:
            return 0
        if self.hash > other.hash:
            return 1
        if self.hash < other.hash:
            return -1

    def __hash__(self):
        return hash(self.hash)


def create_img(image_name):
    """returns Image object with name and hash"""
    im_identify = "identify -verbose \"{}\" | grep signature"
    return Image(image_name, re.sub("signature: ", "",
                 os.popen(im_identify.format(image_name)).read())
                 .rstrip())


@timeit
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="""get rid of visually of identical images,
                        leaving one with alphabeticaly greatest name""",
                        action="store_true")
    parser.add_argument("-l", help="list visualy identical images",
                        action="store_true")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    pic_names = os.listdir(".")
    images = []
    pool = Pool(5)
    images = pool.map(create_img, pic_names)
    pool.close()
    pool.join()

    images = filter(lambda x: x.hash != "", images)
    result = []

    for image in images:
        result.append(tuple(filter(lambda i: image == i, images)))

    result = filter(lambda x: len(x) > 1, result)

    result = list(set(result))

    if args.l:
        for i in result:
            for item in i:
                print item
            print "++++++++++++++++"

    if args.d:
        for group in result:
            for name in group[1:]:
                os.popen("rm {}".format(name))

if __name__ == "__main__":
    main()
