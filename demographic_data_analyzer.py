import pandas as pd

# URL to the Adult dataset file
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

# Define column names as per the dataset description
columns = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
]

# Load the dataset
df = pd.read_csv(url, header=None, names=columns, skipinitialspace=True)

# Display the first few rows
print(df.head())
#counting no of races in the dataset
race_count=df['race'].value_counts()
print(race_count)
#avg age of men
men_avg_age=df[df['sex']=='Male']['age'].mean()
print("avg age of the men:",men_avg_age)
#bachelors degree count
bd=df[df['education']=='Bachelors'].shape[0] #shape counts no of rows of bachelors degree
percent=(bd/5)*100
print(percent)
#percentage of people who have adv education income greater than >50K
advanced_education = ['Bachelors', 'Masters', 'Doctorate']
adved_count=df[df['education'].isin(advanced_education)]
income=adved_count[adved_count['salary']=='>50K']
income_percent=(income.shape[0]/adved_count.shape[0])*100
print(f"Percentage of people with advanced education making more than 50K: {income_percent:.2f}%")
#percentage of people who do  not have adv ed making >50K
non_adved_count=df[~df['education'].isin(advanced_education)]
income_nonadv=non_adved_count[non_adved_count['salary']=='>50K']
income_nonadv_percent=(income_nonadv.shape[0]/non_adved_count.shape[0])*100
print(f"Percentage of people with no advanced education making more than 50K: {income_nonadv_percent:.2f}%")
#min no of hours per week
min_hours=df['hours-per-week'].min()
min_hours_df = df[df['hours-per-week'] == min_hours]
print("min no of hours per week:",min_hours)
# percentage of the people who work the minimum number of hours per week have a salary of more than 50K
high_income_min_hours=min_hours_df[df['salary']=='50K']
high_salary_percent=(high_income_min_hours.shape[0] / min_hours_df.shape[0]) * 100
if min_hours_df.shape[0] > 0:  # Avoid division by zero
    percentage_min_hours_high_income = (high_income_min_hours.shape[0] / min_hours_df.shape[0]) * 100
else:
    percentage_min_hours_high_income = 0
print(f"Percentage of people who work the minimum number of hours per week and earn >50K: {high_salary_percent:.2f}%")
# country with the highest percentage of people earning >50K
total_per_country = df['native-country'].value_counts()
high_income_per_country = df[df['salary'] == '>50K']['native-country'].value_counts()
percentage_per_country = (high_income_per_country / total_per_country) * 100
max_country = percentage_per_country.idxmax()
max_percentage = percentage_per_country.max()
print(f"The country with the highest percentage of people earning >50K is: {max_country}")
print(f"The percentage is: {max_percentage:.2f}%")
#the most popular occupation in india with salary >50K
india_high_income = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
most_popular_occupation = india_high_income['occupation'].value_counts().idxmax()
print(f"The most popular occupation for those earning >50K in India is: {most_popular_occupation}")