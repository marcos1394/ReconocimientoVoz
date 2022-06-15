import youtube_dl

ydl = youtube_dl.YoutubeDL()


def get_video_infos(url):
    with ydl:
        result = ydl.extract_info(
            url, download=False
        )
    if "entries" in result:
        return result("entries")[0]
    return result


def get_audio_url(video_info):
    for f in video_info["formats"]:
        if f["ext"] == "m4a":
            return f["url"]


if __name__ == "__main__":
    video_info = get_video_infos("https://www.youtube.com/watch?v=iKW1RFr4vKk")
    audio_url = get_audio_url(video_info)
    print(audio_url)
