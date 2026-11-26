# CaprisV5
The small utilite module
## TextEngine "CaprisV8" ##
## made by people (DOESN'T AI)
## i'm waiting a bugs

## == Setting == ##
border = 5 # borderSizeX = border * 2, borderSizeY = border (square)
empty = " " # empty stroke
your_selfBorder = False ## your own border_size
borderX = 10
borderY = 5
##################

##===API===##
## a = entity(x, y, name, type) - create a moved entity
## a.move(x, y) - move entity on x and y to right or left or up or down (DOESN'T = HE +=)

## b = block(x, y, type) - add a new block (DOESN'T MOVE HIS)
## coll(target, target2) - return True or False if they touch
## walls = multi_block(x, y, text) - you can create more block, text can was biger wan 2 letters. He return [block, block]

## visible(text_before, [List], text_after) - show a entity/block in list to the screen
## b.al = False - Killing entity/block
## a.anim([list with sym anim], [list all obj], anim_time, before, after]) - anim time — time after before sym

## entity placeholders: a.x a.y a.pos[x/y] a.al (a_live?, True/False) a.data[x/y/type/name] a.type (sym)
## block placeholders: b.x b.y b.pos[x/y] b.type b.al (a_live?, True/False)
## wait(sec) - waiting
## rand_pos() - return random postion (x, y)

## set_wall_clip(function) - if entity move to wall then func activation, if function connect his imposs disconect lol:)

## menu([List], text) - he print question and variants (List) and user can write number. return answer text (exemple: "hello", 0) and what user write (number 1-len(List))

## x, y = rand_pos()
## a = entity(x, y, "a", "a") - exemple rand_pos()

## entity can't leave with ground (border)
## you can change border and empty in different time
## if type had 2 sym his change on "@"
## code have a random time, math and os
