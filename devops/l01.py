import platform
from pprint import pprint

system = platform.system()

uname = platform.uname()

pprint(uname)

# print(system)

a1 = platform.machine()
a2 = platform.version()
pprint(a2)
pprint(a1)
