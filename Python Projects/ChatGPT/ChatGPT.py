#ChatGPT & Education
from datascience import *
import numpy as np
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# -------------------------------
# TEACHER SURVEY
# -------------------------------
# Q1: Consent to participate
# Options:
#   1. ACCEPT
#   2. DECLINE

# Q2: What is your age?
# Options: Please select one ... 70+

# Q3: What is your gender?
# Options:
#   1. Male
#   2. Female
#   3. Non-binary / third gender
#   4. Prefer not to say

# Q4: In what country do you teach?
# (Open response)

# Q5: How many years of teaching experience do you have?
# (Open response)

# Q6: What grade level do you teach?
# (Open response)

# Q7: What is subject area?
# (Open response)

# Q8: How familiar are you with AI tools such as ChatGPT?
# Options:
#   1. Never heard of or seen them (Not Familiar)
#   2. Knew of them but had not seen or used first-hand (Somewhat Familiar)
#   3. Had briefly tried them (Familiar)
#   4. Extensive experience with them (Very Familiar)

# Q9: Have you used ChatGPT to test answers to questions?
# Options:
#   1. Yes
#   2. No

# Q10: What was the subject area of the questions you asked ChatGPT?
# (Open response)

# Q11: What was the level of the questions you asked ChatGPT?
# (Open response)

# Q12: What sort of question(s) did you give to ChatGPT? (short answer, multiple choice, essay, numerous)
# (Open response)

# Q16: On average, what mark out of 100 would you award ChatGPT's responses?
# (Numeric open response)

teacher = Table.read_table('ChatGPT.csv')
print(teacher)

print(len(teacher.column('Test ChatGPT?')))
print('There are 318 teachers in the survey.\n')

print(teacher.select('Do you consent?').group('Do you consent?'))
print('318 teachers said they consent to the survey.\n')

print(f"Max age of teachers {np.max(teacher.column('What is your age?'))}")
print(f"Median age of teachers {np.median(teacher.column('What is your age?'))}")
print(f"Mean age of teachers {np.round(np.mean(teacher.column('What is your age?')), 2)}")
print(f"Standard Deviation age of teachers {np.round(np.std(teacher.column('What is your age?'), ddof = 1), 2)}")
print(f"Min age of teachers {np.min(teacher.column('What is your age?'))}\n")


teacher.hist('What is your age?', bins = 25)
plt.show()

print(teacher.group('What is your gender?'))
print('129 teachers are male')
print('183 teachers are female')
print('0 teachers are non-binary')
print('6 teachers said they prefer not to say\n')

print(teacher.group('Teaching Region?'))
print('128 teachers teach in America')
print('102 teachers teach in Australasia')
print('71 teachers teach in Europe')
print('17 teachers teach in Other\n')

teacher.group('Teaching Region?').sort('count', descending = True).bar('Teaching Region?')
plt.show()

print(teacher.group('Teaching experience?').sort('count', descending = True))
print('Most teachers have 20 years of teaching experience\n')

print(teacher.group('Grade Level?'))
print('222 teachers teach at the University Level')
print('82 teachers teach at the Secondary Level')
print('14 teachers teach at the Primary Level\n')

teacher.group('Grade Level?').sort('count', descending = True).bar('Grade Level?')
plt.show()

print(teacher.group('Subject Area?').sort('count', descending = True))
print('129 teachers teach Social Sciences')
print('71 teachers teach Arts & Humanities')
print('59 teachers teach Technology')
print('40 teachers teach Physical Sciences')
print('14 teachers teach Life Sciences & Biomedicine')
print('4 teachers teach Non-Specific')
print('1 teachers teach Other\n')

teacher.group('Subject Area?').sort('count', descending = True).bar('Subject Area?')
plt.show()

print(teacher.group('Familiarity AI?'))
print(f'5 teachers are not familiar with AI {np.round((5/318) * 100, 2)}%')
print(f'74 teachers are somewhat familiar with AI {np.round((74/318) * 100, 2)}%')
print(f'154 teachers are familiar with AI {np.round((154/318) * 100, 2)}%')
print(f'85 teachers are very familiar with AI {np.round((85/318) * 100, 2)}%\n')


print(teacher.group('Test ChatGPT?'))
print(f'192 teachers have used AI {np.round((192/318) * 100, 2)}%')
print(f'126 teachers have not used AI {np.round((126/318) * 100, 2)}%\n')

grades = teacher.where('What grade x/100?', lambda x: not np.isnan(x))
print(grades.select('What grade x/100?').sort('What grade x/100?', descending = True))
print(f"Max grade given to ChatGPT {np.max(grades.column('What grade x/100?'))}")
print(f"Mean grade given to ChatGPT {np.round(np.mean(grades.column('What grade x/100?')), 2)}")
print(f"Standard Deviation grade given to ChatGPT {np.round(np.std(grades.column('What grade x/100?'), ddof = 1), 2)}")
print(f"Median grade given to ChatGPT {np.median(grades.column('What grade x/100?'))}")
print(f"Min grade given to ChatGPT {np.min(grades.column('What grade x/100?'))}")