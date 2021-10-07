def simple_interest(p,r,t):
    return (p*r*t)/100
print(simple_interest(100, 5, 20))

def compound_interest(p,r,t):
    ci = p*(1+(r)/100)**t
    return ci-p
print(compound_interest(100, 5, 20))