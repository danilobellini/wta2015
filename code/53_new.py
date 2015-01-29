class MsgKeeper(object):
    def __new__(cls, msg):
        instance = super(MsgKeeper, cls).__new__(cls)
        instance.msg = msg
        return instance if msg != "Certa!" else -1

    @classmethod
    def alt_new(cls, msg):
        return cls(msg[::-1])

obj = MsgKeeper("Minha mensagem!")
print(obj)     # <__main__.MsgKeeper object at 0x...>
print(obj.msg) # Minha mensagem!

print(MsgKeeper("Certa!")) # -1

obj_alt = MsgKeeper.alt_new("Certa!")
print(obj_alt.msg) # !atreC
