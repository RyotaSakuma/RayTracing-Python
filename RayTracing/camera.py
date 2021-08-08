from ray import vec3, ray, dot
import math
import random

def random_in_unit_disk():
    while True:
        p = vec3(random.random(), random.random(), 0)*2.0 - vec3(1.0, 1.0, 0)
        if dot(p, p) < 1.0:
            return p

class camera():
    def __init__(self, fov, aspect, lookfrom, lookat, vup, aperture=None, focus_dist=None):

        self.lens_radius = aperture / 2      
        half_height = math.tan(math.radians(fov/2))
        half_width = aspect * half_height

        self.origin = lookfrom
        self.w = (lookfrom - lookat).unit_vec()
        self.u = vup.cross(self.w).unit_vec()
        self.v = self.w.cross(self.u)

        self.lower_left_corner = self.origin - (self.u * half_width + self.v * half_height + self.w) * focus_dist
        self.horizontal = self.u * (2.0 * half_width)
        self.vertical = self.v * (2.0 * half_height)

    def get_ray(self, s, t):
        rd = random_in_unit_disk() * self.lens_radius
        offset = self.u * rd.x + self.v * rd.y
        return ray(self.origin+offest, self.lower_left_corner+self.horizontal*s+self.vertical*t-self.origin-offset)
