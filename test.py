from crypto.ZLib import compress

x = compress("x".encode())
with open("imgs/x.mig", "wb") as f:
    f.write(x)
    f.close()