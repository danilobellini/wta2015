# Adaptado da AudioLazy, audiolazy/test/__init__.py
from importlib import import_module, sys
import types, pytest
from _pytest.skipping import XFailed

class XFailerModule(types.ModuleType):
    def __init__(self, name):
        try:
            if isinstance(import_module(name.split(".", 1)[0]),
                          XFailerModule):
                raise ImportError
            import_module(name)
        except (ImportError, XFailed):
            sys.modules[name] = self
            self.__name__ = name

    __file__ = __path__ = __loader__ = ""

    def __getattr__(self, name):
        def xfailer(*args, **kwargs):
            pytest.xfail(reason="Module {} not found"
                                .format(self.__name__))
        return xfailer
