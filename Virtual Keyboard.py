import pygame
pygame.init()

display_width = 500
display_height = 400

win = pygame.display.set_mode((display_width, display_height))

font = pygame.font.SysFont('freesansbold.ttf', 25)

class Letter(object):
    def __init__(self, x, y, value, shape):
        self.x = x
        self.y = y
        self.value = value
        self.shape = shape
        self.radius = display_width//30

    def draw(self):
        text = font.render(self.value, True, (255, 0, 0))
        if self.shape == "c": #i.e. If the shape is a circle
            pygame.draw.circle(win, (255, 255, 0), (self.x, self.y), self.radius)
            textLocation = ((((self.x) - (text.get_width()/2)), ((self.y) - (text.get_width()/2))))
        elif self.shape == "r":
            pygame.draw.rect(win, (255, 255, 0), (self.x, self.y, 60, 40))
            textLocation = ((((self.x + 60/2) - (text.get_width()/2)), ((self.y + 40/2) - (text.get_height()/2))))
        win.blit(text, textLocation)
        

def redrawGameWindow():
    win.fill((0, 0, 0))
    
    q.draw()
    w.draw()
    e.draw()
    r.draw()
    t.draw()
    y.draw()
    u.draw()
    i.draw()
    o.draw()
    p.draw()

    a.draw()
    s.draw()
    d.draw()
    f.draw()
    g.draw()
    h.draw()
    j.draw()
    k.draw()
    l.draw()

    z.draw()
    x.draw()
    c.draw()
    v.draw()
    b.draw()
    n.draw()
    m.draw()

    caps.draw()
    delete.draw()
    space.draw()

    text = font.render(shownText, True, (255, 0, 0))
    win.blit(text, (30, 300))

    pygame.display.update()

run = True
shiftValue = 0
shownText = ""

while run == True:

    if shiftValue % 2 == 0:
        q = Letter((display_width//11), 20, "q", "c")
        w = Letter((display_width//11 * 2), 20, "w", "c")
        e = Letter((display_width//11 * 3), 20, "e", "c")
        r = Letter((display_width//11 * 4), 20, "r", "c")
        t = Letter((display_width//11 * 5), 20, "t", "c")
        y = Letter((display_width//11 * 6), 20, "y", "c")
        u = Letter((display_width//11 * 7), 20, "u", "c")
        i = Letter((display_width//11 * 8), 20, "i", "c")
        o = Letter((display_width//11 * 9), 20, "o", "c")
        p = Letter((display_width//11 * 10), 20, "p", "c")

        a = Letter((display_width//10), 50, "a", "c")
        s = Letter((display_width//10 * 2), 50, "s", "c")
        d = Letter((display_width//10 * 3), 50, "d", "c")
        f = Letter((display_width//10 * 4), 50, "f", "c")
        g = Letter((display_width//10 * 5), 50, "g", "c")
        h = Letter((display_width//10 * 6), 50, "h", "c")
        j = Letter((display_width//10 * 7), 50, "j", "c")
        k = Letter((display_width//10 * 8), 50, "k", "c")
        l = Letter((display_width//10 * 9), 50, "l", "c")

        z = Letter((display_width//8), 80, "z", "c")
        x = Letter((display_width//8 * 2), 80, "x", "c")
        c = Letter((display_width//8 * 3), 80, "c", "c")
        v = Letter((display_width//8 * 4), 80, "v", "c")
        b = Letter((display_width//8 * 5), 80, "b", "c")
        n = Letter((display_width//8 * 6), 80, "n", "c")
        m = Letter((display_width//8 * 7), 80, "m", "c")

    else:
        q = Letter((display_width//11), 20, "Q", "c")
        w = Letter((display_width//11 * 2), 20, "W", "c")
        e = Letter((display_width//11 * 3), 20, "E", "c")
        r = Letter((display_width//11 * 4), 20, "R", "c")
        t = Letter((display_width//11 * 5), 20, "T", "c")
        y = Letter((display_width//11 * 6), 20, "Y", "c")
        u = Letter((display_width//11 * 7), 20, "U", "c")
        i = Letter((display_width//11 * 8), 20, "I", "c")
        o = Letter((display_width//11 * 9), 20, "O", "c")
        p = Letter((display_width//11 * 10), 20, "P", "c")

        a = Letter((display_width//10), 50, "A", "c")
        s = Letter((display_width//10 * 2), 50, "S", "c")
        d = Letter((display_width//10 * 3), 50, "D", "c")
        f = Letter((display_width//10 * 4), 50, "F", "c")
        g = Letter((display_width//10 * 5), 50, "G", "c")
        h = Letter((display_width//10 * 6), 50, "H", "c")
        j = Letter((display_width//10 * 7), 50, "J", "c")
        k = Letter((display_width//10 * 8), 50, "K", "c")
        l = Letter((display_width//10 * 9), 50, "L", "c")

        z = Letter((display_width//8), 80, "Z", "c")
        x = Letter((display_width//8 * 2), 80, "X", "c")
        c = Letter((display_width//8 * 3), 80, "C", "c")
        v = Letter((display_width//8 * 4), 80, "V", "c")
        b = Letter((display_width//8 * 5), 80, "B", "c")
        n = Letter((display_width//8 * 6), 80, "N", "c")
        m = Letter((display_width//8 * 7), 80, "M", "c")

    caps = Letter((display_width//4), 110, "Caps", "r")
    delete = Letter((display_width//4 * 2), 110, "Delete", "r")
    space = Letter((display_width//4 * 3), 110, "Space", "r")

    lettersList = [q, w, e, r, t, y, u, i, o, p, a, s, d, f, g, h, j, k, l, z, x, c, v, b, n, m, caps, delete, space]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for L in lettersList:
                if L.shape == "c":
                    if pos[0] > L.x - L.radius and pos[0] < L.x + L.radius:
                        if pos[1] > L.y - L.radius and pos[1] < L.y + L.radius:
                            shownText = shownText + str(L.value)
                            #print(shownText)
                else:
                    if pos[0] > L.x and pos[0] < L.x + 60:
                        if pos[1] > L.y and pos[1] < L.y + 40:
                            if L.value == "Delete":
                                try:
                                    shownText = shownText[:-1]
                                except:
                                    pass
                            elif L.value == "Caps":
                                shiftValue = shiftValue + 1
                            elif L.value == "Space":
                                shownText = str(shownText) + " "
                            else:
                                shownText = shownText + str(L.value)
                  
    redrawGameWindow()

    

pygame.quit()    
