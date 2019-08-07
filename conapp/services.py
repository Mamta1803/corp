
from abc import ABC, abstractmethod
from conapp.restapi import *
import requests


# class BookServices(ABC):
#
#     @abstractmethod
#     def fetchall_books(self):
#         pass
#
#     @abstractmethod
#     def fetch_book(self, book_id):
#         pass
#
#     @abstractmethod
#     def remove_book(self, book_id):
#         pass
#
#     @abstractmethod
#     def add_book(self, book_ob):
#         pass
#
#     @abstractmethod
#     def modify_book(self, book_ob):
#         pass


class BookImpl():

    @staticmethod
    def fetchall_books():
        response = requests.get(BASE_URL)
        json_obj = response.json()
        all_books = deserialiser(json_obj,'M')
        return all_books

    @staticmethod
    def fetch_book(book_id):
        response = requests.get(BASE_URL+str(book_id))
        json_obj = response.json()
        book = deserialiser(json_obj, 'S')
        return book

    @staticmethod
    def remove_book(book_id):
        ob = BookImpl.fetch_book(book_id)
        if ob:
            requests.delete(BASE_URL + str(book_id))
            return 'Deleted successfully'
        else:
            print('Book not available')

    @staticmethod
    def add_book(book_ob):
        if type(book_ob) == Book:
            if book_ob.book_id == 0:
                book_ob.__dict__.pop("book_id")
            response = requests.post(url=BASE_URL,data=book_ob.__dict__)
            print(response.status_code)
            print(book_ob.__dict__)
            # print(response.json())
            print('Data added successfully!!!')
        else:
            print('invalid book type!!!')

    @staticmethod
    def modify_book(book_ob):
        ob = BookImpl.fetch_book(book_ob.book_id)
        print(ob)
        if ob:
            ob.book_name = book_ob.book_name
            ob.book_pub = book_ob.book_pub
            ob.book_auth = book_ob.book_auth
            ob.book_price = book_ob.book_price
            ob.book_qty = book_ob.book_qty
            response = requests.put(url=BASE_URL + str(book_ob.book_id) + '/',json=ob.__dict__)
            print(response.json())
            return 'updated successfully'
        else:
            print('book not found !!!')



if __name__ == '__main__':
    boj = BookImpl() #not needed for static method
    blist = BookImpl.fetchall_books()
    print(blist)
    # print(type(blist))
    # print(type(blist[0]))

    # b1 = BookImpl.fetch_book(2)
    # print(b1)
    # print(type(b1))

    # ob = Book(bnm='mango',bpub='lenom',bath='batman',bprice=999,bqty=10)
    # print(ob)
    # b2 = BookImpl.add_book(ob)

    # b3 = BookImpl.remove_book(3)
    # print(b3)
    #
    # ob = Book(bid=2, bnm='mango',bpub='lenom',bath='batman',bprice=999,bqty=10)
    # b3 = BookImpl.modify_book(ob)
    # print(b3)

