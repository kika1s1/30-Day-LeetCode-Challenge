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
            match.group(1).zfill(2)  # Extract day number and ensure 2-digit format (e.g., '01')
            for f in os.listdir(user_dir)
            if (match := re.match(r"day_?(\d+)\.py", f))  # Match "day01.py", "day_01.py", or "day011.py"
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

# Badge Mapping
BADGES = {1: "🏅 Gold", 2: "🥈 Silver", 3: "🥉 Bronze"}

# Generate leaderboard with badges
sorted_participants = sorted(
    progress["participants"].items(),
    key=lambda x: -x[1]["completed_days"]
)

leaderboard = f"# Leaderboard 🏆\n\nUpdated on: {datetime.now().strftime('%Y-%m-%d %I:%M %p')}\n\n"
leaderboard += "| Rank | Participant       | Completed Days | Badge      | Last Updated         |\n"
leaderboard += "|------|-------------------|----------------|------------|----------------------|\n"

for rank, (username, details) in enumerate(sorted_participants, 1):
    badge = BADGES.get(rank, "")  # Assign badge for top 3 or leave blank
    leaderboard += f"| {rank:<4} | @{username:<16} | {details['completed_days']:<14} | {badge:<10} | {details['last_updated']} |\n"

# Write leaderboard to file
with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
    f.write(leaderboard)
