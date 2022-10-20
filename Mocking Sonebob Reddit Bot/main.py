import praw
import time
import os

def botLogin():
    reddit = praw.Reddit(
        user_agent="Mocking Spongebob by u/Mocking--Spongebob",
        client_id="wSDWKm78pdUs3nlcKMxpDQ",
        client_secret="Ztn3PrCBoGMlloV4FXLHKc-jFrE7Ww",
        username="Mocking--Spongebob",
        password="pl353d0ntb4n"
    )
    
    return reddit

def spongbobMockCovert(toBeConverted):
    converted = ""

    while toBeConverted.find("e") >= 0:
        toBeConverted = toBeConverted.replace("e", "")

    while toBeConverted.find("o") >= 0:
        toBeConverted = toBeConverted.replace("o", "")

    letterCounter = 0
    for i in range(0, len(toBeConverted)):
        currentChar = toBeConverted[i]
        if (currentChar != " "):
            if (letterCounter % 5 == 0):
                converted += currentChar
                letterCounter += 1
            elif (letterCounter % 5 == 1):
                converted += currentChar.upper()
                letterCounter += 1
            elif (letterCounter % 5 == 2 or letterCounter % 5 == 3):
                converted += currentChar
                letterCounter += 1
            elif (letterCounter % 5 == 4):
                converted += currentChar.upper()
                letterCounter += 1
        else:
            converted += currentChar

    return converted

def getSavedComments():
    # if file does not exist, create repliedTo lsit
    if not os.path.isfile("../commentsRepliedTo.txt"):
        repliedTo = []
    else:
        with open("../commentsRepliedTo.txt", "r") as f:
            repliedTo = f.read()
            repliedTo = repliedTo.split("\n")
            repliedTo = list(filter(None, repliedTo)) #filter out white space at end of input file

    return repliedTo

def processSubmission(submission):
    normalized_title = submission.title.lower()
    reply = spongbobMockCovert(normalized_title)
    print(f"Replying to: {submission.title}")
    submission.reply(body=reply)

def main():
    subreddit = a.subreddit("CSHATEEE")
    for post in subreddit.stream.submissions():
        processSubmission(post)
        repliedTo.append(post.id)
        with open("../commentsRepliedTo.txt", "a") as f:
            f.write(post.id + "\n")

    for comment in subreddit.comments(limit = 500):
        if comment.id not in repliedTo and comment.author != a.user.me():
            global i
            i += 1
            processSubmission(comment)
        repliedTo.append(comment.id)
        with open("../commentsRepliedTo.txt", "a") as f:
            f.write(comment.id + "\n")
        print("Sleeping for 5 seconds")
        time.sleep(5)

a = botLogin()
repliedTo = getSavedComments()

while True:
    main()
    print()
