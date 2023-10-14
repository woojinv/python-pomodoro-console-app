from threading import Timer

prompt = "How long do you want this session to be?\n"

def get_minutes():
    start_timer(input(prompt))

def start_timer(minutes):
    try:
        t = Timer(float(minutes), get_minutes)
        t.start()
    except ValueError:
        start_timer(input("Not a number. " + prompt))
    
get_minutes()
