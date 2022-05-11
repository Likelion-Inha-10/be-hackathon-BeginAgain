# be-hackathon-BeginAgain
기획의도 : 
1.	특정 계정이 구독한 채널의 인기동영상 댓글을 워드클라우드로 추출하고 이를 바탕으로 해당 계정 주인의 유튜브 시청 목적(힐링, 게임, 여행, 먹방)을 유추하고자 함. 그러나 특정 계정의 구독 정보를 알아내기 어려웠다.
2.	주제가 같지만 구독자의 평균 연령대가 다른 여러 채널의 댓글을 비교하여 연령대 별 사용 어휘를 워드클라우드 형태로 시각화하여 분석하고자 하였다.

분업과정 :
1.	특정 계정의 채널 구독 정보를 가져온다.
2.	구독 채널의 인기동영상 5편, URL을 가져온다.
3.	다중의 URL에서 댓글을 크롤링하여 csv파일로 내보낸다.
4.	csv파일을 형태소 분석 및 불용어 제거 후 워드클라우드로 추출한다.

시행착오 : 
-	여진 : 특정 계정의 채널 구독 정보 가져오기
	구독 정보가 대부분 비공개로 설정되어 있어 불가능했다.
	개인 계정으로 로그인 후 구독 정보를 가져오려 했으나 Youtube 보안 정책 등 어려움이 있었다.
-	민경 : 구독 채널의 재생목록 중 조회수 상위 5편, URL 가져오기
	채널의 videoID를 반복문으로 가져오는 과정에서 오류가 많이 발생하였다.
-	석민 : 다중의 URL에서 댓글을 크롤링하여 csv파일로 내보내기
	URL을 videoID라는 고유번호로 자동전환하였다.
	팀원 분들의 도움으로 YoutubeAPI 정책을 열람하고 필요없는 대댓글 정보는 삭제하는 등 최적화 과정을 거쳤다.
-	재필 : csv파일을 형태소 분석 및 불용어 제거 후 워드클라우드로 추출하기
	의미있는 데이터 분석을 위해 불용어 제거 작업을 거쳤으나 불용어 선정 기준을 결정하는데 어려움이 있었다.

결과물 : 

실행 이후, 
API 키를 입력해주세요 : AIzaSyCaUMmzzx4n3A2HAh9_c3p9yNxYpgJNFik
원하는 채널명을 입력해주세요 : 찐언니
['HVy4mX4v3JA']
원하는 채널명을 입력해주세요 : 김로라
['TC4phaMVNr8']
원하는 채널명을 입력해주세요 : 김파란
['Fonu-sD1oLU']
['HVy4mX4v3JA', 'TC4phaMVNr8', 'Fonu-sD1oLU']

17세 미만 : 
![17세 미만](https://user-images.githubusercontent.com/86829166/167811737-b3eebda3-689e-4e18-963d-f9b30b649835.png)

65세 이상 : 
![65세 이상](https://user-images.githubusercontent.com/86829166/167812584-bff4011f-589a-4913-86d2-69d4a1bcbd12.png)
