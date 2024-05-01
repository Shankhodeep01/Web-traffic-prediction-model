# -*- coding: utf-8 -*-
"""Copy of New Web Traffic prediction

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vxCwmQwV7Nmt9vSQCJkVC25wmUzvoqz3
"""

import pandas as pd
import random
import collections
import math
import warnings

# warnings.filterwarnings('ignore')

#Technology
w1 = {
    'category' : 'Technology',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': []
}
#healthcare
w2 = {
    'category' : 'Healthcare',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': []
}
#Online Learning
w3 = {
    'category' : 'Education',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': []
}
#Finance
w4 = {
    'category' : 'Finance',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': []
}
#Environment
w5 = {
    'category' : 'Environment',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': []
}

websites = [w1, w2, w3, w4, w5]

def process_data(Keywords_data):
  Keywords_data = Keywords_data.split(',') # Splitting the string into list
  key = [word.strip() for string in Keywords_data for word in string.split(',')]

  output_list = []
  for item in key:
      words = item.split()
      output_list.extend(words)

  output_list = [item.strip('()') for item in output_list]
  return output_list

def getIndex(domain_name):
    for index in range(len(websites)):
      if(domain_name == websites[index]['category']):
        return index

def feedData(df):
  column_name1 = 'Age'
  column_name2 = 'Keywords'
  column_name3 = 'Domain'

  for index, row in df.iterrows():
    domain_name = row[column_name3]
    website_index = getIndex(domain_name)
    get_keywords = process_data(row[column_name2])
    websites[website_index]['keywords'].extend(get_keywords)

  # print(websites[3])

def common_members(a,b,n):
  result = collections.Counter(a) & collections.Counter(b) #common keywords
  length = len(result.keys())
  return 100-(length/n)*100

def getRow(age) :
  if age >= 55 :
    return 6
  elif age >= 50 :
    return 5
  elif age >= 40 :
    return 4
  elif age >= 35 :
    return 3
  elif age >= 25 :
    return 2
  elif age >= 20 :
    return 1
  elif age >= 15 :
    return 0

def getMinInd(visitor_age, visitor_new_key, n, flag):
  minInd = 999999999
  minDist = 999999999
  if(flag == 1) :
    print("\t\t\tSimilarity Score |", "Current Distance")
  for index in range(5) :
    currSc = common_members(visitor_new_key, websites[index]['keywords'], n)
    currDist = math.sqrt((visitor_age - websites[index]['age'])**2 + currSc*currSc)
    if(flag == 1) :
      print(websites[index]['category'],end=" :\t")
      print("\t",round(currSc,4),"\t\t\t",round(currDist,4))
    if(currDist < minDist) :
      minInd = index
      minDist = currDist
  return minInd

def automated_input(df_data) :
  count_right = 0 # Takes the count of total correct matches
  column_name1 = 'Age'
  column_name2 = 'Keywords'
  column_name3 = 'Domain'

  df_ans = pd.DataFrame({})
  ans = [[0 for i in range(5)] for j in range(7)]    #for storing the number of hits in the websites
  for index, row in df.iterrows() :    # iterating through data
    visitor_age = int(row[column_name1])   # Storing the current visitor age

    visitor_new_key = process_data(row[column_name2])     # Getting the user search keyword

    # for j in range(n) :
    #   visitor_new_key.append(random.choice(visitor_keywords)) #visitor (search) keyword

    minInd = getMinInd(visitor_age, visitor_new_key, len(visitor_new_key), 2) # Getting the index of the website which we predict the user is going to visit

    if(row[column_name3] == websites[minInd]['category']):  # Matching the actual value with the prediction
      count_right = count_right + 1

    ans_row = getRow(visitor_age)       # Getting the visitor age group
    # total_age[row] = total_age[row] + 1
    ans[ans_row][minInd] = ans[ans_row][minInd] + 1   # Updating the Answer matrix

    currNoOfVisitor = websites[minInd]['noOfVisitor']

    websites[minInd]['age'] = (websites[minInd]['age']*currNoOfVisitor + visitor_age)/(currNoOfVisitor + 1) #new  web page age
    websites[minInd]['noOfVisitor'] = currNoOfVisitor + 1 # new no. of visitor

  columns = ['Technology', 'Health-Care', 'Education', 'Finance', 'Environment']
  age_groups = ['15-20', '20-25', '25-35', '35-40', '40-50', '50-55', '55-60']

  df_ans = pd.DataFrame(ans, columns=columns, index=age_groups)
    # df = df.append(df2, ignore_index=True)

  # print(ans)
  excel_writer = pd.ExcelWriter('output1.xlsx', engine='openpyxl')
  df_ans.to_excel(excel_writer, sheet_name='Sheet1')
  excel_writer._save()
  print(df_ans)

  print("Accuracy: ", count_right/len(df)*100,'%')

def manual_input():
  user_age = int(input("Enter your age: "))
  print("Suggestive keywords:")
  words_per_row = 5
  suggested_keywords = ["Open Educational Resources (OER)", "Blockchain", "5G Networks", "Green Building", "Carbon Capture and Storage (CCS)", "Smart Cities", "Algorithmic Trading", "Telehealth", "Sustainable Development Goals (SDGs)", "Climate Resilience", "Flipped Classroom", "Distance Education", "Data Privacy", "Payment Gateways", "Artificial Intelligence in Finance", "Clean Energy", "Digital Health", "Regtech", "Digital Literacy", "Cryptocurrency", "Contactless Payments", "Wearable Health Sensors", "E-Learning Platforms", "Neobanks", "MOOCs (Massive Open Online Courses)", "Machine Learning", "Environmental Policy", "Climate Change Mitigation", "Sustainability", "Health AI", "Health Tech Startups", "Biodiversity", "Lifelong Learning", "Renewable Energy", "Water Management", "Autonomous Vehicles", "Virtual Reality", "Precision Medicine", "Air Quality Monitoring", "Financial Inclusion", "Digital Banking", "Biotechnology", "Cybersecurity", "Educational Apps", "Nanotechnology", "Healthcare Analytics", "Medical Devices", "Competency-Based Education", "Health Information Exchange (HIE)", "Blended Learning", "Educational Technology (EdTech)", "Wearable Technology", "Personalized Learning", "Augmented Reality", "Healthcare Compliance", "Eco-Friendly Practices", "Patient Engagement", "Personalized Medicine", "Automation", "Gamification", "Big Data Analytics in Finance", "Robo-Advisors", "Environmental Conservation", "Health Wearables", "Genomics", "Financial Inclusion", "Health Informatics", "AI in Education", "Educational Technology (EdTech)", "Wealth Management", "Precision Medicine", "Sustainable Agriculture", "Remote Patient Monitoring", "Robo-Advisors", "Digital Literacy", "Healthcare Analytics", "Telemedicine", "Biotechnology", "AI in Education", "Big Data", "Healthcare Compliance", "Artificial Intelligence", "Circular Economy", "Insurtech", "Personalized Medicine", "E-Learning Platforms", "Healthcare Compliance", "Blockchain in Finance", "Cybersecurity in Banking", "Peer-to-Peer Lending", "Medical Imaging", "Financial Inclusion", "Open Banking", "Machine Learning", "Wearable Technology", "Regtech", "Virtual Classrooms", "Telehealth", "Waste Management", "Eco-Friendly Practices", "Health Information Exchange (HIE)", "Educational Apps", "Digital Banking", "5G Networks", "Sustainable Agriculture", "Health AI", "Online Learning", "Cryptocurrency", "Algorithmic Trading", "Digital Health", "Educational Apps", "Green Technology", "Virtual Reality", "IoT", "Environmental Policy", "Bioinformatics"]

  for i in range(0, len(suggested_keywords), words_per_row):
      row = ", ".join(suggested_keywords[i:i + words_per_row])
      print(row)
  user_manual = list(input("Enter upto 10 search keyword: ").split(" "))

  minInd = getMinInd(user_age, user_manual, len(user_manual), 1)

  currNoOfVisitor = websites[minInd]['noOfVisitor']

  websites[minInd]['age'] = (websites[minInd]['age']*currNoOfVisitor + user_age)/(currNoOfVisitor + 1) #new  web page age
  websites[minInd]['noOfVisitor'] = currNoOfVisitor + 1 # new no. of visitor

  print("Predicted Domain :- ", websites[minInd]['age'], websites[minInd]['category'], )
  # print("Number of visitor in that particular domain till now: ", currNoOfVisitor + 1)

excel_file = '/content/ProjectSurvey.xlsx'
df = pd.read_excel(excel_file)
feedData(df)

while(True):
  flag = int(input("Press 1 for manual input or 2 for automated input or 3 to exit: "))
  if(flag == 1):
    manual_input()
  elif (flag == 2):
    automated_input(df)
  else:
    break