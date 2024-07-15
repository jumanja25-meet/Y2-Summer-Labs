def create_youtube_video(title, description):
    new_youtube_video = {
        "title": title,
        "description": description,
        "likes": 0,
        "dislikes": 0,
        "comments": {}
    }
    return new_youtube_video

def like(youtube_video):
    if "likes" in youtube_video:
        youtube_video["likes"] += 1
    return youtube_video

def dislike(youtube_video):
    if "dislikes" in youtube_video:
        youtube_video["dislikes"] += 1
    return youtube_video

def add_comment(youtube_video, username, comment_text):
    if "comments" in youtube_video:
        youtube_video["comments"][username] = comment_text
    return youtube_video

youtube_video = create_youtube_video("this is amazinggg", "Wow you have to try this ;)")

youtube_video = add_comment(youtube_video, "hahaa", "slay")

for _ in range(495):
    youtube_video = like(youtube_video)

print(youtube_video)
