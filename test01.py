#coding:utf-8
# 闭包的使用

def set_passline(passline):
    def cmp(val):
        if val>=passline:
            print "pass"
        else:
            print "failed"
    return cmp

f_100=set_passline(60)
f_100(89)

f_150=set_passline(90)
f_150(89)