class MsgKeeper(object):
    def __init__(self, msg):
        self.msg = msg
    def show(self):
        print(self.msg)

foo = MsgKeeper("foo")
bar = MsgKeeper("bar")

foo.show()
bar.show()
MsgKeeper.show(foo)
MsgKeeper.show(bar)
