#!/usr/bin/python
import math
import Image


BLACK = (0,0,0)

def warm_color_lookup_table(z=0,iteration=0):
	return (0,111,1) #dull green

def cool_color_lookup_table(z=0,iteration=0):
	return (230,52,0) #orange-red

def convert_coordinates(floatx,floaty):
	x = -int((-0.613 - floatx)*1000)
	y = -int((-1.3 - floaty)*1000)
	return (x,y)

def paint():
	x_range = [-0.613 + n*0.001 for n in range(1+int(1000*(0.605+0.613)))]
	y_range = [-1.30 + n*0.001 for n in range(1+int(1000*(1.3+0.405)))]

	im = Image.new("RGB",(len(x_range),len(y_range)),(255,255,255))

	for xc in x_range:
		for yc in y_range:
			z = complex(xc,yc)
			trapped = False
			iteration = 1
			while trapped == False:
				z = z**2 - z/2 + (math.sqrt(5)-1)/2
				x = z.real
				y = z.imag
				if abs(x-3.5)<0.9 and abs(y-1)<0.9 and iteration>1:
					color = warm_color_lookup_table(z,iteration)
					trapped = True
					print 'WARM'
				u = abs(complex(x-3.5,1))
				e1 = abs(2*y-2-math.cos(2*math.pi*u/3))
				e2 = abs(2*y-2-math.cos(2*math.pi*(u-1)/3))
				e3 = abs(2*y-2-math.cos(2*math.pi*(u+1)/3))
				if(e1<0.1 or e2<0.1 or e3<0.1) and iteration > 1:
					color = warm_color_lookup_table(z,iteration)
					trapped = True
					print 'WARM'
				if abs(x) > 10**10:
					color = cool_color_lookup_table(z,iteration)
					trapped = True
					print 'COOL'
				if iteration > 50:
					color = BLACK
					trapped = True
					print 'BLACK'
				iteration += 1
			print "Plotting",xc,",",yc
			intx,inty = convert_coordinates(xc,yc)
			print "Converted to",intx,",",inty
			im.putpixel((intx,inty),color)
			print "Finished plotting",xc,",",yc
	im.save("painting.png","PNG")

if __name__ == '__main__':
	paint()
