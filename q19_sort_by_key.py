'''write a python program to sort by key in dictionaries.'''

a={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshani':50}
h={}
max=0
for i in a:
    if a[i]>max:
        max=a[i]
        k=i
a.pop(k)
h.update({k:max})


smax=0
for i in a:
    if a[i]>smax:
        smax=a[i]
        d=i
# print(smax)
a.pop(d)
h.update({d:smax})

tmax=0
for i in a:
    if a[i]>tmax:
        tmax=a[i]
        m=i
h.update({m:tmax})
a.pop(m)

fmax=0
for i in a:
    if a[i]>fmax:
        fmax=a[i]
        s=i
h.update({s:fmax})
a.pop(s)

dmax=0
for i in a:
    if a[i]>dmax:
        dmax=a[i]
        l=i
h.update({l:dmax})
print('ascending order',h)

# g={'bijender':45,'deepak':60,'param':20,'anjali':30,'roshani':50}
# u={}
# min=0
# for i in g:
#     if g[i]<min:
#         min=g[i]
#         z=i
# print(min)
# g.pop(z)
# u.update({z:min})

# smin=0
# for i in g:
#     if g[i]<smin:
#         smin=g[i]
#         v=i
# u.update({v:smin})
# g.pop(v)

# tmin=0
# for i in g:
#     if g[i]<tmin:
#         tmin=g[i]
#         o=i
# u.update({o:tmin})
# g.pop(o)

# fmin=0
# for i in g:
#     if g[i]<fmin:
#         fmin=g[i]
#         t=i
# u.update({t:fmin})
# g.pop(t)

# dmin=0
# for i in g:
#     if g[i]<dmin:
#         dmin=g[i]
#         b=i
# u.update({b:dmax})
# print('discending order',u)

