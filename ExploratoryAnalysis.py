import pandas as pd
from collections import Counter

######################################################
# Given any number of column names, print the unique
# values in each column
######################################################
def print_unique_values(df, *col_names):
    # Get the unique values from the column of lists
    for col_name in col_names:
        unique_values = set(df[col_name].apply(pd.Series).stack().unique())
        print(f"The unique values for {col_name} are: {unique_values}\n")


######################################################
# Prints the unique values for the columns we care about
# not including IDs, comments.
######################################################
def print_most_unique_values(df):
    cols_to_drop = ['ResponseId', 'SOAI', 'CompTotal', 'ConvertedCompYearly', 'WorkExp', 'YearsCode', 'YearsCodePro',
                    'Knowledge_2', 'Knowledge_3', 'Knowledge_4', 'Knowledge_5', 'Knowledge_6', 'Knowledge_7',
                    'Knowledge_8',
                    'Frequency_2', 'Frequency_3']
    df.drop(cols_to_drop, axis=1, inplace=True)
    print_unique_values(df, *df.columns)


######################################################
# Returns a set of the unique values in a single column
######################################################
def get_unique_values(df, col_name):
    # Get the unique values from the column of lists
    return set(df[col_name].apply(pd.Series).stack().unique())


######################################################
# Prints data frame head information, all columns
# specify number of rows, defaults to 10
######################################################
def print_verbose_summary(df, n=10):
    print(df.info())
    with pd.option_context('display.max_columns', None):
        print(df.head(n))


######################################################
# Prints the number of rows, columns, and lists the
# column names
######################################################
def print_short_summary(df):
    print(f'\nThis data frame has {df.shape[0]} rows and {df.shape[1]} columns.')
    print(f'The columns are: \n{df.columns}')


######################################################
# Prints the number of null values in each column
######################################################
def print_number_null_values(df):
    print("\nDisplaying the number of null values in each column: ")
    with pd.option_context('display.max_rows', None):
        print(df.isnull().sum())
    print("\n")


def print_number_entries(df, col_name):
    # for each of the unique items in the col name.
    # print the number of times it occurs
    print(f"\nUnique values for the column {col_name}")
    occurrences = get_number_occurrences_each_field(df, col_name)
    print(occurrences)
    return occurrences

def get_number_occurrences_each_field(df, col_name):
    unique_values = get_unique_values(df, col_name)
    occurrences = dict.fromkeys(unique_values, 0)
    df[col_name].apply(lambda x:  [occurrences.update({i: occurrences[i] + x.count(i)}) for i in set(x)])
    return occurrences
