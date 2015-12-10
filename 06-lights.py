# coding: utf-8

# common functions
def read_instr(text, get_act):
    import re
    pat = r"(turn on|toggle|turn off)\s(\d*\,\d*)\sthrough\s(\d*\,\d*)"
    match = re.match(pat, text)
    action, start, end = match.groups()
    action = get_act(action)
    start = [int(i) for i in start.split(',')]
    end = [int(i) for i in end.split(',')]
    return action, start, end

def count_on():
    on = 0
    for row in lights:
        on += sum(row)
    return on

def solve(part):
    if part==1:
        get_act = get_action1
        turn = turn1
    elif part==2:
        get_act = get_action2
        turn = turn2

    with open("instructions6.txt") as input:
        instructions = input.readlines()
        for inst in instructions:
            action, start, end = read_instr(inst, get_act)
            turn(action, start, end)

    on = count_on()
    print "There are: {} lights on".format(on)


# 1st part
def turn1(action, start, end):
    x_i, y_i = start
    x_f, y_f = end
    for x in range(x_i, x_f+1):
        for y in range(y_i, y_f+1):
            if isinstance(action,int):
                lights[x][y]=action
            elif action=="toggle":
                lights[x][y]=0 if lights[x][y]==1 else 1

def get_action1(action):
    if action=="turn on": return 1
    elif action=="turn off": return 0
    elif action=="toggle": return "toggle"
    else: print "Action {} not known!".format(action)

# 2nd part
def turn2(action, start, end):
    x_i, y_i = start
    x_f, y_f = end
    for x in range(x_i, x_f+1):
        for y in range(y_i, y_f+1):
            if isinstance(action,int):
                if (lights[x][y]==0 and action==-1): continue
                lights[x][y] += action

def get_action2(action):
    if action=="turn on": return 1
    elif action=="turn off": return -1
    elif action=="toggle": return 2
    else: print "Action {} not known!".format(action)


if __name__=="__main__":
    lights = [[0 for i in range(1000)] for j in range(1000)]
    print "Part 1:", solve(1)
    
    lights = [[0 for i in range(1000)] for j in range(1000)]
    print "Part 2:", solve(2)

# EOF