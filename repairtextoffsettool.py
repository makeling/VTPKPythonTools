#-*- coding: UTF-8 -*-
#!/usr/bin/python
#
#  Created by makeling on 7/24/17.
#  Copyright © 2017 esrichina.com. All rights reserved.
#


import os
import sys
import json
import imp

def analysisLayers(stylePath=None):
    print("stype path:" + stylePath)
    jsonfile = open(stylePath)
    jd = json.loads(jsonfile.read())

    layers = jd['layers']
    print ("layers count: " +str(len(layers)))

    print ("layer list :")

    for layer in layers:
        print (layer['id'])

    jsonfile.close()


def changeStyle(stylePath=None, changeField=None):
    jsonfile = open(stylePath)
    jd = json.loads(jsonfile.read())
    layers = jd['layers']
    for layer in layers:
        if layer['id'].count(changeField):
            layerid = layer['id']
            print ("changed layer :" + layerid)
            layout = layer['layout']
            layout["text-offset"] = [0, 1]

    newjd = json.dumps(jd, ensure_ascii=False)
    newjsonfile = open(stylePath, 'w')
    newjsonfile.write(newjd)
    print ("style file have been changed.")
    jsonfile.close()
    newjsonfile.close()


if __name__ == "__main__":
    # imp.reload(sys)
    #sys.setdefaultencoding('utf-8')
    stylePath = '/Users/maklmac/Desktop/root.json'
    analysisLayers(stylePath)
    print("-----------------------------------")
    changeField = str(input("input field id for changed:"))

    changeStyle(stylePath, changeField)
