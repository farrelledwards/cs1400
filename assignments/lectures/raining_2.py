is_raining = True
have_umbrella = True


if not is_raining or (is_raining and have_umbrella):
    print("Walk to school.")
else:
    print("Take the bus.")
