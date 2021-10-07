try:
    debit,balance= map(float,input().split())
    if debit+0.5 <= balance and debit%5==0:
        print("%0.2f"%(balance-(debit+0.5)))
    else:
        print("%0.2f"%balance)
except:
    pass