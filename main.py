import os

os.umask(0o022)

LINE = "The office microwave just died. Turns out three minutes is an eternity when you're reheating yesterday's ambition."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
os.chmod("/output/entry.txt", 0o644)