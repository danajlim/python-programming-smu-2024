import math

G=6.673*(10**-11)

planets={
    "화성":{"M":6.42e23,"r":3396.2e3},
    "달":{"M":7.3e22,"r":1737.5e3},
    "토성":{"M":5.68e26,"r":60268e3}
}

for planet, data in planets.items():
    V=math.sqrt(2*G*data["M"]/data["r"])
    print("{planet}의 탈출 속도: {V:.2f}m/s")


##교수님 답
import math

massMars=6.42e23
radiusMars=3396.2*1000

massMoon=7.3e22
radiusMoon=1737.5e3

massSaturn=5.68e26
radiusSaturn=60268e3

G=6.673e-11
VMars=math.sqrt((2*G*massMars)/radiusMars)
VMoon=math.sqrt((2*G*massMoon)/radiusMoon)
VSaturn=math.sqrt((2*G*massSaturn)/radiusSaturn)

print("VMars=",VMars)
print("VMoon=",VMoon)
print("VSaturn=",VSaturn)