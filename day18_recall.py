def log(massage):
    f=open("log.txt","a")
    f.write(massage + "\n")
    f.close()
