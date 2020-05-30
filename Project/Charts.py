from AI import AI

import matplotlib.pyplot as plt

Values, Labels = AI.Accuracy()

figureObject, axesObject = plt.subplots()

axesObject.pie(Values, labels=Labels, autopct='%1.2f', startangle=90)
axesObject.axis('equal')

plt.show()

Values, Labels = AI.ShareOfRatings()

figureObject, axesObject = plt.subplots()

axesObject.pie(Values, labels=Labels, autopct='%1.2f', startangle=90)
axesObject.axis('equal')

plt.show()