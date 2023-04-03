import os
import sys

env = os.environ.items()

if len(sys.argv) > 1:
    filter_params = sys.argv[1:]
    env = [param for param in env if any(f_p in param[0] for f_p in filter_params)]

for name, value in sorted(env):
    print(name, value)
