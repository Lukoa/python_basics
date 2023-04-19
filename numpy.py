import numpy as np

carl=[73, 67,43]
weight=[0.3, 0.2, 0.5]
def crop_yield(carl, weight):
    result=0
    for x, w in zip(carl, weight):
        result +=x*w
    return result

print(crop_yield(carl, weight))       