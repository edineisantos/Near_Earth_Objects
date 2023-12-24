# Import the necessary functions from extract.py
from extract import load_neos, load_approaches

# Load data using the functions with their default file paths
neos = load_neos()
approaches = load_approaches()

# Print some of the loaded data to verify
print("Loaded NEOs:")
for neo in neos[:10]:  # Print the first 10 NEOs
    print(neo)

print("\nLoaded Close Approaches:")
for approach in approaches[:10]:  # Print the first 10 Close Approaches
    print(approach)