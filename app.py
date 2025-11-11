import platform
import psutil
import os
import json
from flask import Flask
from flask import jsonify



nomeIntegrante = "Eros Felipe de Quevedo dos Santos"

# Obtém versão do S.O. subj
print(platform.platform())

# Obtém PID
print(os.getpid())

# Obtém uso de CPU (%)
print(psutil.cpu_percent())

# Obtém uso de memória (MB)
print(psutil.virtual_memory().used // 1024 **2)

metricas ={
    'pid': os.getpid(),
    'memoria_mb': psutil.virtual_memory().used // 1024 ** 2,
    'uso_cpu': psutil.cpu_percent(),
    'so': platform.platform()
}

# transformando em texto para json
print(json.dumps(metricas, ensure_ascii=False))

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Página inicial!'

@app.route('/info')
def info():
    return nomeIntegrante

@app.route('/metricas')
def metricas():
    return json.dumps(metricas, ensure_ascii=False)

if __name__ == '__main__':
    app.run(debug=True)
