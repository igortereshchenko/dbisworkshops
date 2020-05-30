import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from database_connection import engine

df_ora = pd.read_sql("""SELECT GRADE,DURATION,COMPLEXITY,LENGTH,
                        MAX_HEIGHT_INC,MAX_HEIGHT_RED,
                        AVERAGE_HEIGHT_INC,AVERAGE_HEIGHT_RED,
                        AVERAGE_DAY_KM,EQUIPMENT,HEALTHY,
                        EXTRACT(YEAR FROM sysdate)-EXTRACT(YEAR FROM BIRTH_DATE) AS AGE,
                        HEIGHT,WEIGHT
                        
                        FROM HIKES,FEATURE,ORDERS

                        WHERE FEATURE_ID=FK_FEATURE_ID AND HIKE_ID=FK_HIKE_ID""", con=engine)
# print(df_ora)

Data = df_ora.drop('grade', 1)
Grades = df_ora['grade']

X_train, X_test, y_train, y_test = train_test_split(Data, Grades,
                                                    random_state=9)

clf = SVC(kernel='rbf', gamma=0.0001).fit(X_train, y_train)



# print(clf.predict(X_train))


class AI(object):
    clf

    @classmethod
    def TablePrediction(cls, data):
        result = clf.predict(data)
        return result

    @classmethod
    def SortByComplexity(cls, data, user_complexity):
        data['predict_complexity'] = cls.TablePrediction(data.drop("hike_name", 1))
        data['sort'] = abs(data['complexity'] - user_complexity)
        data = data.sort_values("sort").drop(["sort", "age", "equipment", "healthy", "height", "weight"], 1)
        return data

    @classmethod
    def SortForID(cls, id, user_complexity):
        df_ora = pd.read_sql("""SELECT HIKE_NAME,DURATION,COMPLEXITY,LENGTH,
                                MAX_HEIGHT_INC,MAX_HEIGHT_RED,
                                AVERAGE_HEIGHT_INC,AVERAGE_HEIGHT_RED,
                                AVERAGE_DAY_KM,EQUIPMENT,HEALTHY,
                                EXTRACT(YEAR FROM sysdate)-EXTRACT(YEAR FROM BIRTH_DATE) AS AGE,
                                HEIGHT,WEIGHT
                                                        
                                FROM HIKES,FEATURE
                                
                                WHERE FEATURE_ID={}""".format(id), con=engine)

        return cls.SortByComplexity(df_ora, user_complexity)

    @classmethod
    def Serialise(cls, data):
        result = [{a: b for a, b in zip(data.columns.tolist(), data.values[i])}.items() for i in
                  range(len(data.values))]
        return result

    @classmethod
    def Accuracy(cls):
        Corrected = clf.score(X_train, y_train)
        Uncorrected = 1 - Corrected
        return [Corrected, Uncorrected], ['Corrected', 'Uncorrected']

    @classmethod
    def ShareOfRatings(cls):
        result = df_ora['grade'].value_counts()
        return result.values, result.index

