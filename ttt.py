for i in range(1,10):
    print(f'''
class key{i}(Command):
    def __init__(self,nd):
        super().__init__(locals())
        self.time=nd
    def main(self):
        if Key.key{i}!="" and int(runearrow.monster_())>=1:
            press(Key.key{i}, 1, nd=self.time)
''')
