from django.shortcuts import render
from django.conf import settings
# Create your views here.
import googleapiclient.discovery
apikey = settings.YT_API_KEY
Vidid = settings.VIDEO_ID
def ListTopLevelComments():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = apikey

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=Vidid
    )
    response = request.execute()
    return response


apikey = settings.YT_API_KEY
def home(request):
	commentdata=ListTopLevelComments()

	comments = []
	for item in commentdata.get("items", []):
	    comment_data = item["snippet"]["topLevelComment"]["snippet"]
	    comments.append(
	        {
	            "textOriginal": comment_data["textOriginal"],
	            "authorDisplayName": comment_data["authorDisplayName"],
	            "likeCount": comment_data["likeCount"],
	            "authorProfileImageUrl": comment_data["authorProfileImageUrl"],
	        }
	    )    

	# print(comments)
	return render(request,'home.html', {"comments": comments})