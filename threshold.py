import pandas as pd
df = pd.read_excel('Threshold.xlsx')
for i in range(22):
    df[f'E{i}'] = 0
current_user = None
current_task = None
current_error = None
consecutive_count = 0
for index, row in df.iterrows():
    if (
        row['UserID'] == current_user
        and row['taskid'] == current_task
        and row['errorClasses'] == current_error
    ):
        consecutive_count += 1
    else:
        consecutive_count = 1
    threshold = (
        2 if row['errorClasses'] == 2 else
        3 if row['errorClasses'] == 3 else
        4 if row['errorClasses'] == 5 else
        5
    )
    if consecutive_count == threshold:
        df.at[index, f'E{row["errorClasses"]}'] += 1
        consecutive_count = 0
    current_user = row['UserID']
    current_task = row['taskid']
    current_error = row['errorClasses']
df.to_excel('student_info.xlsx', index=False)
