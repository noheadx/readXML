#!/usr/bin/env python

import xml.dom.minidom
import os


DEFAULT_PATH = './'
DEFAULT_DELIMITER = ';'

def _extract_xml(elements, delimiter, file):
    # load and parse each XML file
    doc = xml.dom.minidom.parse(file);

    # get a the required of XML elements from the document
    # belnrs = doc.getElementsByTagName("BELNR")
    # bookingids = doc.getElementsByTagName("IDTNR")
    # prices = doc.getElementsByTagName("SUMME")
    nodes = []
    # extract elements into separate nodelists
    for element in elements:
        nodes.append(doc.getElementsByTagName(element))

    nodeiterator = 0
    row = file
    head = ''

    # go through each nodelist
    for node in nodes:
        itemiterator = 0
        #check the items in the current node
        while itemiterator <= len(node):
            if node.item(itemiterator):
                row = row + delimiter + node.item(itemiterator).firstChild.data
            itemiterator+=1

    #create each row
    # row = file +";" + belnrs.item(0).firstChild.data + ";"+bookingids.item(0).firstChild.data.split("_")[0]

    # for price in prices:
    #     row= row + ";"+price.firstChild.data
    print(row)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--elementlist', help='Comma separated list of elements to be extracted.', action='store')
    parser.add_argument('--xmlfolder', help='Path to folder where to find the xml files')
    parser.add_argument('--xmlfile', help='XML file to be processed')
    parser.add_argument('--target', help='Path where to store the created csv file')
    parser.add_argument('--delimiter', help='Defines the delimiter to use in the csv file')
    args = parser.parse_args()

    elements = args.elementlist.split(',')
    xmlfolder = args.xmlfolder
    xmlfile = args.xmlfile
    targetpath = args.target if args.target else DEFAULT_PATH
    delimiter = args.delimiter if args.delimiter else DEFAULT_DELIMITER
    head = "FILENAME;BELNR;BOOKINGID;PRICE1;PRICE2;PRICE3;PRICE4"
    print(head)
    if (xmlfolder):
        for subdir, dirs, files in os.walk(xmlfolder):
            for file in files:
                if file.endswith(".xml"):
                    _extract_xml(elements, delimiter, xmlfolder+'/'+file)
    elif (xmlfile):
        _extract_xml(elements, delimiter, xmlfile)
    else:
        print('No argument for source file/folder given!')
