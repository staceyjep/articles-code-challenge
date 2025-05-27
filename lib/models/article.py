class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,new_title):
        if hasattr(self,"title"):AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title,str):
                if 5<=len(new_title)<=50:
                    self._title=new_title
                else:ValueError("Title must be between 5 and 50 characheters")
            else:TypeError("Title must be a string")
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:TypeError("Author must be an instance of Author")
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self,new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:TypeError("Magazine must be an instance of Magazine")
    
