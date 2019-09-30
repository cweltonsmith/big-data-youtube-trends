#!/usr/bin/python

# Format of each line is:
# video_id/trending_date/title/channel_title/category_id/publish_time/tags/
# views/likes/dislikes/comment_count/thumbnail_link/comments_disabled/
# ratings_disabled/video_error/description
#
# I want elements 3 (channel_title) and 7 (views)
# We need to write them out to standard output, separated by a comma

import sys

def is_num(num):
	try:
		float(num)
		return True
	except ValueError:
		return False 

for line in sys.stdin:
	data = line.strip().split(",")
	if len(data) == 16:
		v_id, td, v_ti, c_ti, c_id, p_t, tgs, vs, ls, ds, c_c, t_l, cd, rd, v_e, des = data
		if is_num(vs):
			print "{0}\t{1}".format(c_ti, vs)

