import json
import sys

data = json.load(sys.stdin)  # Read POST data from AJAX
with open("ip_info.json", "w") as file:
    json.dump(data, file)
print("IP info saved.")
