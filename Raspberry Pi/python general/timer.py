import time

def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.perf_counter()
procedure()
print (time.perf_counter()-t0)

