#import cPickle as pickle
import pickle
import numpy as np

#pickle.dump([embeddings], open('embeddings_from_XYZ.p', 'wb'))

# ../
load_path = "ebmeddings_from_celeb_12k_noflips_160px.p"
load_path = "embeddings_from_celeb_12kwithflips_160px.p"
load_path = "embeddings_from_celeb_30k_noflip_160px.p"
with open(load_path, "rb") as input_file:
    embeddings = pickle.load(input_file, encoding='latin1')

print("embeddings",embeddings)
print("embeddings",len(embeddings[0]))
#print("embeddings.shape" ,embeddings.shape)


embeddings_n = np.asarray(embeddings)
print("embeddings_n",embeddings_n)
print("embeddings_n.shape" ,embeddings_n.shape)
