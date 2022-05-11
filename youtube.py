import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#from oauth2client.tools import argparser
import pandas as pd
import datetime
import time

class VideoId:
    def __init__(self, APIKey):
        self.DEVELOPER_KEY=APIKey
        YOUTUBE_API_SERVICE_NAME='youtube'
        YOUTUBE_API_VERSION='v3'
        self.youtube=build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION,developerKey=self.DEVELOPER_KEY)

    def getVideoId(self):
        # 원하는 채널명 입력
        video_id_list = []

        for i in range(0,3):

            search=input("원하는 채널명을 입력해주세요 : ")

            video_list = []
            search_response = []
            titles=[]
            ids=[]


            #for a in range(0,3):
                # 채널명을 검색 / 관련 채널 상위 20개 검색
            search_response=self.youtube.search().list(       
                q=search,
                order='relevance',
                part='snippet',
                maxResults=20,
                ).execute()

            # 그 중 가장 관련있는 채널(이론상 유명한 유튜브 채널은 대부분 가능)명의 id 가져오기
            channel_id=search_response['items'][0]['id']['channelId']

            # 해당 채널의 영상들을 조회수 순으로 정렬해서 리스트 만들기
            video_list=self.youtube.search().list(
                channelId =channel_id,
                order='viewCount',
                part='snippet',
                maxResults=1,
                ).execute()


            # IDs에 videoId 저장 / Titles에 title 저장
            for i in video_list['items']:
                ids.append(i['id']['videoId'])
                titles.append(i['snippet']['title'])


            df=pd.DataFrame([titles,ids]).T
            df.columns=['Titles','IDs']

            print(ids)
            video_id_list.extend(ids)

        print(video_id_list)
        return(video_id_list)

'''

10대 - 채널 5개 -> 비디오 조회수 높은 순으로 1개씩 5개 -> 5개의 영상 댓글을 모두 모아서 -> 하나의 워드클라우드 
20대 - 채널 5개 -> 비디오 조회수 높은 순으로 1개씩 5개 -> 5개의 영상 댓글을 모두 모아서 -> 하나의 워드클라우드 

'''
