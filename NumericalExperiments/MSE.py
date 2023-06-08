import random
import matplotlib.pyplot as plt
import torch
import numpy as np
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


def set_phi(temperater,gamma):
    '''

    Parameters
    ----------
    temperater: Temperater scaling
    gamma: Variation of proposal distribution

    Returns
    -------
    Anchor-specific a,b for seting proposal distribution phi~U[a,b]
    '''
    #each observation \hat_x: theoretical minimum -1/temperater**2 <=  \hat_x <=  theoretical maximum 1/temperater**2
    a = random.uniform(-1/temperater**2 ,-1/temperater**2 + gamma/temperater**2)
    b = random.uniform(1/temperater**2-gamma/temperater**2, 1/temperater**2 )
    return a,b

def phi(x,a,b):
    if a <=x<= b:
        return 1/(a-b)
    else:
        return 0

def Phi(x,a,b):
        if a < x<= b:
            return (x-a)/(b-a)
        elif  x<=a:
            return 0
        else:
            return 1

def AccRejetSamplingFN(alpha,a, b):
    pos_score = np.random.uniform(a, b)
    proposal_cdf = Phi(pos_score, a, b)
    while np.random.uniform(0, 1) > (1 - alpha + (2 * alpha - 1) * proposal_cdf) / alpha:
        pos_score = np.random.uniform(a, b)
        proposal_cdf = Phi(pos_score, a, b)
    return pos_score

def AccRejetSamplingTN(alpha, a, b):
    neg_score = np.random.uniform(a, b)
    proposal_cdf = Phi(neg_score, a, b)
    while np.random.uniform(0, 1) > (alpha + (1 - 2 * alpha) * proposal_cdf) / alpha:
        neg_score = np.random.uniform(a, b)
        proposal_cdf = Phi(neg_score, a, b)
    return neg_score



######################Algorithm 1################################
def generatesample(tau_plus,alpha,gamma,temperater,M_anchors,N_negatives):
    scores = []
    labels = []
    posscores = []
    for anchor in range(M_anchors):
        a, b = set_phi(temperater,gamma)
        anchor_scores = []
        anchor_labels = []
        anchor_pos = []
        for unlabel in range(N_negatives):
            if np.random.uniform(0, 1) < tau_plus:
                pos_score = AccRejetSamplingFN(alpha,a, b)  # generate positive samples
                anchor_scores.append(pos_score)
                anchor_labels.append(False)
            else:
                neg_score = AccRejetSamplingTN(alpha,a, b) # generate negative samples
                anchor_scores.append(neg_score)
                anchor_labels.append(True)
        for unlabel in range(10):
            pos_score = AccRejetSamplingFN(alpha,a, b)
            anchor_pos.append(pos_score)
        scores.append(anchor_scores)
        labels.append(anchor_labels)
        posscores.append(anchor_pos)
    #[M,N], [M,N], [M,10]
    scores,labels,posscores = np.array(scores),np.array(labels),np.array(posscores)
    return trasform(scores,temperater),labels,trasform(posscores,temperater)

def trasform(x,temperater):
    return np.exp(x/temperater)

def cdf_trans(tau_plus,alpha,p):
    tau_minus = 1-tau_plus
    a = (tau_minus-tau_plus)*(1-2*alpha-1e-8)
    b = 2*(alpha*tau_minus + (1-alpha)*tau_plus)
    c = -p
    cdf = (-b + torch.sqrt(b**2-4*a*c))/(2*a)
    return cdf

def estimator(scores,posscores,alpha, beta, tau_plus,temperater):
    # BCL estimator
    def BCL(negative_scores, alpha, beta, tau_plus):
        X = negative_scores.unsqueeze(1)
        hatx = negative_scores.unsqueeze(-1)
        cdf_u = (X <= hatx).sum(dim=-1) / X.shape[-1]
        cdf = cdf_trans(tau_plus, alpha, cdf_u)
        ccdf = 1 - cdf
        phi1 = 2 * ccdf
        phi2 = 2 * cdf

        x_tn = alpha * phi1 + (1 - alpha) * phi2
        x_fn = (1 - alpha) * phi1 + alpha * phi2

        x_htn = (alpha * (1 - beta) * phi1 + (1 - alpha) * beta * phi2) / (alpha * (1 - beta) + (1 - alpha) * beta + 1e-3)
        omega = x_htn / (x_tn * (1 - tau_plus) + x_fn * tau_plus)
        return omega
    negative_scores = torch.tensor(scores)
    omega = BCL(negative_scores,alpha,beta,tau_plus)
    theta_bcl = (negative_scores*omega).mean(dim=-1) / omega.mean(dim=-1)  #[M,]

    # InfoNCE estimator
    theta_biased = scores.mean(-1) #[M,]

    #DCL estimator M=3
    pos = posscores.mean(axis=-1) #[M,]
    minimal = np.e ** (-1 / temperater**2)
    theta_dcl = (-tau_plus *pos + theta_biased) / (1 - tau_plus) #[M,]
    theta_dcl = np.array([max(minimal,i) for i in theta_dcl])                   #[M,]

    #true value
    theta = np.array([scores[i][labels[i]].mean() for i in range(M_anchors) ]) #[M,]

    #mean_values
    mean_bcl = theta_bcl.mean().item()
    mean_dcl = theta_dcl.mean()
    mean_biased = theta_biased.mean()
    mean_theta = theta.mean()
    #MSE
    assert theta_bcl.shape[0] == M_anchors
    mse_bcl = ((theta - np.array(theta_bcl))**2).mean()
    mse_dcl = ((theta- theta_dcl)**2).mean()
    mse_biased = ((theta - theta_biased)**2).mean()
    return mean_theta,mean_bcl,mean_dcl,mean_biased,mse_bcl,mse_dcl,mse_biased

M_anchors = 100
N_negatives = 100
tau_plus = 0.1
alpha = 0.9
beta = 0.5
gamma = 0
temperater = 0.5
result = []

list = np.linspace(0.5,1,50)
for alpha in list:
    print("alpha value: %.2f" % alpha)
    scores,labels,posscores = generatesample(tau_plus,alpha,gamma,temperater,M_anchors,N_negatives)
    mean_theta,mean_bcl,mean_dcl,mean_biased,mse_bcl,mse_dcl,mse_biased = estimator(scores,posscores,alpha, beta, tau_plus,temperater)
    result.append([mean_theta,mean_bcl,mean_dcl,mean_biased,mse_bcl,mse_dcl,mse_biased])
y = np.array(result)


font_dict=dict(fontsize=36,
              color='black',
              family='Times New Roman',
              weight='light',
              style='italic',
              )

###################### MSE ################################
plt.figure(figsize=(6, 6*0.618))
plt.plot(list,y[:,4],linestyle='-.',linewidth=3,label=r'$MSE \theta_{BCL}$',color='#2BD2FF')
plt.plot(list,y[:,5],linestyle='-.',linewidth=3,label=r'$MSE \theta_{DCL}$',color='#2BFF88')
plt.plot(list,y[:,6],linestyle='-.',linewidth=3,label=r'$MSE \theta_{Biased}$',color = '#FA8BFF')
plt.xlabel(r"$\alpha$",fontdict=font_dict)
plt.ylabel(r"$MSE$",fontdict=font_dict)
plt.tick_params(labelsize=30)
plt.grid()
plt.legend(fontsize=30)
plt.show()

###################### Mean ################################
plt.figure(figsize=(6, 6*0.618))
plt.plot(list,y[:,0],label=r'$\bar\theta$',color='black')
plt.plot(list,y[:,1],linestyle='-.',linewidth=3,label=r'$\bar\theta_{BCL}$',color='#2BD2FF')
plt.plot(list,y[:,2],linestyle='-.',linewidth=3,label=r'$\bar\theta_{DCL}$',color='#2BFF88')
plt.plot(list,y[:,3],linestyle='-.',linewidth=3,label=r'$\bar\theta_{Biased}$',color = '#FA8BFF')
plt.xlabel(r"$\alpha$",fontdict=font_dict)
plt.ylabel(r"$\bar \theta$",fontdict=font_dict)
plt.tick_params(labelsize=30)
plt.grid()
plt.legend(fontsize=30)
plt.show()





