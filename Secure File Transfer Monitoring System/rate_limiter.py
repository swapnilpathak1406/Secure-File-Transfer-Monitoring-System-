import time

REQUEST_LIMIT = 5   # max requests
TIME_WINDOW = 10    # seconds

ip_tracker = {}

def is_rate_limited(ip):
    current_time = time.time()

    if ip not in ip_tracker:
        ip_tracker[ip] = []

    ip_tracker[ip] = [t for t in ip_tracker[ip] if current_time - t < TIME_WINDOW]
    ip_tracker[ip].append(current_time)

    return len(ip_tracker[ip]) > REQUEST_LIMIT
