import youtube3
import task_3
import total

APIKey = input("API 키를 입력해주세요 : ")
videoId=youtube3.VideoId(APIKey)
videoIdList=videoId.getVideoId()

comments = task_3.CommentsCollection(APIKey, videoIdList)
comments.getComments()

wordcloud=total.MakeWordCloud()
wordcloud.getWordCloud()