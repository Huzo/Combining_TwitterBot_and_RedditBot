import praw

reddit = praw.Reddit(client_id='',client_secret='',
					username='',password='',user_agent='r')


subreddit = reddit.subreddit('worldnews')

for submission in subreddit.stream.submissions():
	if not submission.stickied:
		print(str(submission.title) + " " + str(submission.url) + " #news #worldnews\n")
		
