import numpy as np



def pairwise_cosine_similarity(X):
    def cos_sim(a,b):
        if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
            return 0.0
        else:
            return np.round(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)),4)
    
    similarities = []
    for i in range(len(X)):
        row = []
        for other in X:
            row.append(cos_sim(X[i],other))
            
        similarities.append(row)
        row = []


    return similarities