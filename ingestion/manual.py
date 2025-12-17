from datetime import datetime
from storage.signals import write_signal

def save_manual_signal(service, signal_type, name, value, timestamp):
    signal = {
        "timestamp": datetime.combine(timestamp, datetime.min.time()),
        "service": service,
        "signal_type": signal_type,
        "name": name,
        "value": value,
        "tags": {},
        "source": "manual"
    }
    write_signal(signal)
