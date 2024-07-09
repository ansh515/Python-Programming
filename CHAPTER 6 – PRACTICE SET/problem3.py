# CHATGPT

spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]

message = input("Enter your comment: ")

is_spam = any(keyword in message for keyword in spam_keywords)

if is_spam:
    print("Spam")
else:
    print("Not Spam")
