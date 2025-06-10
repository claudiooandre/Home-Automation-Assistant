from house import SmartHome

home = SmartHome()

def handle_command(command):
    c = command.lower()

    if "open front door" in c:
        return home.open_door("front")
    elif "close front door" in c:
        return home.close_door("front")
    elif "open back door" in c:
        return home.open_door("back")
    elif "close back door" in c:
        return home.close_door("back")

    elif "open bedroom window" in c:
        return home.open_window("bedroom")
    elif "close bedroom window" in c:
        return home.close_window("bedroom")
    elif "open living room window" in c:
        return home.open_window("living_room")
    elif "close living room window" in c:
        return home.close_window("living_room")

    elif "turn on kitchen light" in c:
        return home.turn_on_light("kitchen")
    elif "turn off kitchen light" in c:
        return home.turn_off_light("kitchen")

    elif "turn on bedroom light" in c:
        return home.turn_on_light("bedroom")
    elif "turn off bedroom light" in c:
        return home.turn_off_light("bedroom")

    elif "status" in c or "house status" in c:
        status = home.status()
        return (
            f"Doors: {status['doors']}\n"
            f"Windows: {status['windows']}\n"
            f"Lights: {status['lights']}"
        )

    return "Sorry, I didn't understand that command."
