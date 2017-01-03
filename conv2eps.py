#!/usr/bin/env python
#-*-coding : utf-8-*-

import sys
from PIL import Image

def epsfn(fn):
    if fn:
        i = fn.rfind('.')
        return fn[:i] + '.eps'
    return None

def convert2eps(fn, eps):
    im = Image.open(fn)
    im.save(eps)

if __name__ == '__main__':
    i = 0
    for fn in sys.argv[1:]:
        eps = epsfn(fn)
        print 'conv %s to %s' %(fn, eps)
        convert2eps(fn, eps)
        i += 1
    print 'Convert %s/%s images.\nDone!\n' %(i, len(sys.argv[1:]))
