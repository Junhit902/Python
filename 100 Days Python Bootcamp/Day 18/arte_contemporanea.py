import colorgram

rgb_cores = []

cores = colorgram.extract("images.jpg", 15)

def cor_nova():
    for cor_rgb in cores:
        r = cor_rgb.rgb.r
        g = cor_rgb.rgb.g
        b = cor_rgb.rgb.b
        nova_cor = (r, g, b)
        rgb_cores.append(nova_cor)
    return rgb_cores
print(cor_nova())
