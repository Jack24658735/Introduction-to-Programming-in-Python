class Person:
    def __init__(self, name):
        self._name = name
        self._children = []
        self._mother = None
        self._tree = []
        self._aunts = []
        self._sisters = []
    def __repr__(self):
        return f"Person('{self._name}')"
    
    @property
    def name(self):
        return self._name

    @property
    def children(self):
        return self._children
 
    def add_children(self, *children):
        for child in children:
            self._children.append(Person(child))  #construct person list
             
        for PersonObject in self._children:
            PersonObject._mother = self
            #remember not to create a new object
    @property
    def mother(self):
        return self._mother
    
    @property
    def sisters(self):
        for sis in self.mother.children:
            if sis.name != self._name:
                self._sisters.append(sis)
        return self._sisters
    @property
    def aunts(self):
        self._aunts = self.mother.sisters
        return self._aunts 
    
    @property
    def grandmother(self):
        return self.mother.mother

    @property
    def grandchildren(self):
        grandchild = []
        for daughter in self.children:
            for grandchild in daughter.children:
                grandchild.append(grandchild)
        return grandchild
    
    @property
    def family_tree(self):
        #using inner function so that 
        #it can execute recursion without doing the method
        def rec_tree(PersonObject):
            descendant_tree = {}
            ans_tree = {}
            if len(PersonObject.children) == 0: #base case
                ans_tree[PersonObject.name] = descendant_tree
                return ans_tree
            else:       #recursive case
                for item in PersonObject.children:
                    tmp_tree = rec_tree(item)   #keep recursion
                    descendant_tree[item.name] = tmp_tree[item.name]
                ans_tree[PersonObject.name] = descendant_tree
                return ans_tree
        return rec_tree(self)

if __name__ == '__main__':
    p = Person('Wilma')
    p.add_children('Mary', 'Ann', 'Jill', 'Jane')
    mary, ann, jill, jane = p.children
    mary.add_children('Lynn', 'Cindy')
    lynn, cindy = mary.children
    jill.add_children('Kate')
    print(p.family_tree)
