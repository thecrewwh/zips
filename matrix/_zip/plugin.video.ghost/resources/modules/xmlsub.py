#!/usr/bin/python
# -*- encoding:utf-8 -*-

"""Translate Google's Transcript into srt file.
Takes google's transcript filename as argument (xml extension required).
NB: to get google's transcript, use tihs URL:
http://video.google.com/timedtext?lang=en&v=VIDEO_ID
"""

# srt example
"""1
00:00:20,672 --> 00:00:24,972
Entre l’Australia et la South America,
dans l’Océan South Pacific…"""

# Google's transcript example (first tags)
"""<?xml version="1.0" encoding="utf-8" ?>
<transcript>
<text start="11.927" dur="2.483">
This is a matter of National Security.</text>"""

import re, sys,requests,time,logging
from resources.modules import log
# Pattern to identify a subtitle and grab start, duration and text.
pat = re.compile(r'text start="(.+?)" dur="(.+?)">(.+?)</text', re.DOTALL)

def parseLine(text):
    """Parse a subtitle."""
    m = re.match(pat, text)
    
    if m:
        return (m.group(1), m.group(2), m.group(3))
    else:
        print pat
        print text
        return None

def formatSrtTime(secTime):
    """Convert a time in seconds (google's transcript) to srt time format."""
    if '.' in str(secTime):
        sec, micro = str(secTime).split('.')
    else:
        sec=str(secTime)
        micro=0
    m, s = divmod(int(sec), 60)
    h, m = divmod(m, 60)
    log.warning(h)
    log.warning(m)
    log.warning(s)
    log.warning(micro)
    return "{0}:{1}:{2},{3}".format(str(h).zfill(2),str(m).zfill(2),str(s).zfill(2),str(micro).zfill(3))

def convertHtml(text):
	"""A few HTML encodings replacements.
	&amp;#39; to '
	&amp;quot; to "
	"""
	return text.replace('&amp;#39;', "'").replace('&amp;quot;', '"')

def printSrtLine(i, elms):
	"""Print a subtitle in srt format."""
	return "{}\n{} --> {}\n{}\n\n".format(i, formatSrtTime(elms[0]), formatSrtTime(float(elms[0])+float(elms[1])), convertHtml(elms[2])).replace('&amp;','&').replace('lt;','<').replace('&gt;','>').replace('&<','<')



def xml2srt(buf,des):
    """Parse google's transcript and write the converted data in srt format."""
    #buf=requests.get('https://drive.google.com/timedtext?authuser=0&id=1Wc7KJLkNUd7sWE66-rGvpwA1J3qPfZ7N&vid=92afb9c0d000b9db&ts=1565136790041827&type=track&lang=iw&format=1&kind=').content
    
    # Split the buffer to get one string per tag.
    buf = buf.split('><')
    
    i = 0
    
    with open(des, 'w') as outfile:
        for text in buf:
            parsed = parseLine(text)
            if parsed:
                i += 1
                outfile.write(printSrtLine(i, parsed))
    
print time.time()
if __name__ == "__main__":
	main()