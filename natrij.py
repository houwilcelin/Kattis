dh, dm, ds = tuple(map(int, input().split(':')))
fh, fm, fs = tuple(map(int, input().split(':')))
dseconds = ds + dm * 60 + dh * 60 * 60
fseconds = fs + fm * 60 + fh * 60 * 60
dif = fseconds - dseconds if (fseconds > dseconds) \
    else (24 * 3600 - dseconds) + fseconds
oh = dif // 3600
dif -= (oh * 3600)
om = dif // 60
dif -= om * 60
print("{:0>2}:{:0>2}:{:0>2}".format(oh, om, dif))