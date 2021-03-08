with open('xnuspy', 'rb') as f:
    ori = f.read()

with open('el1/xnuspy_ctl/xnuspy_ctl', 'rb') as f:
    ctl = f.read()
    
off = ori.find('XNUSPY_CTL_STUB_SPACE')
print "Found stub at offset %d" % off

with open('xnuspy_consolidated', 'wb') as f:
    f.write(ori[:off])
    f.write(ctl)
    f.write(ori[off+len(ctl):])