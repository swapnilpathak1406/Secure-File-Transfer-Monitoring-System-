from flask import Flask, request, jsonify
from rules import detect_attack
from rate_limiter import is_rate_limited
from logger import log_event

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inspect_request():
    ip = request.remote_addr
    payload = str(request.args) + str(request.form)

    # Rate limiting
    if is_rate_limited(ip):
        log_event(ip, "Rate Limit", "Blocked")
        return jsonify({"status": "blocked", "reason": "Rate limit exceeded"}), 429

    # Attack detection
    attack = detect_attack(payload)
    if attack:
        log_event(ip, attack, "Blocked")
        return jsonify({"status": "blocked", "attack": attack}), 403

    log_event(ip, "None", "Allowed")
    return jsonify({"status": "allowed", "message": "Request is safe"}), 200

if __name__ == "__main__":
    app.run(debug=True)
