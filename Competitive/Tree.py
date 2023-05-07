class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self    # The parent of the child will be the class instance which is self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level()
        prefix = spaces + '|__' if self.parent else ''
        print(prefix + self.data)
        for child in self.children:
            child.print_tree()        # Recursive as child is also the object of TreeNode class

def build_product_tree():
    root = TreeNode('Electronics')
    laptop = TreeNode('Laptops')
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('Iphone'))
    cellphone.add_child(TreeNode('Pixel'))
    cellphone.add_child(TreeNode('Samsung'))

    tv = TreeNode('Television')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('Sony'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()

if __name__ == '__main__':
    build_product_tree()
