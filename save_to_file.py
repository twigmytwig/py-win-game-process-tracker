from datetime import datetime, timedelta
import json

def get_game_time_seconds(game_time : datetime):
    return timedelta(hours=game_time.hour, minutes=game_time.minute, seconds=game_time.second).total_seconds()

def save_to_file(closed_game_data, closed_game_name,filename):
    seconds_only_format : str = "%S.%f"
    format : str = "%H:%M:%S.%f"
    file = open(filename)
    game_time_data = json.load(file)
    print('Game time data variable: ---' + str(game_time_data))
    if game_time_data:
        for x in game_time_data:
            print("Gametime data["+str(x)+"] -- "+ str(game_time_data[x]["total_game_time_seconds"]))
            if x == closed_game_name:
                previous_game_time = datetime.strptime(closed_game_data[closed_game_name],format)
                temp_game_time= float(game_time_data[x]["total_game_time_seconds"])
                print("secconds: " + str(temp_game_time))
                print("temp_game time variable : " + str(temp_game_time))
                total_time_seconds = temp_game_time\
                                     + float(get_game_time_seconds(previous_game_time))
                print("Total time variable : " + str(total_time_seconds))
                game_time_data[x]["total_game_time_seconds"] = total_time_seconds
                with open(filename, 'w') as data_file:
                    json.dump(game_time_data, data_file, indent=2)

    else:
        print("in else")
        with open(filename, 'w') as data_file:
            json.dump(closed_game_data, data_file)