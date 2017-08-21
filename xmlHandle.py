#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.sax


class CountryHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.CurrentAttributes = ""
        self.rank = ""
        self.year = ""
        self.gdppc = ""
        self.nei_name = ""
        self.nei_dire = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        self.CurrentAttributes = attributes
        if tag == "country":
            print("*****Country*****")
            name = attributes["name"]
            print("Name:", name)
        if tag == "neighbor":
            self.nei_name = attributes["name"]
            self.nei_dire = attributes["direction"]

    def endElement(self, tag):
        if self.CurrentData == "rank":
            print("Rank:", self.rank)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "gdppc":
            print("Gdppc:", self.gdppc)
        elif self.CurrentData == "neighbor":
            print("Neighbor:", self.nei_name, self.nei_dire)
        self.CurrentData = ""
        self.nei_name = ""
        self.nei_dire = ""

    def characters(self, content):
        if self.CurrentData == "rank":
            self.rank = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "gdppc":
            self.gdppc = content


if __name__ == "__main__":
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    Handler = CountryHandler()
    parser.setContentHandler(Handler)
    parser.parse("countries.xml")