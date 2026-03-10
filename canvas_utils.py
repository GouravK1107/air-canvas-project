import cv2 as c

def draw_line(canvas, prev_points, curr_points, color=(0, 0, 255), thickness=8):
    if prev_points is None:
        return canvas

    c.line(canvas, prev_points, curr_points, color, thickness)
    return canvas

def clear_canvas(canvas):
    canvas[:] = 0
    return canvas
