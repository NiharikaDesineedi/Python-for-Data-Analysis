import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain exactly nine numbers.")

    arr = np.array(input_list).reshape(3, 3)

    return {
        'mean': [np.mean(arr, axis=0).tolist(), np.mean(arr, axis=1).tolist(), np.mean(arr).item()],
        'variance': [np.var(arr, axis=0).tolist(), np.var(arr, axis=1).tolist(), np.var(arr).item()],
        'standard deviation': [np.std(arr, axis=0).tolist(), np.std(arr, axis=1).tolist(), np.std(arr).item()],
        'max': [np.max(arr, axis=0).tolist(), np.max(arr, axis=1).tolist(), np.max(arr).item()],
        'min': [np.min(arr, axis=0).tolist(), np.min(arr, axis=1).tolist(), np.min(arr).item()],
        'sum': [np.sum(arr, axis=0).tolist(), np.sum(arr, axis=1).tolist(), np.sum(arr).item()]
    }
