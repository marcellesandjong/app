import requests

def get_team_schedule(team_name):
    # Replace spaces with dashes and convert to lowercase for the API
    team_name_formatted = team_name.replace(' ', '-').lower()
    # URL to fetch NFL team schedules (use a placeholder or mock URL for now)
    url = f'http://api.sportsdata.io/v3/nfl/scores/json/Schedules/{team_name_formatted}?key=YOUR_API_KEY'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
