from youtubesearchpython import VideosSearch
import os
def search_video_by_channel(channel_name, video_title):
    try:
        # Search for videos by the specified channel
        video_search = VideosSearch(f'{channel_name} {video_title}', limit = 1)

        # Get the first result
        result = video_search.result()

        if result['result']:
            video_url = result['result'][0]['link']
            video_title = result['result'][0]['title']

            print(f"Video Title: {video_title}")
            print(f"Video URL: {video_url}")

            return video_url
        else:
            print("Video not found.")
            return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def search_video(CHANNEL_NAME, VIDEO_TITLE):

    video_url = search_video_by_channel(CHANNEL_NAME, VIDEO_TITLE)

    if video_url:
        # You can now use the video URL as needed (e.g., open it in a web browser)
        print(f"Opening video URL: {video_url}")
        os.system(f"mpv {video_url}")
    else:
        print("Video not found.")


# search_video("PewDiePie", "Minecraft")