from dao.db import OracleDb

class TokenFinder:

    def __init__(self):
        self.db = OracleDb()

    def getTokenData(self, token_data=None, password=None):

        if token_data and password:
            token_data = "'{0}'".format(token_data)
            password = "'{0}'".format(password)
        else:
            token_data = 'null'
            password = 'null'
        query = "select * from table(orm_user_skillS.GetSkillData({0}))".format(skill_name)

        result = self.db.execute(query)
        return result.fetchall()




if __name__ == "__main__":

    helper = TokenFinder()