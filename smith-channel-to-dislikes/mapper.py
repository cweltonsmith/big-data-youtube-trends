# Format of each line is:
# video_id/trending_date/title/channel_title/category_id/publish_time/tags/
# views/likes/dislikes/comment_count/thumbnail_link/comments_disabled/
# ratings_disabled/video_error/description

import sys

# This function checks to make sure that what is inputed is a number 
def check_num(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

#for loop itterate though each line
for line in sys.stdin:
    data = line.strip().split(",") #strips the ,
    if len(data) == 16: #make sure that theres 16 columns
        idnum, date, title, chantitle, catgor, publish, tags, views, likes, dislikes, comments, thub, commdis, ratdis, err, desc = data
        if check_num(dislikes): #if dislikes is a number
            print"{0}\t{1}".format(chantitle, dislikes)#reprints it
