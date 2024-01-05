import pandas as pd

# Columns that contain multiple values.
multi_value_columns = ['AIAcc',
                       'AIDevHaveWorkedWith', 'AIDevWantToWorkWith',
                       'AISearchHaveWorkedWith', 'AISearchWantToWorkWith',
                       'BuyNewTool', 'CodingActivities', 'Country', 'Currency',
                       'DatabaseHaveWorkedWith', 'DatabaseWantToWorkWith',
                       'DevType', 'Employment',
                       'LanguageHaveWorkedWith', 'LanguageWantToWorkWith',
                       'LearnCode', 'LearnCodeCoursesCert', 'LearnCodeOnline',
                       'MiscTechHaveWorkedWith', 'MiscTechWantToWorkWith',
                       'NEWCollabToolsHaveWorkedWith', 'NEWCollabToolsWantToWorkWith',
                       'OfficeStackAsyncWantToWorkWith', 'OfficeStackAsyncHaveWorkedWith',
                       'OfficeStackSyncWantToWorkWith', 'OfficeStackSyncHaveWorkedWith',
                       'PlatformHaveWorkedWith', 'PlatformWantToWorkWith',
                       'ProfessionalTech',
                       'ToolsTechHaveWorkedWith', 'ToolsTechWantToWorkWith',
                       'WebframeHaveWorkedWith', 'WebframeWantToWorkWith',
                       'OpSysPersonal use', 'OpSysProfessional use']

# Columns that contain single values.
single_value_cols = ['Age', 'OrgSize', 'MainBranch', 'RemoteWork', 'EdLevel',
                     'PurchaseInfluence', 'TechList',
                     'AISelect', 'AISent', 'AIBen', 'ICorPM',
                     'Knowledge_1', 'Knowledge_2', 'Knowledge_3', 'Knowledge_4',
                     'Knowledge_5', 'Knowledge_6', 'Knowledge_7', 'Knowledge_8',
                     'Frequency_1', 'Frequency_2', 'Frequency_3',
                     'TimeAnswering', 'TimeSearching', 'Industry']

# AI-specific columns that contain multiple values
AI_cols = ['AIToolCurrently Using', 'AIToolInterested in Using', 'AIToolNot interested in Using',
           'AINextVery different', 'AINextNeither different nor similar', 'AINextSomewhat similar',
           'AINextVery similar', 'AINextSomewhat different']

# Columns we are not interested in - mostly specific to Stack Overflow
cols_to_drop = ['Q120', 'NEWSOSites', 'SOAccount', 'SOVisitFreq', 'SOComm',
                'SOPartFreq', 'SurveyLength', 'SurveyEase', 'TBranch']

other_cols = ['SOAI', 'YearsCode', 'YearsCodePro']


# Columns that contain numeric data that don't need cleaning
numeric_cols = ['ConvertedCompYearly', 'WorkExp', 'CompTotal']

######################################################
# Turn the ; separated values into lists
######################################################
def listify_choices(df, column_name):
    df[column_name] = df[column_name].fillna('')
    df[column_name] = df[column_name].str.lower()
    df[column_name] = df[column_name].str.split(';')
    df[column_name] = df[column_name].astype(object)

######################################################
# Replace text responses with a number and convert
# columns to numeric
######################################################
def clean_num_years(df):
    df['YearsCode'] = df['YearsCode'].replace('Less than 1 year', 0)
    df['YearsCode'] = df['YearsCode'].replace('More than 50 years', 50)
    df['YearsCode'] = pd.to_numeric(df.YearsCode)
    df['YearsCodePro'] = df['YearsCodePro'].replace('Less than 1 year', 0)
    df['YearsCodePro'] = df['YearsCodePro'].replace('More than 50 years', 50)
    df['YearsCodePro'] = pd.to_numeric(df.YearsCodePro)

def tidy_labels(df):
    # Tidy up the org size label text
    df['OrgSize'] = df['OrgSize'].str.replace(' employees', '')
    df['OrgSize'] = df['OrgSize'].str.replace('10,000 or more', '10,000+')
    df['OrgSize'] = df['OrgSize'].str.replace('Just me - I am a freelancer, sole proprietor, etc.', '1')
    df['OrgSize'] = df['OrgSize'].str.replace("I don’t know", 'Unsure')

######################################################
# Removes columns that we are not interested in from
# the data frame
######################################################
def drop_unneeded_columns(df):
    df.drop(cols_to_drop, axis=1, inplace=True)


def clean(df):
    drop_unneeded_columns(df)

    # Turn the ;-separated selections into lists
    for col in multi_value_columns:
        listify_choices(df, col)
    for col in AI_cols:
        listify_choices(df, col)

    # Convert the years of experience columns into numeric.
    clean_num_years(df)

    # Tidy up labels for charts
    tidy_labels(df)


# Opens a file, extracts a single field and writes it to a new file.
# Does not write out null fields.
def extract_field_to_file(from_file, field, to_file):
    df = pd.read_csv(from_file)
    new_df = pd.DataFrame(df[field])

    new_df = new_df.dropna()
    new_df.to_csv(to_file)
    return new_df


# Opens the stack overflow file, cleans it, saves it, and returns a data frame
# containing the data
def open_and_clean_so_file(so_file):
    df = pd.read_csv(so_file)
    clean(df)
    return df