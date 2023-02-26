from copy import copy

from PIL import Image
import pytesseract

pytesseract.tesseract_cmd = r'Tesseract-Main/tesseract.exe'

# img = Image.open("test.png").convert('L')


def read(read_img: Image):
    boxes = pytesseract.image_to_boxes(read_img, lang='guj')
    return boxes


def extract_positions(text: str):
    arr = text.split()
    positions = []
    for i in range(0, len(arr), 6):
        x1 = int(arr[i + 1])
        y1 = int(arr[i + 2])
        x2 = int(arr[i + 3])
        y2 = int(arr[i + 4])
        half_x = int((x1 + x2) / 2)
        half_y = int((y1 + y2) / 2)
        half_width = int(abs((x2 - x1) / 2))
        half_height = int(abs((y2 - y1) / 2))
        positions.append([x1, y1, x2, y2, half_x, half_y, half_width, half_height])
    return positions


# print(extract_positions(read(img)))


def sort_lines(arr: list):
    local = copy(arr)
    n = len(local)

    ret_arr = []

    for i in range(n):
        for j in range(0, n - i - 1):
            if local[j][5] > local[j + 1][5]:
                local[j], local[j + 1] = local[j + 1], local[j]

    old = 0
    for k in range(n):
        if not (local[old][5] - (local[old][7] / 4) <= local[k][5] <= local[old][5] + (
                local[old][7] / 4)):
            ret_arr.append(local[old:k])
            old = k

    return ret_arr


def sort_positions_in_line(arr: list):
    local = copy(arr)
    n = len(local)

    for k in range(len(arr)):
        for i in range(len(arr[k])):
            for j in range(0, len(arr[k]) - i - 1):
                if local[k][j][4] > local[k][j + 1][4]:
                    local[k][j], local[k][j + 1] = local[k][j + 1], local[k][j]

    return local

# print(sort_positions_in_line(sort_lines(extract_positions(read(img)))))
