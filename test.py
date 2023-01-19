from dist_meta.distributions import WheelDistribution
from glob import glob

for path in glob('*.whl'):
    print(path)
    wheel = WheelDistribution.from_path(path)
    try:
        print(len(wheel.get_metadata()))
    except FileNotFoundError:
        pass

