#Movie recommendation system using jaccard distances
dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user = {'matrix','kgf','dabang','dhamaal','uri','bala','thor'}
scores = {}

for key in dataset:
    movies = dataset[key]
    movies = set(movies)
    numer = len(user.intersection(movies))
    denom = len(user.union(movies))
    sim = numer / denom
    scores[key] = round(sim,2)

print(scores)

'''
1. Find key whose value is max
2. Find all movies of that key only
3. Now show only those movies which user has not seen yet
'''

category = max(scores, key=scores.get)
print("User has watched {} movies max".format(category))

rec_category = dataset[category]
rec_movies = set(rec_category) - user
print("Recommended movies are",rec_movies)

