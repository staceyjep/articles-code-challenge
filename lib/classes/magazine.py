
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def add_article(self, article):
        """Adds an article to the magazine."""
        if not isinstance(article, Article):
            raise ValueError("Can only add instances of Article.")
        self._articles.append(article)

    def articles(self):
        """Returns a list of articles for this magazine."""
        return self._articles

    def contributors(self):
        """Returns a list of unique authors (contributors) for this magazine."""
        return list({article.author for article in self._articles})

    def article_titles(self):
        """Returns list of titles of all articles in this magazine."""
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        """Returns authors who have written more than 2 articles for this magazine."""
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None  # Return None if no contributors

    @staticmethod
    def top_publisher():
        """Returns the magazine with the most articles."""
        if not Magazine.all:
            return None
        # Find the magazine with the most articles
        return max(Magazine.all, key=lambda mag: len(mag.articles()), default=None)
