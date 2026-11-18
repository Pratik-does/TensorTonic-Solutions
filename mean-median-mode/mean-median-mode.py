from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    mean = np.mean(x)
    median= np.median(x)
    count=Counter(x)
    max_frequency=max(count.values())
    mode=min(value for value, frequency in count.items()
                        if  frequency == max_frequency)
    return {
        "mean":float(mean),
        "median":float(median),
        "mode":float(mode)
    }