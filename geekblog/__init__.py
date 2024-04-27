from flask import Flask, request, jsonify
from . import log, config
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "欢迎来到 GeekBlog！"

def start():
    log.info("正在启动 "+config.get_config_name(os.getcwd()))
    config.get_config(os.getcwd())
    server_port = config.get_config_port(os.getcwd())
    server_host = config.get_config_host(os.getcwd())
    log.info(f"🎉恭喜您！"+config.get_config_name()+"已在 http://localhost:{server_port} 上启动，请参阅官方文档以查看如何调用。")
    app.run(host=server_host, port=server_port, threaded=True)

if __name__ == '__main__':
    start()