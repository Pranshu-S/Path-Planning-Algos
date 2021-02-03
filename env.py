import numpy

class env:
    def __init__(self):
        self.x_range = 51
        self.y_range = 51
        self.motions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        self.obs = self.obs_map()

    def update_obs(self, obs):
        self.obs = obs

    def obs_map(self):
        x = self.x_range
        y = self.y_range
        obs = set()

        for i in range(x):
            obs.add((i, 0))
        for i in range(x):
            obs.add((i, y - 1))

        for i in range(y):
            obs.add((0, i))
        for i in range(y):
            obs.add((x - 1, i))

        for i in numpy.arange(0,7,0.3):
            obs.add((i,35-5*i))

        for i in range(7,45):
            obs.add((i,0.1315*i - 0.921))

        for i in numpy.arange(45,50,0.2):
            obs.add((i,8*i - 355))

        for i in range(25,50):
            obs.add((i,-0.2*i +55))

        for i in range(0,25):
            obs.add((i,0.6*i+35))

        for i in range(20,35):
            obs.add((i,15))
            obs.add((i,30))

        for i in range(15,30):
            obs.add((35,i))



        return obs
