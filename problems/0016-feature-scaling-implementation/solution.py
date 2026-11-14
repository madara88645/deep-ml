import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = [np.round((x- np.mean(data, axis=0))/np.std(data,axis=0),4) for x in data]
    normalized_data = [np.round((x - np.min(data,axis=0)) / (np.max(data,axis=0)-np.min(data,axis=0)),4)for x in data]
    return standardized_data, normalized_data