import numpy as np
import pandas as pd

data = pd.read_csv('t2data.csv', skip_blank_lines=True)

env_factors = [
	'Average temperature (°F)',
	'Total annual snowfall (inches)',
	'Average ocean temperature (°C)',
	'Ocean pH level'
]

data = data.dropna(subset=env_factors)
env_data = data[env_factors]

#normalize data
def norm(factor):
	return (factor - factor.min()) / (factor.max() - factor.min() + 1e-10)

norm_data = env_data.apply(norm)

#entropy calculation
epsilon = 1e-10
entro_prop = norm_data / (norm_data.sum(axis=0) + epsilon)
entropy = - (entro_prop * np.log(entro_prop + epsilon)).sum(axis=0) 
entro_weights = (1 - entropy) / (1 - entropy).sum()	

w_env_data = norm_data * entro_weights

factor_weights = {
	'Average temperature (°F)': -1,
	'Total annual snowfall (inches)': 1,
	'Average ocean temperature (°C)': -1,
	'Ocean pH level': 1
}

for i in w_env_data:
	w_env_data[i] *= factor_weights[i]

env_index_raw = w_env_data.sum(axis=1)

scale_factor = 0.2 / env_index_raw.max()
env_index = env_index_raw * scale_factor
#norm_env_index = ((env_index - env_index.min()) / (env_index.max() - env_index.min()))
#env_index = 1 - env_index

data['Environmental Index'] = env_index

print("Entropy Weights:")
print(entro_weights)

print(w_env_data)
print(data[['Year', 'Environmental Index']])







