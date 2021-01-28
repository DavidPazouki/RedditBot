import praw

reddit = praw.Reddit(client_id= 'I3N24ZmSTug7cA', 
                     client_secret= 'K_hoUv8lQYNw4LxgZmnlMlPZxulHNg' ,
                     username= 'Taysteeee',
                     password= 'DXE87jDeuQ99CF3',
                     user_agent= 'prawtest')

subreddit = reddit.subreddit('wallstreetbets')

hot_wsb = subreddit.hot(limit=5)

for submission in hot_wsb:
    if not submission.stickied:
        print('Title: {}, ups: {}'.format(submission.title, submission.ups))
        print('\n')