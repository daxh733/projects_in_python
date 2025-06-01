import random,sys,time

try:
    import bext
except ImportError:
    sys.exit()

width,height=bext.size()

width-=1

num_of_logos=5
pause_amount=0.2
colors=['red','green','yellow','blue','magenta','cyan','white']
UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)


COLOR='color'
X='x'
Y='y'
DIR='direction'

def main():
    bext.clear()

    #generate some logos
    logos=[]
    for i in range(num_of_logos):
        logos.append({
            COLOR:random.choice(colors),
            X:random.randint(1,width-4),
            Y:random.randint(1,height-4),
            DIR:random.choice(DIRECTIONS)
        })
        if logos[-1][X]%2==1:
            logos[-1][X]-=1

    cornerBounces=0
    while True:
        for logo in logos:
            bext.goto(logo[X],logo[Y])
            print('  ',end='')
            originalDirection=logo[DIR]

            if logo[X]==0 and logo[Y]==0:
                logo[DIR]=DOWN_RIGHT
                cornerBounces+=1
            elif logo[X]==0 and logo[Y]==height-1:
                logo[DIR]=UP_RIGHT
                cornerBounces+=1
            elif logo[X]==width-3 and logo[Y]==0:
                logo[DIR]=DOWN_LEFT
                cornerBounces+=1
            elif logo[X]==width-3 and logo[Y]==height-1:
                logo[DIR]=UP_LEFT
                cornerBounces+=1

            elif logo[X]==0 and logo[DIR]==UP_LEFT:
                logo[DIR]=UP_RIGHT
            elif logo[X]==0 and logo[DIR]==DOWN_LEFT:
                logo[DIR]=DOWN_RIGHT
            elif logo[X]==width-3 and logo[DIR]==UP_RIGHT:
                logo[DIR]=UP_LEFT
            elif logo[X]==width-3 and logo[DIR]==DOWN_RIGHT:
                logo[DIR]=DOWN_LEFT
            elif logo[Y]==0 and logo[DIR]==UP_RIGHT:
                logo[DIR]=DOWN_RIGHT
            elif logo[Y]==0 and logo[DIR]==UP_LEFT:
                logo[DIR]=DOWN_LEFT
            elif logo[Y]==height-1 and logo[DIR]==DOWN_RIGHT:
                logo[DIR]=UP_RIGHT
            elif logo[Y]==height-1 and logo[DIR]==DOWN_LEFT:
                logo[DIR]=UP_LEFT

            if logo[DIR]!=originalDirection:
                logo[COLOR]=random.choice(colors)
            

            if logo[DIR]==UP_RIGHT:
                logo[X]+=2
                logo[Y]-=1
            elif logo[DIR]==UP_LEFT:
                logo[X]-=2
                logo[Y]-=1
            elif logo[DIR]==DOWN_RIGHT:
                logo[X]+=2
                logo[Y]+=1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        bext.goto(5,0)
        bext.fg('white')

        for logo in logos:
            bext.goto(logo[X],logo[Y])
            bext .fg(logo[COLOR])
            print('DVD',end='')
        bext.goto(0,0)

        sys.stdout.flush()  # (Required for bext-using programs.)
        time.sleep(pause_amount)

# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()