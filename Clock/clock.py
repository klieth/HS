while True: #we're going to look for times infinitely--I'll quit later.
    time = input() # Get the time from stdin
    if time == "0:00": # Quit condition
        break
    time = time.split(":") # split on the :, result ["HH","MM"]
    dm = int(time[1]) * 6 
    dh = int(time[0]) * 30 + int(time[1])/2.0

    # Check out the format strings to see how to add 3 decimal places
    if dm > dh:
        out = dm - dh
        if out > 180:
            out = 360-out
        print("{:.3f}".format(out))
    else:
        out = dh - dm
        if out > 180:
            out = 360-out
        print("{:.3f}".format(out))
