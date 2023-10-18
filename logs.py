from flask import Flask
from src.logger import logging
# import logging
#from src.logger.logger import logging
#from src.logger.logs import logging
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    logging.info("We are testing our logging module")

    return "This is my Machine Learning Project"

if __name__ == '__main__':
    app.run(debug=True) # 5000 default