from ipaddress import ip_address
import geocoder as geo

ip_address = geo.ip('me')
print(ip_address)
text = input("Enter the text: ")
ip = geo.ip(text)
print(ip.city)
print(ip.latlng)
info = geo.google('Kyiv')
print(info.geojson)
print(info.osm)
print(info.wkt)