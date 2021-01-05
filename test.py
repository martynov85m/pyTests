# a, b = 179, 37
# i = 0
#
# while a > 0:
#    a = a - b
#    if a > 0:
#        i += 1
# a = 179
# print("Целочисленное деление ",a," на ",b," дает ",i)

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# TODO здесь ваш код
# def bubbles(step):
#     point = sd.get_point(100, 100)
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2)


# bubbles(step=5)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# TODO здесь ваш код

# def bubbles(point, step, color):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2, color=color)
#
# point = sd.get_point(100, 100)
# bubbles(point=point, step=5, color=253)

# Нарисовать 10 пузырьков в ряд
# TODO здесь ваш код

# def bubbles(point, step, color):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2, color=color)
#
# for x in range(100,1001,100):
#     x += 50
#     point = sd.get_point(x, 100)
#     bubbles(point=point, step=5, color=253)

# Нарисовать три ряда по 10 пузырьков
# TODO здесь ваш код

# def bubbles(point, step, color):
#     radius = 50
#     for _ in range(3):
#         radius += step
#         sd.circle(center_position=point, radius=radius, width=2, color=color)
#
# for x in range(100,1001,100):
#     x += 50
#     for y in range(100, 301, 100):
#         point = sd.get_point(x, y)
#         bubbles(point=point, step=5, color=253)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
# TODO здесь ваш код

def bubbles(point, step, color):
    radius = 10
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)

for _ in range(100):
    point = sd.random_point()
    color = sd.random_color()
    bubbles(point=point, step=5, color=color)

sd.pause()
