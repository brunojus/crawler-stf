import flask
from os import path
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from stf.spiders.processo import ProcessoSpider
import time
import subprocess
import MySQLdb
import MySQLdb.cursors


app = flask.Flask(__name__)

conn = MySQLdb.connect(user='root', passwd='121294', db='stf', host='127.0.0.1', charset="utf8", use_unicode=True)
cursor = conn.cursor()

@app.route('/', methods=['GET'])
def index():
    return flask.render_template('index.html')


@app.route('/flt/', methods=['GET'])
def get_doutrinas():
    processo = flask.request.args.get('filter')

    cursor.execute(
    """INSERT INTO 
        processos (
        numero_processo)
    VALUES (%s)""", ([processo]))
    conn.commit()

    return flask.redirect('/')
 
if __name__ == '__main__':
    app.run(debug=True)
