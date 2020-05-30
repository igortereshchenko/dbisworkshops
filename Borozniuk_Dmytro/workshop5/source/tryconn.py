import cx_Oracle
import pandas as pd
import plotly
import plotly.graph_objs as go
import numpy as np
import json
import matplotlib.pyplot as plt


username = 'MYONLINEEDU'
password = 'MYONLINEEDU'
databaseName = "localhost:1521/xe"

connection = cx_Oracle.connect(username, password, databaseName)
cursor = connection.cursor()
query = 'SELECT * FROM services'
b = cursor.execute(query)
d = []
c = []
for i in b:
    d.append(i[0])
    c.append(i[1])
indexx = [i+1 for i in range(len(d))]
g = list(zip(d,c))#reqiered variable for making a table in services html file


# query222 = 'select SUBSTR(when_date,1,30) Time1, SUBSTR(CURRENT_DATE,1,30) Time2, SUBSTR((CURRENT_DATE-when_date),1,30) Timediff FROM wish'
# diff_date = cursor.execute(query222)
# d_d = []
# for i in diff_date:
#     d_d.append(i[2])
# print(d_d)
#
#first_date = '+000000000 03:11:38'
#
# if first_date[0] == '+' and int(first_date[12])>=1:
#     print(True)
# else:
#     print(False)


# query1 = 'select SERVICE_NAME, sum(wish.PRICE) price from wish group by SERVICE_NAME'
# prserv = cursor.execute(query1)
# namee = []
# total_cash = []
# for i in prserv:
#     namee.append(i[0])
#     total_cash.append(i[1])

# print(namee)
# print(total_cash)
# plt.bar(namee, total_cash)
# plt.show()

def create_plot():
    query1 = 'select SERVICE_NAME, sum(wish.PRICE) price from wish group by SERVICE_NAME'
    prserv = cursor.execute(query1)
    namee = []
    total_cash = []
    for i in prserv:
        namee.append(i[0])
        total_cash.append(i[1])
    #
    # N = 40
    # x = np.linspace(0, 1, N)
    # y = np.random.randn(N)

    df = pd.DataFrame({'x': namee, 'y': total_cash}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


