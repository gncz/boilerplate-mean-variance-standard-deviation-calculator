import numpy as np

def calculate(list):    
    # input validation
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    elif np.any(list) == False:
        raise ValueError("Invalid numbers.")
                
    #creating a new array of 3x3
    reshaped_array = np.array(list, dtype = 'float').reshape(3,3)

    #initializing the required keys with empty arrays
    calculations = {
        "mean": [],
        "variance": [],
        "standard deviation": [],
        "min": [],
        "max": [],
        "sum": []
        }

    for axis in range(2):
        calculations["mean"].append(reshaped_array.mean(axis=axis).tolist())
        calculations["variance"].append(reshaped_array.var(axis=axis).tolist())
        calculations["standard deviation"].append(reshaped_array.std(axis=axis).tolist())
        calculations["min"].append(reshaped_array.min(axis=axis).tolist())
        calculations["max"].append(reshaped_array.max(axis=axis).tolist())
        calculations["sum"].append(reshaped_array.sum(axis=axis).tolist())

    calculations["mean"].append(reshaped_array.mean())
    calculations["variance"].append(reshaped_array.var())
    calculations["standard deviation"].append(reshaped_array.std())
    calculations["min"].append(reshaped_array.min())
    calculations["max"].append(reshaped_array.max())
    calculations["sum"].append(reshaped_array.sum())

    return calculations