
# import pandas
import pandas as pd

# load file contents
data = pd.read_csv(r'grades.csv')

# calculate the average grade for each student 
average_grades = data.groupby('Student Name')['Grade'].mean()

# calculate and display the maxiumum grade in the class
max_grade = data['Grade'].max()
print('Highest grade in the class: ', max_grade)

# calculate and display the minimum grade in the class
min_grade = data['Grade'].min()
print('Lowest grade in the class: ', min_grade)

# calculate and display the overall class average
class_average = data['Grade'].mean()
print('Average grade of the class: ', class_average)

# add pass or fail column
data['Pass/Fail'] = data['Grade'].apply(lambda x: 'Pass' if x >= 60 else 'Fail')
print(data)

# count the number of students who passed or failed
pass_count = data[data['Pass/Fail'] == 'Pass'].shape[0]
fail_count = data[data['Pass/Fail'] == 'Fail'].shape[0]
print('Number of students passed:', pass_count)
print('Number of students failed', fail_count)
