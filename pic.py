import pygame
import random

pygame.init()  # 初始化

white = [255, 255, 255]  # 白色的RGB值

X_max = 874  # 窗口宽度
Y_max = 585  # 窗口高度

dy_min = 3  # 下落速度：（3、4、5）像素/循环
dy_max = 6  # 数学区间为[3,6)，则整数为3,4,5
dx_min = -1  # 下落方向：-1为飘向左，0为竖直下降，1为飘向右
dx_max = 2  # 数学区间为[-1,2)，则整数为-1,0,1

Snow_num = 500  # 雪花的个数

size = [X_max, Y_max]  # 绘制窗口
screen = pygame.display.set_mode(size)
pygame.display.set_caption("下雪")

snow = []  # 给所有的雪花建立一个保存位置的数组
speed = []  # 对应的下落速度
bg = pygame.image.load('aaa.jpg')  # 加载背景图片

for i in range(Snow_num):  # 每个雪花循环一次
    x = random.randrange(0, X_max)
    y = random.randrange(0, Y_max)
    snow.append([x, y])  # 第一次在屏幕上随机出现的位置
    dy = random.randrange(dy_min, dy_max)
    dx = random.randrange(dx_min, dx_max)
    speed.append([dx, dy])  # 第一次出现时的下落速度

clock = pygame.time.Clock()  # 定义计时器

close = False  # 定义“点击关闭按钮”事件的状态
while close == False:  # 点击关闭按钮前一直循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True  # 如果点击关闭按钮，窗口会关闭，但python还在继续执行。这里可以跳出循环使python退出

    screen.blit(bg, (0, 0))  # 每循环一次，重新绘制一次背景图

    for i in range(len(snow)):  # 对每个已有的雪花执行一次
        pygame.draw.circle(screen, white, snow[i], speed[i][1] - 3)  # 在对应坐标上画上雪花点，下落速度dy越快个头越大，可产生立体前后层次感觉
        snow[i][0] += speed[i][0]  # 下落，x=x+dx
        snow[i][1] += speed[i][1]  # 下落，y=y+dy
        if snow[i][1] > Y_max:  # 如果超出窗口的范围
            y = random.randrange(-50, -10)  # y值在一定范围随机，避免雪花刚消失就立刻出现
            x = random.randrange(0, X_max)  # x值重新随机赋予
            snow[i] = [x, y]  # 将刚刚生成的坐标值赋予雪花，以便下一次循环显示在新的位置
            dy = random.randrange(dy_min, dy_max)
            dx = random.randrange(dx_min, dx_max)
            speed[i] = [dx, dy]  # 重新给个速度

    pygame.display.flip()  # 更新画面
    clock.tick(20)  # 延时
pygame.quit()