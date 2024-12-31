

import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv", header=None, names=[
        "age", "workclass", "fnlwgt", "education", "education-num",
        "marital-status", "occupation", "relationship", "race", "sex",
        "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
    ])

    # How many people of each race are represented in this dataset?
    race_count = df["race"].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, Doctorate) make more than 50K?
    advanced_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    high_salary = df["salary"] == ">50K"
    higher_education_rich = round((df[advanced_education & high_salary].shape[0] / df[advanced_education].shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round((df[~advanced_education & high_salary].shape[0] / df[~advanced_education].shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_workers = df["hours-per-week"] == min_work_hours
    rich_min_workers_percentage = round((df[min_workers & high_salary].shape[0] / df[min_workers].shape[0]) * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_total = df["native-country"].value_counts()
    highest_earning_country_percentage = round((country_salary / country_total).max() * 100, 1)
    highest_earning_country = (country_salary / country_total).idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = df[(df["native-country"] == "India") & high_salary]
    top_IN_occupation = india_high_salary["occupation"].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_min_workers_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_min_workers_percentage": rich_min_workers_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }