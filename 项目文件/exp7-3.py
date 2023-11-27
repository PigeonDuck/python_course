# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection =collection
        self.items_per_page=items_per_page
        count = 0
        self.str_len = []
        for i in range(0,len(self.collection)):
            if count <= self.items_per_page:   
               count+=1
            if count == self.items_per_page:
               self.str_len.append(count)
               count=0
            if i == len(self.collection)-1:
               self.str_len.append(count)
        

    # returns the number of items within the entire collection
    def item_count(self):
        length=len(self.collection)
        return length

    # returns the number of pages
    def page_count(self):
        page_count = len(self.str_len)
        return page_count
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):

        if page_index > self.page_count()-1 or page_index < 0:  #2  1
           return -1
        #分配页数
        return self.str_len[page_index]
            
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index<0:
            return -1
        if item_index > len(self.collection)-1:
            return -1
        if item_index == self.items_per_page-1 :
            return 0
        return item_index//self.items_per_page
        

helper = PaginationHelper(['a','b','c','d','e','f','a','b','c','d','e','f','a','b','c','d','e','f','a','b','c','d','e','f'], 10)
# print(helper.page_item_count(0))  # should == 4
# print(helper.page_item_count(1)) # last page - should == 2
# print(helper.page_item_count(2)) # should == -1 since the page is invalid
# str_len=[]
# collection=['a','b','c','d','e','f']
# items_per_page = 4 
# count=0
# print(len(collection))
# for i in range(0,len(collection)):
#     if count <= items_per_page:   
#        count+=1
#     if count == items_per_page:
#        str_len.append(count)
#        count=0
#     if i == len(collection)-1:
#        str_len.append(count)
# page_index takes an item index and returns the page that it belongs on


# page_index takes an item index and returns the page that it belongs on
# print(helper.page_index(5)) # should == 1 (zero based index)

# print(helper.page_index(2)) # should == 0
# print(helper.page_index(20)) # should == -1
# print(helper.page_index(-10)) # should == -1 because negative indexes are invalid\
print(helper.page_index(5))

print(helper.page_item_count(19))
print(helper.page_index(10))
print(helper.page_count())