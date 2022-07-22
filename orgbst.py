from time import perf_counter
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        return 

class bst:
    def __init__(self):
        self.head=None
        return   

    def insert(self,data):
        n=node(data)
        if self.head==None:
            self.head=n
            return
        else:
            x=self.head
            if x.data>data:
                if x.left==None:
                    x.left=n
                    return
                y=0
                while x:
                    if x.data>data:
                        if x.left==None:
                            y=0
                            break
                        x=x.left
                        y=0
                    else:
                        if x.right==None:
                            y=1
                            break
                        x=x.right
                        y=1
                if y==0:
                    x.left=n
                    return
                else:
                    x.right=n
                    return
            else:
                y=1
                if x.right==None:
                    x.right=n
                    return
                while x:
                    if x.data>data:
                        if x.left==None:
                            y=0
                            break
                        x=x.left
                        y=0
                    else:
                        if x.right==None:
                            y=1
                            break
                        x=x.right
                        y=1
                if y==0:
                    x.left=n
                    return
                else:
                    x.right=n
                    return 

    def delete(self,key):
        x=self.head
        if x.data==key:
            temp=x.right
            self.head=x.left
            del x
            x=self.head
            while x.right:
                x=x.right
            x.right=temp
        else:
            z=1
            x=self.head
            while x.data!=key :
                if x.data>key:
                    if x.left==None:
                        z=0
                        break
                    prev=x
                    x=x.left
                    y=0
                else:
                    if x.right==None:
                        z=0
                        break
                    prev=x
                    x=x.right
                    y=1
            if z==0:
                print("element not found to delete")
            else:
                if x.left==None and x.right==None:
                    if y==0:
                        prev.left=None
                    else:
                        prev.right=None
                    del x
                elif x.left==None:
                    if y==0:
                        prev.left=x.right
                        del x
                    else:
                        prev.right=x.right
                elif x.right==None:
                    if y==0:
                        prev.left=x.left
                    else:
                        prev.right=x.left
                else:
                    if y==0:
                        temp=x.right
                        z=x.left
                        del x
                        prev.left=z
                        while z.right:
                            z=z.right
                        z.right=temp                        
                    else:
                        temp=x.right
                        z=x.left
                        del x
                        prev.right=z
                        while z.right:
                            z=z.right
                        z.right=temp

    def search(self,key):
        x=self.head
        if x.data==key:
            print("element found")
        else:
            y=1
            x=self.head
            while x.data!=key:
                if x.data>key:
                    if x.left==None:
                        y=0
                        break
                    x=x.left
                else:
                    if x.right==None:
                        y=0
                        break
                    x=x.right
            if x.data==key:
                print("element found")
            if y==0:
                print("element not found")

    def inorder(self,n):
        if n:
            self.inorder(n.left)
            print(n.data,end=" ")
            self.inorder(n.right)

    def preorder(self,n):
        if n:
            print(n.data,end=" ")
            self.preorder(n.left)
            self.preorder(n.right)

    def postorder(self,n):
        if n:
            self.postorder(n.left)
            self.postorder(n.right)
            print(n.data,end=" ")
t1=perf_counter()           
t=bst()
t.insert(20)
t.insert(10)
t.insert(30)
t.insert(50)
t.insert(9)
t.insert(15)
t.insert(16)
t.insert(11)
t.insert(28)
t.insert(40)
t.insert(18)
t.insert(25)
t.delete(18)
t.search(18)
t.search(20)
t.search(50)
t.search(16)
t.search(80)
print("inorder:",end="")
t.inorder(t.head)
print()
print("preorder:",end="")
t.preorder(t.head)
print()
print("postorder:",end="")
t.postorder(t.head)
print()
t2=perf_counter()
print(t2-t1)