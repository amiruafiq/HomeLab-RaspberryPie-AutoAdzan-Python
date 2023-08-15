import requests
from crontab import CronTab

# API endpoint and your API key
api_endpoint = "https://api.example.com/prayer_times"
api_key = "your_api_key"

# Make HTTP request to the API
response = requests.get(api_endpoint, params={"api_key": api_key})

if response.status_code == 200:
    # Parse the response and extract the prayer times
    prayer_times = response.json()["data"]["prayer_times"]

    # Update the crontab file with the new prayer times
    cron = CronTab(user=True)
    cron.remove_all()  # Remove existing Adzan playback schedule

    # Add new schedule for each prayer time
    for prayer, time in prayer_times.items():
        # Convert prayer time to cron format (e.g., "13:30" -> "30 13 * * *")
        hour, minute = time.split(":")
        cron_time = f"{minute} {hour} * * *"
        
        # Create a new cron job for the prayer time
        job = cron.new(command=f"play_adzan.py --prayer {prayer}")
        job.setall(cron_time)
        job.enable()

    # Write changes to the crontab file
    cron.write()
    print("Adzan playback schedule updated successfully.")
else:
    print("Failed to fetch prayer time data from the API.")