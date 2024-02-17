import praw
import requests
import os

#praw is the main reddit library data need

def scrapereddit(subredditname, numposts):
    reddit = praw.Reddit(client_id='', #provide your own!
                         client_secret='', #provide your own!
                         user_agent='okipullup')

    #user agent can be anything, client id and secret come from my developer account

    subreddit = reddit.subreddit(subredditname)
    hotposts = subreddit.hot(limit=numposts) #limit is just range of posts
    # change the .hot to anything like .top if you want a diff filter

    print(f"Getting {numposts} hot posts from r/{subreddit}\n")

    for post in hotposts:
        print(f"Title of Post: {post.title}") #spam post. and you get what you want, thanks praw!
        print(f"Author: {post.author}")
        print(f"Score: {post.score}")
        print(f"URL: {post.url}")
        print(f"Comments: {post.num_comments}")
        print(f"Content: {post.selftext}")
        print("-------------------------")

        if post.url.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            image_url = post.url
            image_name = post.title + os.path.splitext(image_url)[1]
            image_path = os.path.join("images", image_name)
            if not os.path.exists("images"):
                os.makedirs("images")
            try:
                with open(image_path, 'wb') as f:
                    f.write(requests.get(image_url).content)
                print(f"Image downloaded: {image_path}")
            except Exception as e:
                print(f"Failed to download image: {str(e)}")

        # needed stack overflow help for the image downloading lols :/


if __name__ == "__main__":
    subredditname = input("Enter the name of the subreddit you want to scrape: ")
    numposts = int(input("Enter the number of posts you want to scrape: "))

    scrapereddit(subredditname, numposts)
