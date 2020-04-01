import random
import math
import copy
from src.Point import Point


def gen_velocity(W):
    vx = random.randint(-1 * W, W)
    vy = random.randint(-1 * W, W)
    while vx == 0 or vy == 0:
        vx = random.randint(-1 * W, W)
        vy = random.randint(-1 * W, W)
    return vx, vy


def dist(b1, b2):
    return math.sqrt((b1.x-b2.x)**2 + (b1.y-b2.y)**2)


def dot(w1, w2):
    return w1[0]*w2[0] + w1[1]*w2[1]


def collision(b1, b2):
    q1 = Point(b1.x + b1.vx, b1.y + b1.vy)
    q2 = Point(b2.x + b2.vx, b2.y + b2.vy)
    return dointersect(b1, q1, b2, q2)


#https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
def dointersect(p1, p2, q1, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    elif o1 == 0 and onsegment(p1, p2, q1):
        return True
    elif o2 == 0 and onsegment(p1, q2, q1):
        return True
    elif o3 == 0 and onsegment(p2, p1, q2):
        return True
    elif o4 == 0 and onsegment(p2, q1, q2):
        return True
    else:
        return False


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2


def onsegment(p, q, r):
    if max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y):
        return True
    else:
        return False


def mag(w):
    return math.sqrt(w[0] ** 2 + w[1] ** 2)


def ball_collision_ods(b1, b2, r, acc):
    DIST = dist(b1, b2)
    w1 = [b1.x - b2.x, b1.y - b2.y]
    w2 = [b1.vx - b2.vx, b1.vy - b2.vy]
    b1c = copy.deepcopy(b1)
    b2c = copy.deepcopy(b2)
    roz_dist = abs(2*r-DIST)/2 + acc
    if mag(w1) == 0:
        w1short = [round(-x * roz_dist / b1.v) for x in [b1.vx, b1.vy]]
        w2short = [round(-x * roz_dist / b2.v) for x in [b2.vx, b2.vy]]
        b1.x += w1short[0]
        b1.y += w1short[1]
        b2.x += w2short[0]
        b2.y += w2short[1]
        c = dot(w1, w2) / dist(b1, b2)**2
    else:
        w1short = [round(x*roz_dist/mag(w1)) for x in w1]
        mw1short = [round(-x) for x in w1short]
        b1.x += w1short[0]
        b1.y += w1short[1]
        b2.x += mw1short[0]
        b2.y += mw1short[1]
        c = dot(w1, w2) / dist(b1, b2)**2
    dvx = (c * (b2c.x - b1c.x))
    dvy = (c * (b2c.y - b1c.y))
    # --
    b1.vx += dvx
    b1.vy += dvy
    b2.vx -= dvx
    b2.vy -= dvy

    return b1, b2


def ball_collision(b1, b2):
    if dist(b1, b2) == 0:
        return b1.vx, b1.vy, b2.vx, b2.vy
    w1 = [b1.x - b2.x, b1.y - b2.y]
    w2 = [b1.vx - b2.vx, b1.vy - b2.vy]
    c = dot(w1, w2) / dist(b1, b2) ** 2
    dvx = c * (b2.x - b1.x)
    dvy = c * (b2.y - b1.y)
    dvx = round(dvx)
    dvy = round(dvy)
    return b1.vx + dvx, b1.vy + dvy, b2.vx - dvx, b2.vy - dvy


def wall_collision(ball, R):
    b = copy.deepcopy(ball)
    #b.update()
    if b.y + b.vy < 0 or b.y + b.vy > 2*R:#górna i dolna
        return b.vx, -1*b.vy
    elif b.x + b.vx < 0 or b.x + b.vx > 2*R:#lewa i prawa
        return -1*b.vx, b.vy
    else:
        return b.vx, b.vy