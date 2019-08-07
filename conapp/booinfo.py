class Book:

    def __init__(self,bnm,bpub,bath,bprice,bqty,bid=0):
        self.book_name = bnm
        self.book_pub = bpub
        self.book_auth = bath
        self.book_price = bprice
        self.book_qty = bqty
        self.book_id = bid

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)