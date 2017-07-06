import sys
from PIL import Image, ImageDraw

Phi = 1.618
phi = 0.618

def Mdraw_fib():
        result = []
        a, b = 0, 1
        size =  650, 650
        s = 0
        dCent = 300
        while b <= 650:
                result.append(b)
                a, b = b, a+b
        Spiral = Image.new('RGB', size, "white")
        draw = ImageDraw.Draw(Spiral)
        draw.line((dCent, dCent, dCent, dCent+result[0]), fill="red")
        draw.line((dCent, dCent+result[0], dCent-result[1], dCent+result[0]), fill="red")
        draw.line((dCent-result[1], dCent+result[0], dCent-result[1], dCent-result[2]), fill="red")
        draw.line((dCent-result[1], dCent-result[2], dCent+result[3], dCent-result[2]), fill="red")	
        draw.line((dCent+result[3], dCent-result[2], dCent+result[3], dCent+result[4]), fill="red")
        draw.line((dCent+result[3], dCent+result[4], dCent-result[5], dCent+result[4]), fill="red")	
        draw.line((dCent-result[5], dCent+result[4], dCent-result[5], dCent-result[6]), fill="red")
        draw.line((dCent-result[5], dCent-result[6], dCent+result[7], dCent-result[6]), fill="red")
        draw.line((dCent+result[7], dCent-result[6], dCent+result[7], dCent+result[8]), fill="red")	
        draw.line((dCent+result[7], dCent+result[8], dCent-result[9], dCent+result[8]), fill="red")	
        draw.line((dCent-result[9], dCent+result[8], dCent-result[9], dCent-result[10]), fill="red")	
        draw.line((dCent-result[9], dCent-result[10], dCent+result[11], dCent-result[10]), fill="red")	
        draw.line((dCent+result[11], dCent-result[10], dCent+result[11], dCent+result[12]), fill="red")	
        draw.line((dCent+result[11], dCent+result[12], dCent-result[13], dCent+result[12]), fill="red")
        draw.line((dCent-result[13], dCent+result[12], dCent-result[13], dCent-result[14]), fill="red")
        Spiral.save("Spiral.png", "PNG")
        return 0
        
        """
'''
	draw.arc((dCent, dCent, dCent, dCent+result[0]),0, 45, fill="green")
	draw.arc((dCent, dCent+result[0], dCent-result[1], dCent+result[0]),0, 45, fill="green")
	draw.arc((dCent-result[1], dCent+result[0], dCent-result[1], dCent-result[2]),0, 45,  fill="green")
	draw.arc((dCent-result[1], dCent-result[2], dCent+result[3], dCent-result[2]),0, 45, fill="green")	
	draw.arc((dCent+result[3], dCent-result[2], dCent+result[3], dCent+result[4]),0, 45, fill="green")
	draw.arc((dCent+result[3], dCent+result[4], dCent-result[5], dCent+result[4]),0, 45, fill="green")	
	draw.arc((dCent-result[5], dCent+result[5], dCent-result[5], dCent-result[6]),0, 45, fill="green")
	draw.arc((dCent-result[5], dCent-result[6], dCent+result[7], dCent-result[6]),0, 45, fill="green")	
	draw.arc((dCent+result[7], dCent-result[6], dCent+result[7], dCent+result[8]),0, 45, fill="green")	
	draw.arc((dCent+result[7], dCent+result[8], dCent-result[9], dCent+result[8]),0, 45, fill="green")	
	draw.arc((dCent-result[9], dCent+result[8], dCent-result[9], dCent-result[10]),0, 45, fill="green")	
	draw.arc((dCent-result[9], dCent-result[10], dCent+result[11], dCent-result[10]),0, 45, fill="green")	
	draw.arc((dCent+result[11], dCent-result[10], dCent+result[11], dCent+result[12]),0, 45, fill="green")	
	draw.arc((dCent+result[11], dCent+result[12], dCent-result[13], dCent+result[12]),0, 45, fill="green")
	draw.arc((dCent-result[13], dCent+result[12], dCent-result[13], dCent-result[14]),0, 45, fill="green")
	'''
			
			"""
        

def Mdraw_lucas():
        result = []
        a, b = 2, 1
        size =  650, 650
        s = 0
        dCent = 300
        while b <= 650:
                result.append(b)
                a, b = b, a+b
        Spiral = Image.new('RGB', size, "white")
        draw = ImageDraw.Draw(Spiral)
        draw.line((dCent, dCent, dCent, dCent+result[0]), fill="red")
        draw.line((dCent, dCent+result[0], dCent-result[1], dCent+result[0]), fill="red")
        draw.line((dCent-result[1], dCent+result[0], dCent-result[1], dCent-result[2]), fill="red")
        draw.line((dCent-result[1], dCent-result[2], dCent+result[3], dCent-result[2]), fill="red")	
        draw.line((dCent+result[3], dCent-result[2], dCent+result[3], dCent+result[4]), fill="red")
        draw.line((dCent+result[3], dCent+result[4], dCent-result[5], dCent+result[4]), fill="red")	
        draw.line((dCent-result[5], dCent+result[4], dCent-result[5], dCent-result[6]), fill="red")
        draw.line((dCent-result[5], dCent-result[6], dCent+result[7], dCent-result[6]), fill="red")	
        draw.line((dCent+result[7], dCent-result[6], dCent+result[7], dCent+result[8]), fill="red")	
        draw.line((dCent+result[7], dCent+result[8], dCent-result[9], dCent+result[8]), fill="red")	
        draw.line((dCent-result[9], dCent+result[8], dCent-result[9], dCent-result[10]), fill="red")	
        draw.line((dCent-result[9], dCent-result[10], dCent+result[11], dCent-result[10]), fill="red")	
        draw.line((dCent+result[11], dCent-result[10], dCent+result[11], dCent+result[12]), fill="red")	
        Spiral.save("Spiral.png", "PNG")
        return 0
		


def fib(y):
        result = []
        a, b = 0, 1
        while b <= y:
                result.append(b)
                a, b = b, a+b
        return result

def lucas(y):
        result = []
        a, b = 2, 1
        while b <= y:
                result.append(b)
                a, b = b, a+b
        return result

def divPhi(x):
        result = x/Phi
        return result

def divphi(x):
        result = x/phi
        return result

def idivPhi(x):
        result = int(x/Phi)
        return result

def idivphi(x):
        result = int(x/phi)
        return result

def PhiE(x, y):
        result = []
        a, b = x, x
        while b <= y:
                result.append(b)
                b = a**Phi
                a += 1
        return result

def PhiEi(x, y):
        result = []
        a, b = x, x
        while b <= y:
                result.append(b)
                b = int(a**Phi)
                a += 1
        return result

def PhiA(y):
        x = Phi
        result = []
        while x <= y:
                result.append(x)
                x = x+Phi
        return result

def PhiAi(y):
        a = Phi
        b = int(a)
        result = []
        while b <= y:
                result.append(b)
                a = a+Phi
                b = int(a)
        return result

def phiE(x, y):
        result = []
        a, b = x, x
        while b <= y:
                result.append(b)
                b = a**phi
                a += 1
        return result

def phiEi(x, y):
        result = []
        a, b = x, x
        while b <= y:
                result.append(b)
                b = int(a**phi)
                a += 1
        return result

def phiA(y):
        x = phi
        result = []
        while x <= y:
                result.append(x)
                x = x+phi
        return result

def phiAi(y):
        a = phi
        b = int(a)
        result = []
        while b <= y:
                result.append(b)
                a = a+phi
                b = int(a)
        return result

def main():
        print('''*************************************************\n
*  Please Enter The Number of The Ratio to Use  *\n
* 1.  Phi Exponent Ratio                        *\n
* 2.  Phi Exponent Ratio as integer             *\n
* 3.  Phi Addition Ratio                        *\n
* 4.  Phi Addition Ratio as integer             *\n
* 5.  phi Exponent Ratio                        *\n
* 6.  phi Exponent Ratio as integer             *\n
* 7.  phi Addition Ratio                        *\n
* 8.  phi Addition Ratio as integer             *\n
* 9.  Divide By Phi                             *\n
* 10. Divide By Phi      as integer             *\n
* 11. Divide By phi                             *\n
* 12. Divide By phi      as integer             *\n
* 13. Fabonacci Sequence                        *\n
* 14. Lucas Numbers                             *\n
* 15. draw straight line Fabonacci Spiral       *\n
* 16. draw straight line Lucas Spiral           *\n
* 17. References                                *\n
* 18. Exit                                      *\n
*************************************************''')
        RatioOpt = int(input())
        if RatioOpt == 1:
                x = input('Enter starting exponent: ')
                y = input('Enter max number in sequence: ')
                print(PhiE(x, y))
        elif RatioOpt == 2:        
                x = input('Enter starting exponent: ')
                y = input('Enter max number in sequence: ')
                print(PhiEi(x, y))
        elif RatioOpt == 3:
                y = input('Enter max number in sequence: ')
                print(PhiA(y))
        elif RatioOpt == 4:
                y = input('Enter max number in sequence: ')
                print(PhiAi(y))
        elif RatioOpt == 5:        
                x = input('Enter starting exponent: ')
                y = input('Enter max number in sequence: ')
                print(phiE(x, y))        
        elif RatioOpt == 6:        
                x = input('Enter starting exponent: ')
                y = input('Enter max number in sequence: ')
                print(phiEi(x, y))        
        elif RatioOpt == 7:        
                y = input('Enter max number in sequence: ')
                print(phiA(y))
        elif RatioOpt == 8:        
                y = input('Enter max number in sequence: ')
                print(phiAi(y))
        elif RatioOpt == 9:
                x = input('Enter number to divide by Phi: ')
                print(divPhi(x))
        elif RatioOpt == 10:        
                x = input('Enter number to divide by Phi: ')
                print(idivPhi(x))
        elif RatioOpt == 11:        
                x = input('Enter number to divide by phi: ')
                print(divphi(x))        
        elif RatioOpt == 12:        
                x = input('Enter number to divide by phi: ')
                print(idivphi(x))        
        elif RatioOpt == 13:                
                y = input('Enter max number in sequence: ')
                print(fib(y))
        elif RatioOpt == 14:                
                y = input('Enter max number in sequence: ')
                print(lucas(y))
        elif RatioOpt == 15:
                Mdraw_fib()
        elif RatioOpt == 16:
                Mdraw_lucas()



                
        elif RatioOpt == 17:
                print('http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/lucasNbs.html')
        elif RatioOpt == 18:
                return 0
                sys.exit
        else:
                main()
                
if __name__ == '__main__':
# sys.exit(main(sys.argv)) # used to give a better look to exists
        main()
