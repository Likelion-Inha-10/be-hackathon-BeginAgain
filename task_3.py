import pandas
from googleapiclient.discovery import build
import warnings 
warnings.filterwarnings('ignore')


class CommentsCollection:
    def __init__(self, APIKey, VideoIds):
        self.comments = list()
        self.api_obj = build('youtube', 'v3', developerKey=APIKey)
        self.video_id_list = VideoIds
    
    def getComments():
        for i in self.video_id_list:
            response = self.api_obj.commentThreads().list(part='snippet,replies', videoId=i, maxResults=100).execute()

            while response:
                for item in response['items']:
                    comment = item['snippet']['topLevelComment']['snippet']
                    self.comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
            
                if 'nextPageToken' in response:
                    response = self.api_obj.commentThreads().list(part='snippet,replies', videoId=i, pageToken=response['nextPageToken'], maxResults=100).execute()
                else:
                    break

        df = pandas.DataFrame(self.comments)
        df.to_csv('task3.csv', header=['comment', 'author', 'date', 'num_likes'], index=None)
        return df