# Numerical arrays
import numpy as np
# Data frames.
import pandas as pd
# Plotting
import matplotlib.pyplot as plt
# neural neworks
import tensorflow.keras as kr

model = kr.models.load_model('model.h5')
model.predict([5])