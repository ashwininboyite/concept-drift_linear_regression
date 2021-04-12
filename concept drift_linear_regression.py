import pandas as pd
import numpy as np
from scipy.stats import ks_2samp
from scipy.stats import binom_test

#modelop.init
def begin():
    global train, actual_values
    train = pd.read_csv('training_data.csv')
    actual_values = train.price
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    predicted_values = data.price
    pvalue = ks_2samp(actual_values, predicted_values)[1]
    
    yield {"pvalue": pvalue}
