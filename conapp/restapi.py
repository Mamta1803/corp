from .booinfo import Book


BASE_URL = "http://127.0.0.1:8000/books/"


def coversation(bookjson):
    return Book(bid =bookjson.get("id"),
                    bnm=bookjson.get("book_name"),
                    bpub=bookjson.get("book_pub"),
                    bath=bookjson.get("book_auth"),
                    bprice=bookjson.get("book_price"),
                    bqty=bookjson.get("book_qty"))


def deserialiser(bookjson,code):
    booklist = []
    if code == 'S':
        return coversation(bookjson)
    if code == 'M':
        for bookj in bookjson:
            booklist.append(coversation(bookj))
        return booklist

