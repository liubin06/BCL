import matplotlib.pyplot as plt
import numpy as np
font_dict=dict(fontsize=20,
              color='black',
              family='Times New Roman',
              weight='light',
              style='italic',
              )
plt.rc('font', family='Times New Roman', size=12)
x = np.linspace(0,1,100)
tau_plus = 0.1
tau_minus = 0.9

def cdf_trans(tau_plus,alpha,p):
    a = (1-2*tau_plus)*(1-2*alpha-1e-8)
    b = 2*alpha*(1-tau_plus)+ tau_plus*(2-2*alpha+1e-8)
    c = -p
    cdf = (-b + np.sqrt(b**2-4*a*c))/(2*a)
    return cdf

def cdf_trans1(cdf_u, alpha, tau_plus):
    tau_minus = 1 - tau_plus
    a = (1 - 2 * alpha) * (tau_minus - tau_plus) + 1e-8
    b = 2 * (alpha * tau_minus + (1 - alpha) * tau_plus)
    return (-b + np.sqrt(b ** 2 + 4 * a * cdf_u)) / (2 * a)

def w(alpha,beta,cdf_u):
    cdf = cdf_trans(tau_plus,alpha,cdf_u)
    #cdf = cdf_trans1(cdf_u, alpha, tau_plus)
    ccdf = 1 - cdf
    phi1 = 2 * ccdf
    phi2 = 2 * cdf

    x_tn = alpha * phi1 + (1 - alpha) * phi2
    x_fn = (1 - alpha) * phi1 + alpha * phi2

    x_htn = (alpha * (1 - beta) * phi1 + (1 - alpha) * beta * phi2) / (alpha * (1 - beta) + (1 - alpha) * beta +1e-8)
    omega = x_htn / (x_tn * (1 - tau_plus) + x_fn * tau_plus)
    return omega



alpha = 0.999
plt.subplot(231)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(1.0))

alpha = 0.9
plt.subplot(232)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(alpha))

alpha = 0.8
plt.subplot(233)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(alpha))

alpha = 0.7
plt.subplot(234)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(alpha))

alpha = 0.6
plt.subplot(235)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(alpha))

alpha = 0.5
plt.subplot(236)
y1 = w(alpha,1,x)
plt.plot(x,y1,label=r'$\beta$ = 1.00')
y1 = w(alpha,0.98,x)
plt.plot(x,y1,label=r'$\beta$ = 0.98')
y1 = w(alpha,0.96,x)
plt.plot(x,y1,label=r'$\beta$ = 0.96')
y1 = w(alpha,0.94,x)
plt.plot(x,y1,label=r'$\beta$ = 0.94')
y1 = w(alpha,0.92,x)
plt.plot(x,y1,label=r'$\beta$ = 0.92')
y1 = w(alpha,0.9,x)
plt.plot(x,y1,label=r'$\beta$ = 0.90')
y1 = w(alpha,0.8,x)
plt.plot(x,y1,label=r'$\beta$ = 0.80')
y1 = w(alpha,0.7,x)
plt.plot(x,y1,label=r'$\beta$ = 0.70')
y1 = w(alpha,0.6,x)
plt.plot(x,y1,label=r'$\beta$ = 0.60')
y1 = w(alpha,0.5,x)
plt.plot(x,y1,label=r'$\beta$ = 0.50')
plt.legend()
plt.grid()
plt.xlabel(r'$\hat\Phi(x)$')
plt.ylabel(r'$\omega$')
plt.title(r'$\alpha={}$'.format(alpha))

plt.show()

