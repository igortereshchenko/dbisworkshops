from sqlalchemy.engine import create_engine

ENGINE_PATH_WIN_AUTH = "postgres://amsurmxifnypqr:4cc7d28e000594fe2351c7f7d04df59ef3cea9347b9028b33e8d262035b12b5a@ec2-54-247-79-178.eu-west-1.compute.amazonaws.com:5432/d4708p9ktk4c5u"

engine = create_engine(ENGINE_PATH_WIN_AUTH)