import cv2 as c

def draw_line(canvas, prev_points, curr_points, color=(0, 0, 255), thickness=8):
    if prev_points is None:
        return canvas

    c.line(canvas, prev_points, curr_points, color, thickness)
    return canvas

def clear_canvas(canvas):
    canvas[:] = 0
    return canvas

colors = {
    "blue": (255, 0, 0),
    "green": (0, 255, 0),
    "red": (0, 0, 255),
    "yellow": (0, 255, 255),
    "white": (255, 255, 255)
}

def draw_toolbar(frame):
    c.rectangle(frame, (0,0), (640,65), (50,50,50), -1)

    c.rectangle(frame,(40,10),(100,60),(255,0,0),-1)
    c.rectangle(frame,(120,10),(180,60),(0,255,0),-1)
    c.rectangle(frame,(200,10),(260,60),(0,0,255),-1)
    c.rectangle(frame,(280,10),(340,60),(0,255,255),-1)
    c.rectangle(frame,(360,10),(420,60),(255,255,255),-1)

def get_color(x, y):

    if y <= 65:

        if 40 < x < 100:
            return (255,0,0)

        elif 120 < x < 180:
            return (0,255,0)

        elif 200 < x < 260:
            return (0,0,255)

        elif 280 < x < 340:
            return (0,255,255)

        elif 360 < x < 420:
            return (255,255,255)

    return None