import matplotlib.pyplot as plt

def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distance in meters')
    plt.ylabel('Gravitational force in Newtons')
    plt.title('mrs-davis and Jamie\'s gravitational force/distance')
    plt.show()

def generate_F_r():
    r = range(100, 1610, 100)
    F = []

    G = 6.674*(10**-11)
    m1 = 86.18
    m2 = 58.96

    for dist in r:
        force = G*(m1*m2)/(dist**2)
        F.append(force)

    draw_graph(r, F)

if __name__=='__main__':
    generate_F_r()
    
