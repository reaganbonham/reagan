x = 7
y = 2
z = 1

print(x / y)
print(x // y)
print(x % y)
print(z % y)

def participation():
    import time
    time.sleep(3), print("I agree")
    time.sleep(3), print("Can you go back a slide?")
    time.sleep(3), print("I'm confused, can you repeat that?")
    time.sleep(3), print("That makes sense, thanks!")

print(participation())

public_transit = {"bart": [42, 35, 32, 32, 45, 68, 78],
                  "bus": [70, 61, 54, 52, 50, 71, 80],
                  "uber": [60, 40, 28, 36, 49, 82, 66]}

def fastest_time():
    for mode, times, in public_transit.items():
        mean_time = sum(times) / len(times)
        for min(mean_time) in times:
        