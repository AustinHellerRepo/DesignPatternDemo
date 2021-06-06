from design_pattern.observer.implementation import RadioStation, Radio


# setup the radio stations (observables)
_west_radio_station = RadioStation(
	name="West Radio 107.1"
)
_east_radio_station = RadioStation(
	name="East Radio 95.5"
)

# setup the radios (observers)
_alice_radio = Radio(
	location="California"
)
_bob_radio = Radio(
	location="Texas"
)
_charles_radio = Radio(
	location="New York"
)

# connect the radios to the radio stations
_west_radio_station.add_observer(
	observer=_alice_radio
)
_west_radio_station.add_observer(
	observer=_bob_radio
)
_east_radio_station.add_observer(
	observer=_bob_radio
)
_east_radio_station.add_observer(
	observer=_charles_radio
)

# permit the user to perform actions based on chosen options
_is_active = True
while _is_active:
	print("Please make a choice from the options below")
	print("1: Change song on west station")
	print("2: Change song on east station")
	print("3: Exit")
	_user_input = input("Choice: ")
	if _user_input == "1":
		_song_name = input("Song name: ").strip()
		if _song_name != "":
			_west_radio_station.notify_observers(_song_name, _west_radio_station.get_name())
	elif _user_input == "2":
		_song_name = input("Song name: ").strip()
		if _song_name != "":
			_east_radio_station.notify_observers(_song_name, _east_radio_station.get_name())
	elif _user_input == "3":
		_is_active = False
	else:
		print(f"Unexpected user input: \"{_user_input}\".")
