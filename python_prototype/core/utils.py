from datetime import datetime, timedelta

def time_delta(date: datetime) -> str:
    delta = datetime.utcnow() - date
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    parts = []
    if days > 0: parts.append(f"{days}d")
    if hours > 0: parts.append(f"{hours}h")
    if minutes > 0: parts.append(f"{minutes}m")
    if seconds > 0: parts.append(f"{seconds}s")

    return " ".join(parts) if parts else "agora"

def capitalize(string: str) -> str:
    return string.capitalize()
