from datetime import datetime

def log_event(ip, attack_type, status):
    with open("security.log", "a") as log:
        log.write(f"{datetime.now()} | IP: {ip} | Attack: {attack_type} | Status: {status}\n")
