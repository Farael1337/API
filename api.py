from flask import Flask, jsonify
import os

app = Flask(__name__)

# Список твоих ботов
BOTS = [
    {"id": "roulette", "name": "🎰 Бот-рулетка", "status": "online"},
    {"id": "shop", "name": "🛒 Бот-магазин", "status": "online"},
]

@app.route('/api/bots')
def get_bots():
    return jsonify(BOTS)

@app.route('/api/bot/<bot_id>/restart', methods=['POST'])
def restart_bot(bot_id):
    # Команда для перезагрузки бота
    os.system(f"systemctl restart discord-{bot_id}")
    return jsonify({"status": "restarting"})

@app.route('/api/bot/<bot_id>/stats')
def get_stats(bot_id):
    return jsonify({
        "servers": 47,
        "users": 1284,
        "uptime": "7д 12ч"
    })

if __name__ == '__main__':
    print("✅ Сервер запущен: http://localhost:5000")
    print("📱 Открой в браузере файл index.html")
    app.run(host='0.0.0.0', port=5000, debug=True)