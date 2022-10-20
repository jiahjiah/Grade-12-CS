import praw

def main():
    a = praw.Reddit(
        client_id="nWn7q14nrzNeu8iuDgTHjw",
        client_secret="0Qvt0h8Z0RNyYwUe3cbn9FWutA4Fww",
        password="gZfnXi26tXSZRkJ",
        user_agent="Mocking Spongebob by u/nthierie",
        username="nthierie",
    )
    

    subreddit = a.subreddit("CSHATEEE")
    for post in subreddit.stream.submissions():
        normalized_comment = post.title.lower()


        if "literally" in post.title:
            # reply = mock(normalized_comment)
            reply = normalized_comment.upper()
            post.reply(body=reply)
            print(reply)



def mock(originalString):
    noVowelString = ""
    for i in range(len(originalString)):
        if not (originalString[i] == ("o") or originalString[i] == ("e")):
            noVowelString += originalString[i]
        
    mockString = ""
    count = 1
    for i in range (len(noVowelString)):
        if not noVowelString[i] == (" "):
            if count % 5 == 0 or count % 5 == 2:
                mockString += noVowelString[i].upper()
            else:
                mockString += noVowelString[i]
            
            count += 1
        else:
            mockString += noVowelString[i]
    return mockString

    
if __name__ == "__main__":
    main()    
