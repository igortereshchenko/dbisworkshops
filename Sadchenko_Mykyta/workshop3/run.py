import os
from source import app

myapp = app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    myapp.run(port=port)
