from collections import deque

def paint_fill(image, pixel, fill_color):
    initial_color = image[pixel[0]][pixel[1]]
    q = deque()
    q.append(pixel)

    while q:
        x, y = q.popleft()

        if image[x][y] != initial_color:
            continue
        if image[x][y] == fill_color:
            continue

        image[x][y] = fill_color

        for i in range(-1, 2):
            for j in range(-1,2):
                new_x, new_y = x + i, y + j
                if 0 <= new_x and 0 <= new_y and new_x < len(image) and new_y < len(image[0]):
                    q.append((new_x, new_y))

    return image

def print_t(img):
    for r in img:
        print(r)

img = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,1,1,1,0],
    [1,1,1,0,0,0,0,0,1,0],
    [1,0,0,0,1,0,1,0,1,0],
    [1,0,0,0,1,0,1,0,1,0],
    [1,1,1,1,1,0,1,1,1,0],
    [0,0,0,0,0,0,1,0,0,0],
    [0,1,1,1,1,1,1,0,0,0],
]

print_t(img)
print('='*100)
new_img = paint_fill(img,(3,1),2)
print_t(new_img)