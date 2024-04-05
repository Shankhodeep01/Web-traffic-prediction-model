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
    'keywords': ["Artificial", "Intelligence", "Blockchain", "Internet", "of", "Things", "IoT", "Cybersecurity", "Cloud", "Computing", "Augmented", "Reality", "Virtual", "Reality", "Machine", "Learning", "Data", "Privacy", "Quantum", "Computing", "Robotics", "Big", "Data", "5G", "Networks", "Wearable", "Technology", "Autonomous", "Vehicles", "Biotechnology", "Cryptocurrency", "Automation", "Nanotechnology", "Smart","Cities"]
}
#healthcare
w2 = {
    'category' : 'Healthcare',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': ["Telemedicine", "Electronic", "Health", "Records", "(EHR)", "Precision", "Medicine", "Medical", "Devices", "Healthcare", "Analytics", "Remote", "Patient", "Monitoring", "Health", "Information", "Exchange", "(HIE)", "Digital", "Health", "Personalized", "Medicine", "Health", "Wearables", "Medical", "Imaging", "Genomics", "Health", "Informatics", "Bioinformatics", "Health", "AI", "Telehealth", "Patient", "Engagement", "Health", "Tech", "Startups", "Wearable", "Health", "Sensors", "Healthcare", "Compliance"]
}
#Online Learning
w3 = {
    'category' : 'Education',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': ["Online", "Learning", "E-Learning", "Platforms", "Distance", "Education", "Adaptive", "Learning", "Gamification", "Virtual", "Classrooms", "MOOCs", "(Massive", "Open", "Online", "Courses)", "Blended", "Learning", "Educational", "Technology", "(EdTech)", "Learning", "Management", "Systems", "(LMS)", "Personalized", "Learning", "Mobile", "Learning", "Open", "Educational", "Resources", "(OER)", "Flipped", "Classroom", "Digital", "Literacy", "Educational", "Apps", "AI", "in", "Education", "STEM", "Education", "Competency-Based", "Education", "Lifelong", "Learning"]
}
#Finance
w4 = {
    'category' : 'Finance',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': ["Fintech", "Cryptocurrency", "Blockchain", "in", "Finance", "Mobile", "Payments", "Digital", "Banking", "Robo-Advisors", "Peer-to-Peer", "Lending", "Insurtech", "Regtech", "Financial", "Inclusion", "Open", "Banking", "Artificial", "Intelligence", "in", "Finance", "Cybersecurity", "in", "Banking", "Big", "Data", "Analytics", "in", "Finance", "Contactless", "Payments", "Wealth", "Management", "Payment", "Gateways", "Tokenization", "Neobanks", "Algorithmic", "Trading"]
}
#Environment
w5 = {
    'category' : 'Environment',
    'age': 0,
    'noOfVisitor' : 0,
    'keywords': ["Renewable", "Energy", "Climate", "Change", "Mitigation", "Sustainability", "Carbon", "Footprint", "Green", "Technology", "Circular", "Economy", "Clean", "Energy", "Sustainable", "Development", "Goals", "(SDGs)", "Environmental", "Conservation", "Eco-Friendly", "Practices", "Biodiversity", "Climate", "Resilience", "Carbon", "Capture", "and", "Storage", "(CCS)", "Environmental", "Policy", "Green", "Building", "Water", "Management", "Waste", "Management", "Ecotourism", "Air", "Quality", "Monitoring", "Sustainable", "Agriculture"]
}

websites = [w1, w2, w3, w4, w5]

visitor_keywords = ["Artificial", "Intelligence", "Blockchain", "Internet", "of", "Things", "IoT", "Cybersecurity", "Cloud", "Computing", "Augmented", "Reality", "Virtual", "Reality", "Machine", "Learning", "Data", "Privacy", "Quantum", "Computing", "Robotics", "Big", "Data", "5G", "Networks", "Wearable", "Technology", "Autonomous", "Vehicles", "Biotechnology", "Cryptocurrency", "Automation", "Nanotechnology", "Smart", "Cities", "Telemedicine", "Electronic", "Health", "Records", "(EHR)", "Precision", "Medicine", "Medical", "Devices", "Healthcare", "Analytics", "Remote", "Patient", "Monitoring", "Health", "Information", "Exchange", "(HIE)", "Digital", "Health", "Personalized", "Medicine", "Health", "Wearables", "Medical", "Imaging", "Genomics", "Health", "Informatics", "Bioinformatics", "Health", "AI", "Telehealth", "Patient", "Engagement", "Health", "Tech", "Startups", "Wearable", "Health", "Sensors", "Healthcare", "Compliance" "Online", "Learning", "E-Learning", "Platforms", "Distance", "Education", "Adaptive", "Learning", "Gamification", "Virtual", "Classrooms", "MOOCs", "(Massive", "Open", "Online", "Courses)", "Blended", "Learning", "Educational", "Technology", "(EdTech)", "Learning", "Management", "Systems", "(LMS)", "Personalized", "Learning", "Mobile", "Learning", "Open", "Educational", "Resources", "(OER)", "Flipped", "Classroom", "Digital", "Literacy", "Educational", "Apps", "AI", "in", "Education", "STEM", "Education", "Competency-Based", "Education", "Lifelong", "Learning", "Fintech", "Cryptocurrency", "Blockchain", "in", "Finance", "Mobile", "Payments", "Digital", "Banking", "Robo-Advisors", "Peer-to-Peer", "Lending", "Insurtech", "Regtech", "Financial", "Inclusion", "Open", "Banking", "Artificial", "Intelligence", "in", "Finance", "Cybersecurity", "in", "Banking", "Big", "Data", "Analytics", "in", "Finance", "Contactless", "Payments", "Wealth", "Management", "Payment", "Gateways", "Tokenization", "Neobanks", "Algorithmic", "Trading", "Renewable", "Energy", "Climate", "Change", "Mitigation", "Sustainability", "Carbon", "Footprint", "Green", "Technology", "Circular", "Economy", "Clean", "Energy", "Sustainable", "Development", "Goals", "(SDGs)", "Environmental", "Conservation", "Eco-Friendly", "Practices", "Biodiversity", "Climate", "Resilience", "Carbon", "Capture", "and", "Storage", "(CCS)", "Environmental", "Policy", "Green", "Building", "Water", "Management", "Waste", "Management", "Ecotourism", "Air", "Quality", "Monitoring", "Sustainable", "Agriculture"]

excel_file = '/content/ProjectSurvey.xlsx'
df = pd.read_excel(excel_file)

# Specify the columns you want to read
column1_name = 'Age'  # Replace 'Column1' with the name of your first column
column2_name = 'Enter Keywords separated by comma'  # Replace 'Column2' with the name of your second column

# Extract data from the specified columns into arrays
Age_data = df[column1_name].tolist()
Keywords_data = df[column2_name].tolist()

key = [word.strip() for string in Keywords_data for word in string.split(',')]

output_list = []
for item in key:
    words = item.split()
    output_list.extend(words)

output_list = [item.strip('()') for item in output_list]

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

def automated_input() :
  df = pd.DataFrame({})
  ans = [[0 for i in range(5)] for j in range(7)]    #for storing the number of hits in the websites
  for i in range(300) :
    visitor_age = int(random.choice(Age_data))
    n = random.randint(1,10) #n = number of visitor search keyword
    visitor_new_key = random.sample(output_list, n)

    # for j in range(n) :
    #   visitor_new_key.append(random.choice(visitor_keywords)) #visitor (search) keyword

    minInd = getMinInd(visitor_age, visitor_new_key, n, 2)

    row = getRow(visitor_age)
    # total_age[row] = total_age[row] + 1
    ans[row][minInd] = ans[row][minInd] + 1

    currNoOfVisitor = websites[minInd]['noOfVisitor']

    websites[minInd]['age'] = (websites[minInd]['age']*currNoOfVisitor + visitor_age)/(currNoOfVisitor + 1) #new  web page age
    websites[minInd]['noOfVisitor'] = currNoOfVisitor + 1 # new no. of visitor

  columns = ['Technology', 'Health-Care', 'Education', 'Finance', 'Environment']
  age_groups = ['15-20', '20-25', '25-35', '35-40', '40-50', '50-55', '55-60']

  df = pd.DataFrame(ans, columns=columns, index=age_groups)
    # df = df.append(df2, ignore_index=True)

  # print(ans)
  excel_writer = pd.ExcelWriter('output1.xlsx', engine='openpyxl')
  df.to_excel(excel_writer, sheet_name='Sheet1')
  excel_writer.save()
  print(df)

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

  print("Predicted Domain :- ", websites[minInd]['category'])
  # print("Number of visitor in that particular domain till now: ", currNoOfVisitor + 1)

while(True):
  flag = int(input("Press 1 for manual input or 2 for automated input or 3 to exit: "))
  if(flag == 1):
    manual_input()
  elif (flag == 2):
    automated_input()
  else:
    break
