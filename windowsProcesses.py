import psutil
import wmi
import time

existing_processes = set(p.name() for p in psutil.process_iter())

def filter_by_name(process_name):
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                yield process
        except psutil.NoSuchProcess:
            pass


def is_running(process_name):
    return any(p for p in filter_by_name(process_name))

def get_current_processes():
    return set(p.name() for p in psutil.process_iter()) #get all active win processes

def monitor_processes(gameList):
    global existing_processes
    running_games = set()
    #existing_processes = get_current_processes()
    new_processes = set(p.name() for p in psutil.process_iter()) - existing_processes #this could be a list? is it better to jsut get set of all processes and see loop through to see if games are in loop?
    if new_processes:
        for game in gameList:
            if game in new_processes:
                print("--------")
                print(game)
                running_games.add(game)                           
    #app.update_process_name(latest_process_name)
    existing_processes = set(p.name() for p in psutil.process_iter())
    return running_games
    #timer.timeout.connect(check_processes) qt timer can do cool stuff
    #timer.start(2000)  # Check for new processes every 1 second

def check_cur_running_games(active_games):
    temp_active_games = active_games.copy()
    print("-------")
    print(existing_processes)
    print("-------")
    for x in active_games:
        if x not in existing_processes:
            print("THIS GAME JUST QUIT: " + x)
            temp_active_games.remove(x)
    return temp_active_games