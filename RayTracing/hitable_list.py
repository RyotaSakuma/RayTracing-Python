from material import lambertian
from ray import vec3
from hitable import hitable, hit_record, sphere
from ray import vec3
from material import lambertian, metal, dielectric
import random

class hitable_list(hitable):
    def __init__(self, list, n):
        #super().__init__()
        self.list = list
        self.list_size = n

    def hit(self, r, t_min, t_max):
        rec = None
        closest_so_far = t_max

        for i in range(self.list_size):
            tmp_rec = self.list[i].hit(r, t_min, closest_so_far)

            if tmp_rec is not None:
                closest_so_far = tmp_rec.t
                rec = tmp_rec

        return rec

def random_scene():
    h_list = [sphere(vec3(0, -1000, 0), 1000, lambertian(vec3(0.5, 0.5, 0.5)))]


    for a in range(-11,11):
        for b in range(-11,11):
            choose_mat = random.random()
            center = vec3(a+0.9*random.random(), 0.2, b+0.9*random.random())
            if (center - vec3(4, 0.2, 0)).length() > 0.9:
                if choose_mat < 0.8:
                    h_list.append(sphere(center, 0.2, lambertian(vec3(random.random()*random.random(), 
                        random.random()*random.random(), random.random()*random.random()))))
                elif choose_mat < 0.95:
                    h_list.append(sphere(center, 0.2, metal(vec3(0.5*(1.0+random.random()), 
                        0.5*(1.0+random.random()), 0.5*(1.0+random.random())), 0.5*(random.random()))))
                else:
                    h_list.append(sphere(center, 0.2, dielectric(1.5)))

    h_list.append(sphere(vec3(0.0,1.0,0.0), 1.0, dielectric(1.5)))
    h_list.append(sphere(vec3(-4.0, 1.0, 0.0), 1.0, lambertian(vec3(0.4, 0.2, 0.1))))
    h_list.append(sphere(vec3(4.0, 1.0, 0.0), 1.0, metal(vec3(0.7, 0.6, 0.5), 0.0)))

    return hitable_list(h_list, len(h_list))

def three_ball():
    h_list = [sphere(vec3(0.0, 0.0, -1.0), 0.5, lambertian(vec3(0.1,0.2,0.5)))]
    h_list.append(sphere(vec3(0, -100.5, -1.0), 100, lambertian(vec3(0.8, 0.8, 0.0))))
    h_list.append(sphere(vec3(1.0, 0.0, -1.0), 0.5, metal(vec3(0.8, 0.6, 0.2))))
    h_list.append(sphere(vec3(-1.0, 0.0, -1.0), 0.5, dielectric(1.5)))
    h_list.append(sphere(vec3(-1.0, 0.0, -1.0), -0.45, dielectric(1.5)))

    return hitable_list(h_list, 5)