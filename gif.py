import imageio.v3 as iio

def read_gif(imagefiles):
    images = []
    for image in imagefiles:
        images.append(iio.imread(image)) #add actual image data to list
    return images

def create_gif(gifname, images, duration = 500, loop = 0):
    iio.imwrite(gifname, images, duration = duration, loop = loop)

def main():
    imagefiles = ['image1.png', 'image2.png', 'image3.png'] #include the images path
    images = read_gif(imagefiles)
    create_gif("mygif.gif", images, duriation = 500, loop = 0) 