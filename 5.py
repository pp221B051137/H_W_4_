class Wordplay:
    def __init__(self,spisok):
        # self.spisok = spisok
        # sp = list(self.spisok)
        sp =list(spisok)
        self.sp = sp
    def words_with_lenght(self,leng):
        for one in self.sp:
            if len(one) == int(leng):
                return one
    def starts_with(self,s):
        for one in self.sp:
            if one[0] == s:
                return one
    def ends_with(self,s):
        a = []
        for one in self.sp:
            if one[len(one)-1] == s:
                a.append(one)
                return a
    def  palindromes(self):
        for one in self.sp:
            if one == one[::-1]:
                return one

spisok = input().split()
wordplay = Wordplay(spisok)
print("1",wordplay.ends_with("r"))
print("2",wordplay.starts_with("s"))
print("3",wordplay.words_with_lenght("5"))
print("4", wordplay.palindromes())