class MsgKeeper(object):
    def __init__(self, msg):
        self.msg = msg
    def show(self):
        print(self.msg)

# Definido fora do namespace da classe
def prefixed_keeper(self):

    class PrefixedKeeper(MsgKeeper):

        @property
        def msg(this):
            return self.msg + this._msg

        @msg.setter
        def msg(this, value):
            this._msg = value

    return PrefixedKeeper

turn = MsgKeeper("turn")

# Monkeypatch
MsgKeeper.prefixed_keeper = prefixed_keeper
# (poderia ser definido dentro da classe)

turno = turn.prefixed_keeper()("o")
turnon = turno.prefixed_keeper()("n")

turn.show()   # turn
turno.show()  # turno
turnon.show() # turnon
turn.msg = "Pyth"
turnon.show() # Python
