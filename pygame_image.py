import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.transform.flip(bg_img,True,False) #練習8：bg_imgを反転
    kk_img = pg.image.load("fig/3.png") # 練習３：こうかとん入れる
    kk_img = pg.transform.flip(kk_img,True,False) #練習3：左右反転
    tmr = 0

    kk_rct = kk_img.get_rect() #練習10-1
    kk_rct.center = 300,200
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
    
        key_lst = pg.key.get_pressed() #練習10-3：押されたすべてのキーの取得
        x1=-1
        y1=0
        if key_lst[pg.K_UP]: #上矢印キーが押された
            y1=-1
        if key_lst[pg.K_DOWN]: #下矢印キーが押された
            y1=1
        if key_lst[pg.K_RIGHT]: #右矢印キーが押された
            x1=1
        if key_lst[pg.K_LEFT]: #左矢印キーが押された
            x1=-1
        kk_rct.move_ip((x1,y1))


        x = tmr % 3200 #練習5 & 練習9
        screen.blit(bg_img, [-x, 0])#練習５
        screen.blit(bg2_img,[-x+1600,0]) #練習7：連続させる
        screen.blit(bg_img,[-x+3200,0]) #練習9
        screen.blit(kk_img, kk_rct) #練習４ ＆　練習10


        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6




if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()