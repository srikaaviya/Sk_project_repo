import time

def start(is_running, ellapsedtime):

    if ellapsedtime == 0 and is_running == False:
        starttime = time.time()
        print("Timer Started ")
        is_running = True
    elif ellapsedtime == 0 and is_running == True:
        print("Timer Already Running")
        return None, is_running
        # print(starttime)
    else:
        starttime = ellapsedtime
        print(starttime)
    return starttime, is_running

def end_timer(starttime):
    endtime = time.time()
    laptime = starttime - endtime
    print(f"laptime:  {laptime}")

def pause_timer(starttime, is_running):
    print("Timer paused")
    current_time = time.time()
    # print(int(starttime))
    # print(int(current_time))
    ellapsedtime = starttime - current_time
    is_running = False
    print(f"Ellapsed time: {ellapsedtime}")
    return ellapsedtime, is_running

def main():
    starttime = 0
    is_running = False
    ellapsedtime = 0

    while True:
        print("1. Start the timer")
        print("2. Stop")
        print("3. Pause")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            starttime, is_running = start(is_running, ellapsedtime)
        elif choice == 2:
            end_timer(starttime)
        elif choice == 3:
            ellapsedtime, is_running = pause_timer(starttime, is_running)
        elif choice == 4:
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    main()