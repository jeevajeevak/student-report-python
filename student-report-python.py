import pandas as pd

# student data

data = {
    'Name' : ['ravi', 'jeeva', 'kumar', 'loki','arun'],
    'Subjects':['Python', 'java', 'python', 'java', 'python'],
    'marks':[85,69,75, 40, 90],
    'status' : ['pass', 'pass', 'pass', 'fail', 'pass']
}

df = pd.DataFrame(data)

#report

print("======== Student Report ========");
print(f"total Student: {len(df)}");
print(f"no of student passed : {len(df[df['status'] == 'pass'])}");
print(f"No of student Failed : {len(df[df['status'] == 'fail'])}");


print("Average marks : ", df['marks'].mean());
print("Highest mark : ", df['marks'].max());
print("lowest mark : ", df['marks'].min());


print("\n failed student");
print(df[df['status'] == 'fail'][['Name', 'marks', 'Subjects']]);

print("\n topper student");
print(df[df['marks'] == df['marks'].max()][['Name', 'marks']]);