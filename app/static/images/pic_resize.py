from PIL import Image, ImageOps

# print(im.format)


def pic_resize(img: str):
    file_name = img.split(".")[0]
    im = Image.open(img)
    r = im.resize((2000, 360))  # save 2000x360
    r.save(file_name + "_2000x360.jpg")
    r = im.resize((4000, 720))  # save 4000x720
    r.save(file_name + "_4000x720.jpg")
    r = im.resize((500, 500))  # save 500x500
    r.save(file_name + "_500x500.jpg")
    r = im.resize((1000, 1000))  # save 1000x1000
    r.save(file_name + "_1000x1000.jpg")


def custom_resize(img: str, h: int, w: int):
    file_name = img.split(".")[0]
    im = Image.open(img)
    r = im.resize((h, w))
    r.save(f"{file_name}_{str(h)}x{str(w)}.jpg")


def add_whitespace(img: str, h: int, w: int):
    file_name = img.split(".")[0]
    old_im = Image.open(img)
    old_size = old_im.size
    new_size = (h, w)
    new_im = Image.new("RGB", new_size, fill="white")
    new_im.paste(
        old_im, ((new_size[0] - old_size[0]) // 2, (new_size[1] - old_size[1] // 2))
    )
    new_im.save(f"{file_name}_{str(h)}x{str(w)}_padwhite.jpg")


def add_border(img: str):
    file_name = img.split(".")[0]
    old_im = Image.open(img)
    im_with_border = ImageOps.expand(old_im, border=500, fill="white")
    im_with_border.save(f"{file_name}_whiteborder.jpg")


if __name__ == "__main__":
    # pic_resize('city-redbus.jpg')
    custom_resize("matrix.jpg", 2000, 720)
    # add_border("website3.jpg")
