#import pandas as pd

# Load the dataset
#data = pd.read_csv('higgs_boson_data.csv')

# Filter for training set
#training_set = data[data['KaggleSet'] == 't']

# Filter for public leaderboard test set
#public_test_set = data[data['KaggleSet'] == 'b']

# Filter for private leaderboard test set
#private_test_set = data[data['KaggleSet'] == 'v']

# Filter for unused events
#unused_set = data[data['KaggleSet'] == 'u']
import pandas as pd

# Load the full dataset
data = pd.read_csv('higgs_boson_data.csv')

# Filter for public and private leaderboard test sets (test set)
test_set = data[(data['KaggleSet'] == 'b') | (data['KaggleSet'] == 'v')]

# Generate the solution file in the format: EventId, Class, Weight
solution_file = test_set[['EventId', 'Label', 'Weight']]
solution_file.columns = ['EventId', 'Class', 'Weight']

# Save the solution file
solution_file.to_csv('solution.csv', index=False)

print("Solution file generated and saved as 'solution_file.csv'")