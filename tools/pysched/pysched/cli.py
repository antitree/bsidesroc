#!/usr/bin/python
# author: antittree
# description: merge a TSV and a schedule file to build the 
# defacto schedule. 

import pysched

import argparse
import logging
import csv
import json

# tmp
import sys

TEMPLATEPATH = './example.json'

def import_skel():
    basetemplate = open(TEMPLATEPATH, 'r').readlines()
    return basetemplate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", 
        help="tab separated file to import",
        action="store",
        type=argparse.FileType('r'))
    parser.add_argument("-p", dest="path", default="../content/about/ops/" )
    parser.add_argument("-D", dest="debug", action='store_true')
    args = parser.parse_args()
    ## TODO validate path
    outputpath = args.path

    print(args)
    if args.debug: 
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug logging enabled")

    colnum = 7
    if len(args.file.readline().split('\t')) == colnum:
        logging.debug("Found %s categories" % colnum)
    else:
        logging.INFO("Invalid number of column headers found")
    
    talks = []
    for record in csv.reader(args.file, delimiter='\t'): 
        talk = talk.Talk()
        talk.title = record[2]
        talk.presenters = record[1]
        talk.bio = record[5]
        talk.description = record[3]
        try:

            ops.append(
                dict(
                    name=talk[1],
                    positions=op[1],
                    bio=op[5],
                    twitter=op[6]
                    )
                )
        except: 
            print(op)
    logging.debug(ops)



if __name__ == "__main__":
    main()
