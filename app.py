from flask import Flask, request, jsonify, render_template, redirect, url_for
import qbittorrentapi
from decouple import config
from tpblite import TPB

app = Flask(__name__)


@app.route("/download", methods=['GET'])
def download():
    magnet = request.args.get("magnet")
    print("magnet")
    print(magnet)
    qbt = qbittorrentapi.Client(host='http://192.168.15.2', 
                                       port=8080, 
                                       username=config('QBIT_USER'), 
                                       password=config('QBIT_PASS'))
    try:
        qbt.auth_log_in()
    except qbittorrentapi.LoginFailed as e:
        print(e)
    
    qbt.torrents.add(magnet)
    return redirect(url_for('search'))


@app.route("/", methods=['GET'])
def search():
    return render_template('index.html')


@app.route("/torrents", methods=['GET'])
def torrents_result():
    search = request.args.get("q")
    t = TPB()
    torrents = t.search(search)
    for torrent in torrents:
        print(torrent.magnetlink)
    return render_template("torrents.html", torrents=torrents)


if __name__ == '__main__':
    app.run(host='0.0.0.0')