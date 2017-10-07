# coding: utf-8
from pylab import *
from numpy import *
from minoritygame import *

T = 200
s = 2
m = 7
N = 101
fig = figure(1,figsize=(8,4))
sim = System(T=1,N=N, m=m,s=s)
S = zeros([N,s,T])
for t in range(T):
    for i in range(N):
        u=sim.Users[i]
        for j in range(s):
            S[i,j,t] = u.Strategies[j].score
    sim.run()
S = S.reshape([N*s,T])
for i in range(N*s):
    plot(S[i,:])
xlabel(r'$t$')
ylabel(r'$strategy\ scores$')
fig.set_tight_layout(True)
savefig('figs/test/strategy_scores_vs_t-s'+str(s)+'m'+str(m)+'.png', format='png',bbox_inches='tight')
