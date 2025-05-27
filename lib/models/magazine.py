class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str):
            if 2<=len(new_name)<=16:
                self._name=new_name
            else:ValueError("Name must be between 2 and 16 charachters long")
        else:TypeError("Name must be a string")
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,new_category):
        if isinstance(new_category,str):
            if len(new_category):
                self._category=new_category
            else:ValueError("Category must have a charachter or more")
        else:TypeError("Category must be a string")
    def articles(self):
        return [article for article in Article.all if self==article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles=[magazine.title for magazine in self.articles()]
        if article_titles:
            return article_titles
        else:return None
    def contributing_authors(self):
        authors={}
        list_of_authors=[]
        for article in self.articles():
            if article.author in authors:
                authors[article.author] +=1
            else:authors[article.author]=1
        for author in authors:
            if authors[author]>=2:
                list_of_authors.append(author)
        if(list_of_authors):
            return list_of_authors
        else:return None