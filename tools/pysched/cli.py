#!/usr/bin/python
# author: antittree
# description: merge a TSV and a schedule file to build the 
# defacto schedule. 

import pysched

import argparse
import logging
import csv
import json
import pprint

# tmp
import sys

TEMPLATEPATH = './2018.json'

def import_skel():
    try: 
        basetemplate = json.load(open(TEMPLATEPATH, 'r'))
    except:
        print("Can't find the 2018 json data. Edit this with the correct path")
        sys.exit()
    
    return basetemplate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", 
        help="tab separated file to import",
        action="store",
        type=argparse.FileType('r'))
    parser.add_argument("-D", dest="debug", action='store_true', default="/tmp/bsidesroc")
    parser.add_argument("-m", dest="markdown", action='store')
    args = parser.parse_args()
    ## TODO validate path
    

    if args.debug: 
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug logging enabled")
    
    schedule = []
    for record in csv.reader(args.file, delimiter='\t'): 
        if record[13] == "APPROVED":
            logging.debug(record)
            talk = pysched.talks.Talk()
            talk.title = record[4]
            talk.speakers = record[2]
            talk.bio = record[6]
            talk.length = record[11][:2]
            talk.description = record[5]
            talk.time_start = record[15]
            talk.room = record[14]
            schedule.append(talk.json())
            talk.markdown(args.markdown)


    template = import_skel()
    for record in template:
        talk = pysched.talks.Talk()
        talk.title = record["title"] 
        talk.speakers = record["speakers"]
        talk.desription = record["description"]
        talk.room = record["room"]
        talk.time_start = record["time_start"]
        schedule.append(talk.json())

    #print(json.dumps(schedule))

    #sorted_schedule = sorted(schedule, key=lambda k: k["room"])
    #from operator import itemgetter
    #sorted_schedule = sorted(schedule, key=itemgetter("room"))

    #print(sorted_schedule)
    #for s in sorted_schedule:
    #    print("%s \t %s" % (s["time_start"], s["title"]))

    '''import textable as tt
    tab = tt.Texttable()
    headings = ["Track1", "Track2", "Track3"]
    tab.header(headings)
    times = range(800,1700,100)
    
    tracks = {}
    for track in ("Track 1", "Track 2", "Track 3"):
        tracks[track] = [x for x in sorted_schedule if x["room"].lower() == track.lower()]
        #print(tracks[track][0])
    
    ## fuck this shit <<<<<<
    print(tracks)
    rows = []
    for i in times:
        row = {}
        for track in tracks:
            for talk in track:
                print(talk)
                if talk["time_start"] == i:
                    row[i].update(talk)
                    print(row)
            

        #rows.append(row)

    print(rows)
        #print(repr('{0:2s} {1:3s} {2:4s}'.format()))
    '''





if __name__ == "__main__":
    main()
