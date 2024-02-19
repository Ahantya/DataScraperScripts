from googleapiclient.discovery import build
import json

apikey = 'AIzaSyDVmut8O8YkYQfxYUPlLPnuUnvuaMG9RGs'


def fetchdetails(videoid):
    youtube = build('youtube', 'v3', developerKey=apikey)

    request = youtube.videos().list(
        part="snippet,statistics",
        id=videoid
    )

    response = request.execute()

    videoinfo = {}
    
    if 'items' in response and len(response['items']) > 0:
        
        item = response['items'][0]
        videoinfo['title'] = item['snippet']['title']
        videoinfo['channeltitle'] = item['snippet']['channelTitle']
        videoinfo['views'] = item['statistics']['viewCount']
        videoinfo['likes'] = item['statistics'].get('likeCount', 0)
        # no point in getting dislikes :
        videoinfo['comments'] = item['statistics'].get('commentCount', 0)

    return videoinfo

if __name__ == "__main__":
    
    videoid = input("Enter YouTube video ID: ")
    video = fetchdetails(videoid)

    if video:
        print("\nVideo Details:")
        print("Title:", video['title'])
        print("Channel Title:", video['channeltitle'])
        print("Views:", video['views'])
        print("Likes:", video['likes'])
        print("Comments:", video['comments'])
        
    else:
        print("Video not found or invalid video ID.")
