# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 11:30:34 2019

@author: Vipul
"""

# Get coefficients of the roots
def get_coefficients(x1, x2):
    a = 1
    b = - (x1 + x2)
    c = x1*x2
    return a, b, c

# Generate random roots
import random
def generate_random_roots():
    x1 = random.randint(1, 1001)
    x2 = random.randint(1, 1001)
    return x1, x2

# Generate dataset
def generate_dataset(num_rows = 1000):
    dataset = []
    for _ in range(num_rows):
        x1, x2 = generate_random_roots()
        a, b, c = get_coefficients(x1, x2)
        dataset.append([a, b, c, x1, x2])
        
    return dataset

dataset = generate_dataset()

# Save dataset to csv file
import pandas as pd
df = pd.DataFrame(data = dataset, columns = ["a", "b", "c", "x1", "x2"])
df.to_csv("Quadratic_Data.csv", index=False)