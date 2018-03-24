import json

class Talk(object):
    VALIDTYPES = ["appsec", "netsec", "meta", "hacking", "dfir"]

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
        self.slides = None

    def __repr__(self):
        return ", ".join([str(x) for x in vars(self).items()])

    def __str__(self):
        return "%s - %s: %s" % (self.title, self.speakers, self.description)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str): raise Exception("Title must be a string")
        self._title = value

    @property
    def type(self, value):
        return self._type

    @type.setter
    def type(self, value):
        if not value in VALIDTYPES: raise Exception("Type not one of the valid types")
        self._type = value

    @property
    def type(self, value):
        return self._description

    @type.setter
    def type(self, value):
        if not isinstance(value, str): raise Exception("Description must be a string")
        ## TODO add HTML validation
        self._description = value

    def dump(self):
        json.dumps([{
            "title":        self.title,
            "type":         self.type,
            "description":  self.description
            }]