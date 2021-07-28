live = False

if live:
    try:
        from .prod import *
    except ImportError:
        from .base import *

else:
    from .local import *