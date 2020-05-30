from sqlalchemy.engine import create_engine


ENGINE_PATH_WIN_AUTH = 'postgres://mxchnqfmkzqsll:be03eda40ed8f0eda91df2caeb926edd199e9ec9a63852f8690a8f657c550030@ec2-52-70-15-120.compute-1.amazonaws.com:5432/d58h6jhh3gu5od'

engine = create_engine(ENGINE_PATH_WIN_AUTH)