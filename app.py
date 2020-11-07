from flask import Flask, request, jsonify
import qbittorrentapi
from decouple import config

app = Flask(__name__)


@app.route("/download", methods=['POST'])
def download():
    content = request.json
    qbt_client = qbittorrentapi.Client(host='http://192.168.15.2', 
                                       port=8080, 
                                       username=config('QBIT_USER'), 
                                       password=config('QBIT_PASS'))
    try:
        qbt_client.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)
    
    qbt_client.torrents.add(content['magnet_link'])


if __name__ == '__main__':
    app.run(host='0.0.0.0')