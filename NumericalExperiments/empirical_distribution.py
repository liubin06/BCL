import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
import seaborn as sns
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)


font_dict=dict(fontsize=20,
              color='black',
              family='Times New Roman',
              weight='light',
              style='italic',
              )

######################Algorithm 1################################
def generatesample(alpha):
    pos_scores = []
    neg_scores = []
    for anchor in range(M_anchors):
        for unlabel in range(N_negatives):
            if np.random.uniform(0, 1) < tau_plus:
                # generate positive sample
                pos_score = AccRejetSamplingFN(alpha,miu, std)
                pos_scores.append(pos_score)
            else:
                # generate negative sample
                neg_score = AccRejetSamplingTN(alpha,miu, std)
                neg_scores.append(neg_score)
    pos_socres,neg_scores = np.array(pos_scores),np.array(neg_scores)
    print("alpha value: %.2f" % alpha)
    return pos_scores,trasform(pos_socres,temperater),neg_scores,trasform(neg_scores,temperater)


miu,std = 0, 1
######################Algorithm 2################################
def AccRejetSamplingTN(alpha,miu,std):
    neg_score = np.random.normal(miu, std)
    proposal_cdf = scipy.stats.norm.cdf(neg_score, miu, std)
    while np.random.uniform(0, 1) > (alpha + (1 - 2 * alpha) * proposal_cdf) / alpha:
        neg_score = np.random.normal(miu, std)
        proposal_cdf = scipy.stats.norm.cdf(neg_score, miu, std)
    return neg_score

######################Algorithm 3################################
def AccRejetSamplingFN(alpha,miu,std):
    pos_score = np.random.normal(miu, std)
    proposal_cdf = scipy.stats.norm.cdf(pos_score, miu, std)
    while np.random.uniform(0, 1) > (1 - alpha + (2 * alpha - 1) * proposal_cdf) / alpha:
        pos_score = np.random.normal(miu, std)
        proposal_cdf = scipy.stats.norm.cdf(pos_score, miu, std)
    return pos_score


def trasform(x,temperater):
    return np.exp(x/temperater)


M_anchors = 1
N_negatives = 20000
tau_plus = 0.5
beta = 0
temperater = 2

#draw Fig.4: emperical distribution
plt.figure(figsize=(6, 6*0.618))
plt.subplot(221)
pos_scores,trans_posscores, neg_scores, trans_negscores= generatesample(0.52)
sns.distplot(trans_posscores,bins=80,label='FN',kde=True,color='#FF5ACD')
sns.distplot(trans_negscores,bins=80,label='TN',kde = True,color= '#2BD2FF')
plt.text(3.8,0.75,r'$\alpha=0.5$',fontdict=font_dict)
plt.xlabel("$exp(\hat{x}/t)$",fontdict=font_dict)
plt.ylabel("Density",fontdict=font_dict)
plt.xlim(-0.5,5)
plt.ylim(0,1.4)
plt.grid()
plt.legend(fontsize=20)

plt.subplot(222)
pos_scores,trans_posscores, neg_scores, trans_negscores= generatesample(0.7)
sns.distplot(trans_posscores,bins=80,label='FN',kde=True,color='#FF5ACD')
sns.distplot(trans_negscores,bins=80,label='TN',kde = True,color= '#2BD2FF')
plt.text(3.8,0.75,r'$\alpha=0.7$',fontdict=font_dict)
plt.xlabel("$exp(\hat{x}/t)$",fontdict=font_dict)
plt.ylabel("Density",fontdict=font_dict)
plt.xlim(-0.5,5)
plt.ylim(0,1.4)
plt.grid()
plt.legend(fontsize=20)

plt.subplot(223)
pos_scores,trans_posscores, neg_scores, trans_negscores= generatesample(0.9)
sns.distplot(trans_posscores,bins=80,label='FN',kde=True,color='#FF5ACD')
sns.distplot(trans_negscores,bins=80,label='TN',kde = True,color= '#2BD2FF')
plt.text(3.8,0.75,r'$\alpha=0.9$',fontdict=font_dict)
plt.xlabel("$exp(\hat{x}/t)$",fontdict=font_dict)
plt.ylabel("Density",fontdict=font_dict)
plt.xlim(-0.5,5)
plt.ylim(0,1.4)
plt.grid()
plt.legend(fontsize=20)

plt.subplot(224)
pos_scores,trans_posscores, neg_scores, trans_negscores= generatesample(1)
sns.distplot(trans_posscores,bins=80,label='FN',kde=True,color='#FF5ACD')
sns.distplot(trans_negscores,bins=80,label='TN',kde = True,color= '#2BD2FF')
plt.text(3.8,0.75,r'$\alpha=1$',fontdict=font_dict)
plt.xlabel("$exp(\hat{x}/t)$",fontdict=font_dict)
plt.ylabel("Density",fontdict=font_dict)
plt.xlim(-0.5,5)
plt.ylim(0,1.4)
plt.grid()
plt.legend(fontsize=20)
plt.show()