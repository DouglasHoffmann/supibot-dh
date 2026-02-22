from .query import query as Query
from .cache import cache as Cache
from .got import got as Got
from .utils import time_delta, capitalize

class Core:
    Query = Query
    Cache = Cache
    Got = Got
    Utils = type('Utils', (), {'time_delta': staticmethod(time_delta), 'capitalize': staticmethod(capitalize)})

core = Core()
