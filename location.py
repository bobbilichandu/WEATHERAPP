import geocoder
def loc(val):
    if val==1:
        g = geocoder.ip('me')
        k=g.latlng
        return k