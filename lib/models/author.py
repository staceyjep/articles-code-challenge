class Author:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if hasattr(self,"name"):AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name,str):
                if len(new_name):
                    self._name=new_name
                else:ValueError("Name must be longer than 0 charachters")
            else:TypeError("Name must be a string")
    
    def articles(self):
        return [article for article in Article.all if self==article.author]
    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)


    def topic_areas(self):
        topic_areas=list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:return None