# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 01:34:45 2014

@author: amyskerry
"""

import base64
import csv
import datetime
import sys

#jpgtxt = base64.encodestring(open("in.jpg","rb").read())

jpgtxt="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"

date=datetime.datetime.now()
datestr=date.strftime("%Y-%m-%d")
photofile='/Users/amyskerry/documents/projects/dlsbridal/dlsbridal_save/dlsphotos.csv'
savedir='/Users/amyskerry/documents/projects/dlsbridal/dlsbridal_save/photos/'
allphotos=[]
csv.field_size_limit(sys.maxsize)
with open(photofile, 'rU') as csvfile:
    reader = csv.reader(csvfile)
    for rown, row in enumerate(reader):
        if rown==0:
            photoindex=row.index('photo')
        else:
            photoentry=row[photoindex]
            #cutstring="MiniFieldStorage('photofield', '"
            cutstring=''
            photo=photoentry[len(cutstring):]
            allphotos.append(photo)
    
for photon, photo in enumerate(allphotos):
    g = open(savedir+'photo'+str(photon)+'_'+datestr+'.jpg', 'w')
    g.write(base64.decodestring(photo))
    g.close()