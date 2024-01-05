import pandas as pd
from matplotlib import pyplot as plt


#############################################################
# Returns a data frame that contains the responses for users
# who use the tool tool_name from the column column_name
#
# Example: Get responses for people who have used Jira
# jira_users = get_users(df, 'OfficeStackAsyncHaveWorkedWith', 'Jira')
#############################################################
def get_users(df, column_name, tool_name):
    df_use = df[df[column_name].apply(lambda x: tool_name.lower() in x)]
    return df_use


#############################################################
# Sample double histogram code.
#############################################################
def double_histogram_years_code_years_code_pro(df):
    # Show a double histogram of YearsCode and YearsCodePro.
    plt.hist(df['YearsCode'], alpha=0.5)
    plt.hist(df['YearsCodePro'], alpha=0.5)
    plt.show()
    plt.clf()


#############################################################
# Sample double histogram code.
#############################################################
def admired_desired_analysis(df, have_worked_with_field, want_work_with_field, num_responses, out_file, *product_names):
    results_df = pd.DataFrame()
    for product_name in product_names:
        df2 = pd.DataFrame()
        df2[have_worked_with_field] = df[have_worked_with_field]
        df2[want_work_with_field] = df[want_work_with_field]

        df2['tH'] = df[have_worked_with_field].apply(lambda x: product_name in x)
        df2['tW'] = df[want_work_with_field].apply(lambda x: product_name in x)
        df2['tHtW'] = df2['tH'] & df2['tW']
        df2['tHfW'] = df2['tH'] & ~df2['tW']
        df2['fHtW'] = ~df2['tH'] & df2['tW']
        tHtW = df2['tHtW'].sum()
        tHfW = df2['tHfW'].sum()
        fHtW = df2['fHtW'].sum()
        desired = round(((tHtW + fHtW) / num_responses) * 100, 2)
        admired = round((tHtW / (tHtW + tHfW)) * 100, 2)
        spread = round(admired - desired, 2)
        new_df = pd.DataFrame({'Name': [product_name], 'Desired': [desired], 'Admired': [admired], 'Spread': [spread]})
        results_df = pd.concat([results_df, new_df], ignore_index=True)
    print(results_df.head(50))
    results_df.to_csv(out_file, index=False)
