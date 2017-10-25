import numpy as np
import pickle
import sys
from profile_details import *

number_clusters = 200
scoring_weights = np.array([1.2, 0.5, 1.02, 1, 1.9, 2.5])
clustering_weights = scoring_weights**0.5


def euclid_dist(vec1, vec2):
    return np.sum(np.square(np.subtract(vec1, vec2))) ** 0.5


# Now load sorted cluster_centers
with open("cluster_centers.pkl", 'rb') as file:
    sorted_clusters = pickle.load(file)
    
    
def predict(features):
    features = features * clustering_weights
    dists = []
    for i in range(number_clusters):
        dists.append(euclid_dist(features, sorted_clusters[i]))
    cluster_number = dists.index(min(dists))
    return cluster_number + 1

# Now to scrap a particular profile and then take info from there
if len(sys.argv) == 1:
    profile = scrapprofile("https://github.com/yugrocks")
else:
    profileurl = sys.argv[1]
    if not ("https://github.com/" in profileurl): # could be a github handle
        profileurl = "https://github.com/" + profileurl
    profile = scrapprofile(profileurl)
features = [profile["num_followers"],
            profile["num_stars"],
            profile["forks"],
            profile["num_followings"],
            profile["num_repositories"],
            profile["stars_received"]
            ]
print("Profile Level = ", predict(features))
