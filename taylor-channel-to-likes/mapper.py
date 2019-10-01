# video_id/trending_date/title/channel_title/category_id/publish_time/tags/
# views/likes/dislikes/comment_count/thumbnail_link/comments_disabled/
# ratings_disabled/video_error/description

import sys

def check_num(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

for line in sys.stdin:
    data = line.strip().split(",")
    if len(data) == 16:
        idnum, date, title, chantitle, catgor, publish, tags, views, likes, dislikes, comments, thub, commdis, ratdis, err, desc = data
        if check_num(likes):
            print"{0}\t{1}".format(chantitle, likes)