import requests

userSentence = "What do you mean by that?"

req = requests.get("https://yoda.p.mashape.com/yoda?sentence=%s" % userSentence, headers={"X-Mashape-Key" : "koOcHBlpromshEfseSd3AZZYbIS7p1v92UojsnlMyVE5DgvNcj"})

req.text
