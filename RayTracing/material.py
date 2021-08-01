import random
from ray import vec3, ray, dot
import math

class material():
    def scatter(self, r_in, rec):
        return

    def reflect(self, v, n):
        return v - n * (dot(v, n)) * 2.0

    def refract(self, v, n, ni_over_nt):
        v = v.unit_vec()
        cos_in = dot(v, n)
        disc = 1.0 - ni_over_nt * ni_over_nt * (1 - cos_in**2)

        if disc > 0:
            return (v - n * cos_in) * ni_over_nt - n * math.sqrt(disc)
        else:
            return None


class lambertian(material):
    def __init__(self, albedo):
        super().__init__()
        self.albedo = albedo

    def scatter(self, r_in, rec):
        target = rec.normal + random_in_unit_sphere()
        scattered = ray(rec.p, target)
        attenuation = self.albedo
        return scattered, attenuation

class metal(material):
    def __init__(self, albedo, fuzz=0.0):
        super().__init__()
        self.albedo = albedo
        self.fuzz = fuzz

    def scatter(self, r_in, rec):
        target = rec.normal + random_in_unit_sphere()

        reflected = self.reflect(r_in.direction().unit_vec(), rec.normal)
        scattered = ray(rec.p, reflected + random_in_unit_sphere() * self.fuzz)
        attenuation = self.albedo
        if dot(scattered.direction(), rec.normal) > 0:
            return scattered, attenuation
        else:
            return None, None



class dielectric(material):
    def __init__(self, ref_idx):
        self.ref_idx = ref_idx

    def scatter(self, r_in, rec):

        attenuation = vec3(1.0, 1.0, 1.0)
        if dot(r_in.direction(), rec.normal) > 0:
            outward_normal = rec.normal * -1
            ni_over_nt = self.ref_idx
            cos = self.ref_idx * dot(r_in.direction(), rec.normal) / r_in.direction().length()
        else:
            outward_normal = rec.normal
            ni_over_nt = 1.0 / self.ref_idx
            cos = -1 * dot(r_in.direction(), rec.normal) / r_in.direction().length()

        refracted = self.refract(r_in.direction(), outward_normal, ni_over_nt)


        if refracted is not None:
            reflect_prob = self.schlick(cos)
            
        else:
            reflect_prob = 1.0
            
        if random.random() < reflect_prob:
            reflected = self.reflect(r_in.direction().unit_vec(), rec.normal)
            scattered = ray(rec.p, reflected)

        else:
            scattered = ray(rec.p, refracted)


        return scattered, attenuation

    def schlick(self, cos):
        r0 = (1.0 - self.ref_idx) / (1.0 + self.ref_idx)
        r0 **= 2
        return r0 + (1 - r0) * math.pow((1-cos), 5)


def random_in_unit_sphere():
    while True:
        p = vec3(random.random(), random.random(), random.random()) * 2.0 - vec3(1.0, 1.0, 1.0)

        if p.squared_length() < 1.0:
            return p