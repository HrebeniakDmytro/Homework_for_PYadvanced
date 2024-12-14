import requests
from tabulate import tabulate

API_KEY = "45222ad4eb2237e145045138b66f8ebf"
BASE_URL = "https://v3.football.api-sports.io"
HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

def show_menu():
    print("\nВиберіть дію:")
    print("1. Подивитися поточні матчі")
    print("2. Подивитися розклад майбутніх матчів")
    print("3. Отримати інформацію про команду")
    print("4. Отримати інформацію про гравця")
    print("5. Вийти з програми")

def get_live_matches():
    try:
        url = f"{BASE_URL}/fixtures?live=all"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if data["response"]:
            matches = []
            for match in data["response"]:
                fixture = match["fixture"]
                league = match["league"]
                teams = match["teams"]
                goals = match["goals"]

                matches.append([
                    league["name"],
                    teams["home"]["name"],
                    goals["home"],
                    goals["away"],
                    teams["away"]["name"],
                    fixture["status"]["elapsed"]
                ])

            print("\nПоточні матчі:")
            print(tabulate(matches, headers=["Ліга", "Команда 1", "Голи 1", "Голи 2", "Команда 2", "Час"], tablefmt="grid"))
        else:
            print("\n[INFO] Наразі немає поточних матчів.")
    except requests.RequestException as e:
        print(f"\n[ERROR] Помилка отримання даних: {e}")

def get_upcoming_matches():
    try:
        url = f"{BASE_URL}/fixtures?next=10"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if data["response"]:
            matches = []
            for match in data["response"]:
                fixture = match["fixture"]
                league = match["league"]
                teams = match["teams"]

                matches.append([
                    fixture["date"].split("T")[0],
                    league["name"],
                    teams["home"]["name"],
                    teams["away"]["name"]
                ])

            print("\nРозклад майбутніх матчів:")
            print(tabulate(matches, headers=["Дата", "Ліга", "Команда 1", "Команда 2"], tablefmt="grid"))
        else:
            print("\n[INFO] Наразі немає запланованих матчів.")
    except requests.RequestException as e:
        print(f"\n[ERROR] Помилка отримання даних: {e}")


def get_team_players(team_id):
    try:
        url = f"{BASE_URL}/players/squads"
        params = {"team": team_id}  
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        data = response.json()

        if data["response"]:
            players = []
            for player_info in data["response"][0]["players"]:
                player_name = player_info.get("name")
                player_id = player_info.get("id")
                player_age = player_info.get("age")
                player_position = player_info.get("position") 
                
                if player_name and player_id and player_age and player_position:
                    players.append({
                        "name": player_name,
                        "id": player_id,
                        "age": player_age,
                        "position": player_position,
                    })
            return players
        else:
            print("[INFO] Гравці не знайдені для цієї команди.")
            return []
    except requests.RequestException as e:
        print(f"[ERROR] Помилка отримання гравців: {e}")
        return []

def get_team_info():
    team_name = input("\nВведіть назву команди: ")
    try:
        url = f"{BASE_URL}/teams?search={team_name}"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        if data["response"]:
            team = data["response"][0]["team"]
            venue = data["response"][0]["venue"]
            team_id = team["id"]  

            player_info = get_team_players(team_id)

            print("\nІнформація про команду:")
            print(f"Назва: {team['name']}")
            print(f"Країна: {team['country']}")
            print(f"Стадіон: {venue['name']}")
            print(f"Місто: {venue['city']}")
            print("\nГравці команди:")
            if player_info:
                for player in player_info[:5]:  
                    print(f"Ім'я: {player['name']}")
                    print(f"ID гравця: {player['id']}")
                    print(f"Вік: {player['age']}")
                    print(f"Позиція: {player['position']}")
                    print("-------------------------------")
            else:
                print("Гравці не знайдені.")
        else:
            print(f"\n[INFO] Команду '{team_name}' не знайдено.")
    except requests.RequestException as e:
        print(f"\n[ERROR] Помилка отримання даних: {e}")


def get_player_info():
    pass

def main():
    while True:
        show_menu()
        choice = input("\nВаш вибір: ")
        
        if choice == "1":
            get_live_matches()
        elif choice == "2":
            get_upcoming_matches()
        elif choice == "3":
            get_team_info()
        elif choice == "4":
            get_player_info()
        elif choice == "5":
            print("\nДякую за використання програми! До побачення!")
            break
        else:
            print("\n[ERROR] Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
