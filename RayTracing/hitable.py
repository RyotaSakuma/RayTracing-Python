from ray import vec3, ray
import math
from material import material
import random

class hit_record():
    def __init__(self, t=None, p=None, normal=None, mat=None):
        self.t = t
        self.p = p
        self.normal = normal
        self.mat = mat


class hitable():
    def hit(self, r, t_min, t_max):
        return

class sphere(hitable):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.mat = material

    def hit(self, r, t_min, t_max):
        rec = hit_record()
        oc = r.origin() - self.center
        a = r.direction().dot(r.direction())
        b = r.direction().dot(oc) * 2.0
        c = (oc).dot(oc) - self.radius**2

        disc = b**2 - 4.0*a*c
        if disc > 0:
            tmp = -(b+math.sqrt(disc)) / (2.0*a)
            if tmp < t_max and tmp > t_min:
                rec.mat = self.mat
                rec.t = tmp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return rec

            tmp = (-b+math.sqrt(disc))/ (2.0*a)
            if tmp < t_max and tmp > t_min:
                rec.mat = self.mat
                rec.t = tmp
                rec.p = r.point_at_parameter(rec.t)
                rec.normal = (rec.p - self.center) / self.radius
                return rec

        return None