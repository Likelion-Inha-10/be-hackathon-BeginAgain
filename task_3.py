import pandas
from googleapiclient.discovery import build
import warnings 
warnings.filterwarnings('ignore')



comments = list()
api_obj = build('youtube', 'v3', developerKey='AIzaSyCgmJab8xSvJyaEXhIxDR-vtNU-w1sUEr4')
for i in video_id_list:
    response = api_obj.commentThreads().list(part='snippet,replies', videoId=i, maxResults=100).execute()

    while response:
        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']
            comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
    
        if 'nextPageToken' in response:
            response = api_obj.commentThreads().list(part='snippet,replies', videoId=i, pageToken=response['nextPageToken'], maxResults=100).execute()
        else:
            break

df = pandas.DataFrame(comments)
df.to_csv('task3.csv', header=['comment', 'author', 'date', 'num_likes'], index=None)

