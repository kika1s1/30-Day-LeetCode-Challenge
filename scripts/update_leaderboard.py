import os
import re
import json
from datetime import datetime

# Paths
SOLUTIONS_DIR = "solutions"
PROGRESS_FILE = "progress.json"
LEADERBOARD_FILE = "LEADERBOARD.md"

# Load existing progress or initialize an empty structure
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r") as f:
        progress = json.load(f)
else:
    progress = {"participants": {}}

# Process each participant folder
for username in os.listdir(SOLUTIONS_DIR):
    user_dir = os.path.join(SOLUTIONS_DIR, username)
    if os.path.isdir(user_dir):  # Ensure it's a folder
        # Find all unique 'dayXX.py' files
        day_files = {
            re.match(r"day(\d{2})\.py", f).group(1)  # Extract day number (e.g., 01, 02)
            for f in os.listdir(user_dir)
            if re.match(r"day\d{2}\.py", f)
        }
        completed_days = len(day_files)  # Unique day count

        # Update progress
        progress["participants"][username] = {
            "completed_days": completed_days,
            "last_updated": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        }

# Save updated progress
with open(PROGRESS_FILE, "w") as f:
    json.dump(progress, f, indent=4)

# Generate leaderboard
sorted_participants = sorted(
    progress["participants"].items(),
    key=lambda x: -x[1]["completed_days"]
)

leaderboard = f"# Leaderboard 🏆\n\nUpdated on: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n\n"
leaderboard += "| Rank | Participant   | Completed Days | Last Updated         |\n"
leaderboard += "|------|---------------|----------------|----------------------|\n"

for rank, (username, details) in enumerate(sorted_participants, 1):
    leaderboard += f"| {rank}    | @{username}    | {details['completed_days']}             | {details['last_updated']} |\n"

# Write leaderboard to file
with open(LEADERBOARD_FILE, "w") as f:
    f.write(leaderboard)
