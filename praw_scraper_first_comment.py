import praw

reddit = praw.Reddit(client_id='HNFCY4PY4ggISQ',
					client_secret='mFl0JQHToOLh5OfQCdSMIpvtbqE',
					user_agent='robot')
subreddit = reddit.subreddit("learnpython")

for item in subreddit.hot(limit=2):
	comment_list = []
	top_level_commments = item.comments
	for comments in top_level_commments[0:1]:
		comment_list.append(comments.body)
	print("Title: ", item.title)
	print("Text: ", item.selftext)
	print("First Comment: ", comment_list[0])