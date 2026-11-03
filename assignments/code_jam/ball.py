ball_x = 200
ball_y = 100
ball_x_velocity = 5
ball_y_velocity = 5

left_paddle_y = 0
right_paddle_y = 0
paddle_velocity = 5
paddle_height = 200

# each loop is one frame
while True:

    # BALL
    ball_x += ball_x_velocity
    ball_y += ball_y_velocity

    # left wall, only bounce if its inside the left paddle
    if x < 0:
        if (ball_y > left_paddle_y) and (ball_y < left_paddle_y + paddle_height):
            ball_x_velocity = abs(ball_x_velocity)
        else:
            out_of_bounds()
    
    if y < 0:
        ball_y_velocity = abs(ball_y_velocity)
    
    # right wall, only bounce if its inside the right paddle
    if x > width:
        if (ball_y > right_paddle_y) and (ball_y < right_paddle_y + paddle_height):
            ball_x_velocity = -abs(ball_x_velocity)
        else:
            out_of_bounds()
    
    if y > height:
        ball_y_velocity = -abs(ball_y_velocity)

    # PADDLES
    if key_pressed('w'):
        left_paddle_y -= paddle_velocity
    if key_pressed('S'):
        left_paddle_y += paddle_velocity
    if key_pressed('O'):
        right_paddle_y -= paddle_velocity
    if key_pressed('L'):
        right_paddle_y += paddle_velocity

    if left_paddle_y < 0:
        left_paddle_y = 0
    if left_paddle_y > (height - paddle_height):
        left_paddle_y = (height - paddle_height)
    if right_paddle_y < 0:
        right_paddle_y = 0
    if right_paddle_y > (height - paddle_height):
        right_paddle_y = (height - paddle_height)