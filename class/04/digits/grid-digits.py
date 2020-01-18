IMAGE_HEIGHT = 28
IMAGE_WIDTH = 28

ALL_IMG = []
ALL_LBL = []

#################################################
# read_all_image_label
#################################################

def read_all_image_label(img_file='test_images.txt', \
                         lbl_file='test_labels.txt'):
    fp_img = open(img_file, 'r')
    fp_lbl = open(lbl_file, 'r')
    try:
        while True:
            img = []
            for j in range(IMAGE_HEIGHT):
                line = fp_img.readline().rstrip('\n')
                img.append(line)
            lbl = int(fp_lbl.readline().rstrip('\n'))
            ALL_IMG.append(img)
            ALL_LBL.append(lbl)
    except (EOFError, ValueError):
        fp_img.close()
        fp_lbl.close()


from colored import fg, bg, attr

def show_image(img, grid=False, i=None, j=None):
    def p(c, f=21, b=None):
        print('%s%s%s' % (fg(f),c,attr(0)), end='')

    hgrid_line = '-'*28*2
    p('|',b=0)
    p(hgrid_line+'\n',b=255)
    for line in img:
        p('|',b=0)
        for c in line:
            p(c,f=10)
            p('|',b=0)
        print()
        p(hgrid_line+'\n',b=0)
    print(); print()

read_all_image_label()

import random
r = random.randint(1,1000)

show_image( ALL_IMG[r] )

