import time

click("1463535593042.png")
click("1463535665977.png")
dragDrop("1463535726227.png", "1463535759063.png")

ISOTIMEFORMAT="%m-%d"
myTime=time.strftime( ISOTIMEFORMAT, time.localtime() )
print myTime

doubleClick("1463536447521.png")
type(myTime)
type("s",KEY_CTRL)







