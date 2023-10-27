
f=10
z=20
def setup():
     size (1000 ,1000)
def draw():
     global f ,z ,t ,s ,p ,q ,r ,u
     background (200 ,100 ,200)
     translate (f,z)
     rect (f ,f ,30 ,30)
     f=f+0.3
     z=z+0.1
     r=random(255)
     u=random(255)
     t=random(255)
     s=random(1000)
     p=random(1000)
     q=50
     stroke (t ,r ,u)
     strokeWeight (q)
     point (p ,s)
