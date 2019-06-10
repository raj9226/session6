def applyPromoCpde(promoCode,amount):
    if promoCode=="FLAT50":
        return amount*50/100
    elif promoCode=="FLAT30":
            return amount*30/100
    else:
        return amount*10/100
total =1000
#discount=applyPromoCpde("FLAT30",total)
#print("please pay:",total-discount)
print("please pay:\u20b9",total-applyPromoCpde("FLAT30",total))
print("apply promocode is:",applyPromoCpde)

#Reference copy
fun=applyPromoCpde
print("fun is:",fun)
print("please pay:\u20b9",total-fun("FLAT50",total))
#del applyPromoCpde
#print("please pay:\u20b9",total-fun("FLAT50",total))

#craete a function thatb apply promocode on the basis of following
#1.flat 50 if total->1000\
#2.flat 30 if total>500 and <1000
#3.we can purpose to apply a promocode which is more beneficial for him/her
#4.make sure of various taste cases