# A 500-meter-long snake (from Nokia 1100 game) is running at a speed of 72 km/hr. 
# If it passes through a tunnel in t seconds, then what is the length 
# (in meter, as integer value) of the tunnel. Consider 't' from user, 
# write a program to find the length of the tunnel.
t = float(input())
dist_travelled = (72*(5/18))*t
length = dist_travelled - 500
print(float(length))

