class SmartHome:
    def __init__(self):
        self.doors = {"front": False, "back": False}
        self.windows = {"living_room": False, "bedroom": False}
        self.lights = {"kitchen": False, "bedroom": False, "living_room": False}

    def open_door(self, door):
        if door in self.doors:
            self.doors[door] = True
            return f"{door.capitalize()} door opened."
        return "Door not found."

    def close_door(self, door):
        if door in self.doors:
            self.doors[door] = False
            return f"{door.capitalize()} door closed."
        return "Door not found."

    def open_window(self, window):
        if window in self.windows:
            self.windows[window] = True
            return f"{window.replace('_', ' ').capitalize()} window opened."
        return "Window not found."

    def close_window(self, window):
        if window in self.windows:
            self.windows[window] = False
            return f"{window.replace('_', ' ').capitalize()} window closed."
        return "Window not found."

    def turn_on_light(self, room):
        if room in self.lights:
            self.lights[room] = True
            return f"Light in {room} turned on."
        return "Room not found."

    def turn_off_light(self, room):
        if room in self.lights:
            self.lights[room] = False
            return f"Light in {room} turned off."
        return "Room not found."

    def status(self):
        return {
            "doors": self.doors,
            "windows": self.windows,
            "lights": self.lights
        }
