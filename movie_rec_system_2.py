#Movie recommendation system using jaccard distances
dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf','raw','lucy'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user_1 = {'matrix','kgf','dabang','dhamaal','uri','bala','thor'}
user_2 = {'kgf','it','uri','thor','dabang','raw','lucy','bala'}
scores = {}

# 1. find out that category whose movies are most common between two users
# 2. recommend those movies which user_1 has not seen yet but user_2 has seen and
# those movies must belong to the category that we found in step 1
