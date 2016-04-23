type(Key.F12)
type("c",KEY_CTRL)
dragDrop("1460803450757.png","1460803478404.png")
wait(2)
click("1460800840302.png")

doubleClick("1460803765447.png")
click("1460800434160.png")
while exists("1460804127255.png"):
    click("1460820126478.png")
    wait(20) 
    click("1460800434160.png")
click("1460821266339.png")
reg=Screen(0).selectRegion() 
reg.doubleClick("1460821557339.png")
type("v",KEY_CTRL)
type("s",KEY_CTRL)
rightClick(reg)
click("1461377578962.png")

find("1461377730219.png").left().click("1461377805782.png")
click("1461377831217.png")
doubleClick("1461377876946.png")
find("1461392575110.png").right().click("1461392630251.png")
type("\\")
type("v",KEY_CTRL)
click("1461392239069.png")
            


#paste("aaa")








