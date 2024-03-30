import random
import collections
import math

# web_dict={w1:18,}

w1 = {
    'age': 18,
    'keywords': ["Search engine","Online advertising","Gmail","Google Maps","Android","Google Drive","YouTube","Google Chrome" ,"Artificial intelligence" ,"Cloud computing"]
}

w2 = {
    'age': 26,
    'keywords': ["Video sharing","Content creators","Subscriptions","Music videos","Vlogs","Live streaming","User-generated content","Monetization","YouTube Premium","Trending videos"]
}

w3 = {
    'age': 55,
    'keywords': ["Social networking","News feed","Friends and family","Groups","Timeline","Messenger","Events","Marketplace","Privacy settings","Advertising"]
}

w4 = {
    'age': 38,
    'keywords': ["Microblogging","Tweets","Hashtags","Followers","Retweets","Trending topics","Verification","Direct messages","Twitterati","Breaking news"]
}

w5 = {
    'age': 13,
    'keywords': ["Photo sharing","Filters","Stories","Influencers","Followers","Hashtags","Explore page","IGTV","Direct messages","Visual content"]
}

websites = [w1, w2, w3, w4, w5]

visitor_keywords = ["Search engine","Online advertising","Gmail","Google Maps","Android","Google Drive","YouTube","Google Chrome" ,"Artificial intelligence" ,"Cloud computing","Video sharing","Content creators","Subscriptions","Music videos","Vlogs","Live streaming","User-generated content","Monetization","YouTube Premium","Trending videos", "Social networking","News feed","Friends and family","Groups","Timeline","Messenger","Events","Marketplace","Privacy settings","Advertising", "Microblogging","Tweets","Hashtags","Followers","Retweets","Trending topics","Verification","Direct messages","Twitterati","Breaking news", "Photo sharing","Filters","Stories","Influencers","Followers","Hashtags","Explore page","IGTV","Direct messages","Visual content","Social media","Online platform","Networking","Digital advertising","User-generated content","Algorithm","Online community","Engagement","Followership","Viral content","Trending","Privacy","Social influence","Data mining","Mobile app","Online communication","Sharing economy","Online video","Digital marketing","Influencer marketing"]

def common_members(a,b):
  result = collections.Counter(a) & collections.Counter(b)
  ans = len(result.keys())
  return ans

ans = [0,0,0,0,0]     #for storing the number of hits in the websites

for i in range(10):
  visitor_age = random.randint(10,60)
  visitor_new_key = []
  n = random.randint(1,5)
  for j in range(n):
    visitor_new_key.append(random.choice(visitor_keywords))
  # print("age: ", visitor_age, "keywords: ", visitor_new_key)
  
  minInd = 999999999
  minDist = 999999999
  for index in range(5):
    currSc = common_members(visitor_new_key, websites[index]['keywords'])
    currDist = math.sqrt((visitor_age-websites[index]['age'])**2 + currSc*currSc)
    if(currDist < minDist):
      minInd = index
      minDist = currDist

  ans[minInd] = ans[minInd] + 1
print(ans)