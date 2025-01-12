resistance1 = 36
resistance2 = 23

voltage1 = 20
voltage2 = 10

current1 = voltage1 / resistance1
current2 = voltage2 / resistance2

lower_current = min(current1, current2)

print("Участок с меньшим током:", lower_current)
