import dados
import numpy as np
from scipy.optimize import minimize

#for index, cpal in enumerate(dados.cpal):
#    dados.qpal_calc.append((dados.qmax*dados.kdpal*cpal)/(1+(dados.kdole*dados.cole[index])+(dados.kdlin*dados.clin[index])+(dados.kdpal*cpal)))
#    dados.qole_calc.append((dados.qmax*dados.kdole*dados.cole[index])/(1+(dados.kdole*dados.cole[index])+(dados.kdlin*dados.clin[index])+(dados.kdpal*cpal)))
#    dados.qlin_calc.append((dados.qmax*dados.kdlin*dados.clin[index])/(1+(dados.kdole*dados.cole[index])+(dados.kdlin*dados.clin[index])+(dados.kdpal*cpal)))
#    print index, cpal

#for index, qpal_calc in enumerate(dados.qpal_calc):
#    dados.calc_fobj1.append(pow(((dados.qpal[index]/dados.qmax)-(qpal_calc/dados.qmax)), 2))
#    dados.calc_fobj2.append(pow(((dados.qole[index]/dados.qmax)-(dados.qole_calc[index]/dados.qmax)), 2))
#    dados.calc_fobj3.append(pow(((dados.qlin[index]/dados.qmax)-(dados.qlin_calc[index]/dados.qmax)), 2))

def fqpal_fobj(x):
    """qpal_calc FOBJ function"""
    dados.qpal_calc = []
    dados.qole_calc = []
    dados.qlin_calc = []
    dados.calc_fobj1 = []
    dados.calc_fobj2 = []
    dados.calc_fobj3 = []
    for index, cpal in enumerate(dados.cpal):
        dados.qpal_calc.append((dados.qmax*x[0]*cpal)/(1+(x[1]*dados.cole[index])+(x[2]*dados.clin[index])+(x[0]*cpal)))
        dados.qole_calc.append((dados.qmax*x[1]*dados.cole[index])/(1+(x[1]*dados.cole[index])+(x[2]*dados.clin[index])+(x[0]*cpal)))
        dados.qlin_calc.append((dados.qmax*x[2]*dados.clin[index])/(1+(x[1]*dados.cole[index])+(x[2]*dados.clin[index])+(x[0]*cpal)))
    for i, qpal_calc in enumerate(dados.qpal_calc):
        dados.calc_fobj1.append(pow(((dados.qpal[i]/dados.qmax)-(qpal_calc/dados.qmax)), 2))
        dados.calc_fobj2.append(pow(((dados.qole[i]/dados.qmax)-(dados.qole_calc[i]/dados.qmax)), 2))
        dados.calc_fobj3.append(pow(((dados.qlin[i]/dados.qmax)-(dados.qlin_calc[i]/dados.qmax)), 2))

    return sum(dados.calc_fobj1) + sum(dados.calc_fobj2) + sum(dados.calc_fobj3)

#print("%20.15e"% (dados.cpal[1]))
#print(dados.cpal[0])
#dados.qpal_calc.append((dados.qmax*dados.kdpal*dados.cpal[0])/(1+(dados.kdole*dados.cole[0])+(dados.kdlin*dados.clin[0])+(dados.kdpal*dados.cpal[0])))
#dados.qole_calc.append((dados.qmax*dados.kdole*dados.cole[0])/(1+(dados.kdole*dados.cole[0])+(dados.kdlin*dados.clin[0])+(dados.kdpal*dados.cpal[0])))
#dados.qlin_calc.append((dados.qmax*dados.kdlin*dados.clin[0])/(1+(dados.kdole*dados.cole[0])+(dados.kdlin*dados.clin[0])+(dados.kdpal*dados.cpal[0])))

##dados.qpal_calc.append(2**22)
#print dados.qpal_calc
#print dados.qole_calc
#print dados.qlin_calc
#print dados.calc_fobj1
#print dados.calc_fobj2
#print dados.calc_fobj3

#def Fqpal_fobj(x):
#    """qpal_calc FOBJ function"""
#    dados.qpal_calc.append((dados.qmax*x[0]*dados.cpal[0])/(1+(x[1]*dados.cole[0])+(x[2]*dados.clin[0])+(x[0]*dados.cpal[0])))
#    return pow(((dados.qpal[0]/dados.qmax)-(dados.qpal_calc[0]/dados.qmax)), 2)


x0 = np.array([dados.kdpal, dados.kdole, dados.kdlin])
##x0.put(1,5)
#print x0[0]
#res = fqpal_fobj(x0)
#print res
#res = fqpal_fobj(x0)
#print res

res = minimize(fqpal_fobj, x0, method='nelder-mead', options={'xtol': 1e-8, 'disp': True, 'maxfev': 1000})

print res.items()

