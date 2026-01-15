def decorate(x):
    def wapper():
        print("wellcome")
        x()
        print("In Universal informatics indore")
    return wapper

@decorate
def greet():
    print("Sneha Patel")

greet()

#add some new implementation or fecutres without adding in a functions 