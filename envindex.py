import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

def plot_envindex(data):
    plt.figure()
    plt.bar(data['Year'], data['Environmental Index'], color='skyblue')
    plt.xlabel('Year')
    plt.ylabel('Environmental Index')
    plt.title('Environmental Index by Year')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

plot_envindex(data)

def plot_envindex_vs_tourists(data):
    years = data['Year']
    env_index = data['Environmental Index']
    tourists = data['Tourist count (million)']

    fig, ax1 = plt.subplots(figsize=(8,5))

    #envindex on left y-axis
    ax1.plot(years, env_index, color='green', marker='o', linewidth=2, label='Environmental Index')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Environmental Index', color='green')
    ax1.tick_params(axis='y', labelcolor='green')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)

    #tourist count on second y-axis
    ax2 = ax1.twinx()
    ax2.plot(years, tourists, color='blue', marker='s', linewidth=2, label='Tourist count (million)')
    ax2.set_ylabel('Tourist count (million)', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

    plt.title('Environmental Index and Tourist Count vs Year')
    plt.tight_layout()
    plt.show()

plot_envindex_vs_tourists(data)
