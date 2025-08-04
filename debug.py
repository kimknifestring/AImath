class HashTable():
    def __init__(self,size):
        self.table=[None]*size
        self.size=size
    def hash_function(self,name):
        # sum=0
        # #이름의 유니코드 값을 활용한 해시 함수
        # for i in name:
        #     x=ord(i)
        #     sum+=x
        # idx=sum%self.size
        # return idx
        return sum(ord(c)*(i+1) for i,c in enumerate(name))%self.size
    
    def insert(self,name):
        index=self.hash_function(name)
        print(index)
    
    # def display(self):
        

hash_table=HashTable(10)
hash_table.insert('메이킷')
hash_table.insert('우진')
hash_table.insert('시은')
hash_table.insert('형우')

hash_table.display()