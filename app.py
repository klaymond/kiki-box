from flask import Flask, request, jsonify, render_template
import qbittorrentapi
from decouple import config

app = Flask(__name__)


@app.route("/download", methods=['POST'])
def download():
    content = request.json
    qbt = qbittorrentapi.Client(host='http://192.168.15.2', 
                                       port=8080, 
                                       username=config('QBIT_USER'), 
                                       password=config('QBIT_PASS'))
    try:
        qbt.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)
    
    qbt.torrents.add(content['magnet_link'])


@app.route("/", methods=['GET'])
def search():
    return render_template('index.html')


@app.route("/torrents", methods=['GET'])
def torrents_result():
    return "Torrent results"


if __name__ == '__main__':
    app.run(host='0.0.0.0')