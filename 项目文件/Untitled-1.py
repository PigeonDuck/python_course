def bouncing_ball(h, bounce, window):
    times = 0
    if h < window or h<0 or window<0:    
        return -1
    # your code
    if h > window :        # 10 > 5
        times = times + 1    # 1
        h_ball = h * bounce  # h_ball = 6.6
        while True:
          if h_ball > window : # 6.6 > 5 
             h_ball = h_ball * bounce
             times = times + 2
          else:
            break
    return times

print(bouncing_ball(-1, 0.75, -1.5))