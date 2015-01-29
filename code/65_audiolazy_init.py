# __init__.py da AudioLazy
__modules__, __all__, __doc__ = \
  __import__(__name__ + "._internals", fromlist=[__name__]
            ).init_package(__path__, __name__, __doc__)
exec(("from .{} import *\n" * len(__modules__)).format(*__modules__))