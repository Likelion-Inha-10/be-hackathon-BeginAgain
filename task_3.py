import pandas
from googleapiclient.discovery import build
import warnings 
warnings.filterwarnings('ignore')


urls = ['https://www.youtube.com/watch?v=HbbyfQbJen4', 'https://www.youtube.com/watch?v=MclZ349RVf8', 'https://www.youtube.com/watch?v=Kbn-dNTpSM4', 'https://www.youtube.com/watch?v=sy_12FM0Xp8', 'https://www.youtube.com/watch?v=389itBs7YlE']
videoIDs = []
for i in urls:
    videoIDs.append (i[32:])
print (videoIDs)
comments = list()
api_obj = build('youtube', 'v3', developerKey='AIzaSyCgmJab8xSvJyaEXhIxDR-vtNU-w1sUEr4')
for i in videoIDs:
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

