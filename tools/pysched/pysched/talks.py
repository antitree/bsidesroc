import json
import html
import os
import re

class Talk(object):
    VALIDTYPES = ["appsec", "netsec", "meta", "hacking", "dfir", "keynote", ""]

    def __init__(self):
        self.title = ""
        self.type = ""
        self.description = ""
        self.speakers = ""
        self.date = ""
        self.time_start = ""
        self.time_end = ""
        self.length = ""
        self.room = ""
        self.bio = ""
        self.slides = ""
        self.video = ""
        self.stub = "none"

    def __repr__(self):
        return ", ".join([str(x) for x in vars(self).items()])

    def __str__(self):
        return "%s - %s: %s" % (self.title, self.speakers, self.description)

    @property
    def stub(self):
        return self._stub

    @stub.setter
    def stub(self, value):
        value = html.escape(value)
        if not value.isprintable(): raise Exception("Stub can only be alpha chars: %s" % value)
        self._stub = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        value = html.escape(value)
        if not isinstance(value, str): raise Exception("Title must be a string")
        self._title = value
        titlewords = re.sub(r'\W+', "", value).lower()
        titlewords = value.split()
        self.stub = "_".join(titlewords[:4])


    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        value = html.escape(value)
        if not value.lower() in self.VALIDTYPES: raise Exception("Type %s not one of the valid types: %s " % (value, self.VALIDTYPES))
        self._type = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not isinstance(value, str): raise Exception("Description must be a string")
        value = html.escape(value)
        self._description = value

    @property
    def speakers(self):
        return self._speakers

    @speakers.setter
    def speakers(self, value):
        value = html.escape(value)
        if not isinstance(value, str): raise Exception("Speakers must be a string")
        self._speakers = value

    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, value):
        value = html.escape(value)
        if not isinstance(value, str): raise Exception("Bio must be a string")
        self._bio = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str): raise Exception("Date must be a string")
        self._date = value

    @property
    def time_start(self):
        return self._time_start

    @time_start.setter
    def time_start(self, value):
        if not isinstance(value, str): raise Exception("Time must be a string")
        self._time_start = value                

    @property
    def time_end(self):
        return self._time_end

    @time_end.setter
    def time_end(self, value):
        if not isinstance(value, str): raise Exception("Time end must be a string")
        self._time_end = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if not isinstance(value, str): raise Exception("Length must be a string")
        self._length = value

    @property
    def room(self):
        return self._room

    @room.setter
    def room(self, value):
        if not isinstance(value, str): raise Exception("Room must be a string")
        self._room = value

    def json(self):
        jsonout = json.dumps({
            "title":        self.title,
            "type":         self.type,
            "description":  self.description,
            "speakers":     self.speakers,
            "date":         self.date,
            "time_start":   self.time_start,
            "time_end":     self.time_end,
            "length":       self.length,
            "room":         self.room,
            "bio":          self.bio,
            "slides":       self.slides,
            "video":        self.video
            })
        try:
            jsonout = eval(jsonout)
        except:
            jsonout = jsonout
        return jsonout

    def markdown(self, path):
        ''' Output the talk into markdown format for Hugo'''
        assert os.path.isdir(path)
        path = os.path.join(path, '')
        md = """+++
title= "{title}"
speakers= "{speakers}"
type= "{type}"
thedate= "{date}"
length= "{length}"
room= "{room}"
bio= "{bio}"
time_start= "{time_start}"
slides= "{slides}"
video= "{video}"
description= "{description}"
stub= "{stub}"
+++""".format(
            title=self.title,
            speakers=self.speakers,
            type=self.type,
            date=self.date,
            length=self.length,
            room=self.room,
            bio=self.bio,
            slides=self.slides,
            video=self.video,
            description=self.description,
            time_start=self.time_start,
            stub=self.stub
            )
        f = open(path + self.stub + ".md", 'w')
        f.writelines(md)
        f.close()
