import re
import os
import pandas as pd


# This should be a list of regex expressions.
# A regex expression should be wrapped in quotes
# and start with the character r. For example,
# the expressions in the list are actually \w+
# and \w+abab
EXPRESSIONS = [r"robinhood"]

# The dataset should reside in a CSV file
# in the same directory as this script on your machine.
# DATA_CSV should be set to the name of the file.
DATA_CSV = "dataset.csv"

# The rows that contain matches will be written to
# another CSV file. SAVE_CSV contains the filename
SAVE_CSV = "filtered.csv"



def matches(row):
	"""
	Returns if a row in the table
	matches an expression in EXPRESSIONS
	"""
	for exp in EXPRESSIONS:
		prog = re.compile(exp)
		match = prog.match(row["comment_text"])
		if match:
			return True
	return False


def main():
	"""
	Entrypoint
	"""
	# Read in the dataset as a pandas DataFrame
	dataset = pd.read_csv(DATA_CSV)
	assert "comment_text" in dataset.columns

	# Apply the matches function to each row
	# of the DataFrame and retains rows that
	# evaluate to true
	mask = dataset.apply(func=matches, axis=1)
	dataset = dataset[mask]

	# save the dataset
	dataset.to_csv(SAVE_CSV, index=True)

	print("Found %s matches" % dataset.shape[0])


if __name__ == "__main__":

	main()

