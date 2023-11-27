def bouncing_ball(h, bounce, window):
    times = 0
    if h <= window :    
        return -1
    if bounce <= 0 or bounce>=1:
        return -1
    if h<=0 :
        return -1
    # your code
    if h > window and bounce<1 and bounce>0 and h>0 and window>0:        # 10 > 5
        times = times + 1    # 1
        h_ball = h * bounce  # h_ball = 6.6
        while True:
          if h_ball > window : # 6.6 > 5 
             h_ball = h_ball * bounce
             times = times + 2
          else:
            break
    return times
    