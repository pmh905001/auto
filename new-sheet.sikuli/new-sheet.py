import time
############################################################################
#
#This script help me to create new sheet, named as %month-%day formated
#
#############################################################################

#Make excel UI on top
if not exists("1463581342128.png"):
    click("1463535593042.png")

click("1463584301588.png")
click("1463535665977.png")
dragDrop("1463535726227.png", "1463535759063.png")

ISOTIMEFORMAT="%m-%d"
myDate=time.strftime( ISOTIMEFORMAT, time.localtime() )
print myDate

doubleClick("1463536447521.png")
type(myDate)
click("1463582110026.png")
type("s",KEY_CTRL)







