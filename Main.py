import LoadAndClean as lc
import ExploratoryAnalysis as ea
import AnalyzeCleaned as ac

#############################################################
# This is the main script that does the data analysis.
# Comment or uncomment the lines as appropriate
#############################################################

#############################################################
# Open and clean the data
#############################################################
# Open the stack overflow file and clean it
df = lc.open_and_clean_so_file("so2023.csv")

# Extract the comments from the question asking how stack overflow should incorporate AI
# and save it to a file.
# soai_comments_df = lc.extract_field_to_file("so2023.csv", 'SOAI', 'so2023-comments-only.csv')

#############################################################
# Exploratory data analysis
#############################################################
#ea.print_short_summary(df)
#ea.print_number_null_values(df)
#ea.print_verbose_summary(df)

# Print out the unique values in columns where it makes sense
#ea.print_most_unique_values(df)

# Print unique values for specific fields.
#ea.print_unique_values(df, 'Age', 'OfficeStackAsyncWantToWorkWith', 'OfficeStackAsyncHaveWorkedWith')
# have_occurrences = ea.print_number_entries(df,'OfficeStackAsyncHaveWorkedWith')
# want_occurrences = ea.print_number_entries(df,'OfficeStackAsyncWantToWorkWith')
#
# for key in have_occurrences:
#     value_have = have_occurrences[key]
#     value_want = want_occurrences[key]
#     print(f"want/have ratio = {key}:  {value_want/value_have}")


#############################################################
# Admired desired analysis
#############################################################
all_values = ea.get_unique_values(df, 'OfficeStackAsyncHaveWorkedWith')
# ac.admired_desired_analysis(df,  'OfficeStackAsyncHaveWorkedWith', 'OfficeStackAsyncWantToWorkWith', 70750,  *all_values)
software_bug_tracking = ['jira', 'clickup', 'youtrack',  'shortcut',  'notion', 'linear', 'azure devops',
                         'github discussions', 'airtable']
general_project_mgmt = ['asana', 'wrike', 'redmine', 'monday.com',  'leankor', 'swit', 'cerri', 'wimi', 'workzone', 'miro',
                        'adobe workfront', 'microsoft lists', 'dingtalk (teambition)', 'trello', 'planview projectplace or clarizen',
                        'microsoft planner', 'nuclino', 'basecamp', 'smartsheet']
documentation_tools =['redocly', 'doxygen', 'wikis', 'markdown file', 'confluence', 'stack overflow for teams', 'document360',
                      'tettra']
ac.admired_desired_analysis(df,  'OfficeStackAsyncHaveWorkedWith', 'OfficeStackAsyncWantToWorkWith', 70750, 'desired_admired.csv',
                            *software_bug_tracking)


#############################################################
# Generate charts
#############################################################
# ac.double_histogram_years_code_years_code_pro(df)
