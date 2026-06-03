from skyfield.api import load
import hashlib
ts = load.timescale()
t = ts.now()
planets = load('de421.bsp')
earth = planets['earth']
def getdistance(planet:str):
    s = planets[planet].at(t).observe(earth)
    dis = s.distance().au
    dis *= 1_000_000
    return int(hashlib.sha256(str(dis).encode()).hexdigest(),16)
def randint(min,max):
    distance = getdistance('earth')
    entropy = (
    int(distance * 1e6) ^
    int(getdistance('moon') * 1e6) ^
    int(getdistance('sun') * 1e6) ^
    int(getdistance('mars') * 1e6) ^
    int(getdistance('venus') * 1e6) ^
    int(getdistance('mercury') * 1e6) ^
    int(getdistance('pluto barycenter') * 1e6)
)
    return (entropy % (max - min + 1)) + min

print(randint(1,10))
