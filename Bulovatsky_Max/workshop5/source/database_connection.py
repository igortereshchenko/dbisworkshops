from sqlalchemy.engine import create_engine

ENGINE_PATH_WIN_AUTH = "postgres://acfwdjeahlsvgl:e90c3e268016942f35a7650124a716365d0ad484c47b391f816ad7dc0e47e11d@ec2-54-247-169-129.eu-west-1.compute.amazonaws.com:5432/d1uae99vpu7qar"

engine = create_engine(ENGINE_PATH_WIN_AUTH)