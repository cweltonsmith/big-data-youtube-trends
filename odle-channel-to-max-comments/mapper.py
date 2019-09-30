#!/usr/bin/python

# Format of each line is:
# video_id\title\channel_title\category_id\tags\views\likes\dislikes\comment_total\thumbnail_link\date
#
# We want elements 2 (channel_title) and 8 (comment_total)
# We need to write them out to standard output, separated by a tab

import sys

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 11:
        video_id, title, channel_title, category_id, tags, views, likes, dislikes, comment_total, thumbnail_link, date = data
        print "{0}\t{1}".format(channel_title, comment_total)

