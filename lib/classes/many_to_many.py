class Article:
    # Class-level list to track all articles
    all = [] 

    # Constructor to initialize an article with author, magazine, and title
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    #Should not be able to change title after instantiation
    @property
    def title(self):
        return self._
    
    # Title must be a string between 5 and 50 characters and of type str
    @title.setter
    def title(self, value):
        if hasattr(self, '_title'):
            raise AttributeError("Title is immutable after instantiation")
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author class")
        self._author = value

    @property
    def magazine(self): 
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class")
        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Author name is immutable after instantiation")
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = value.strip()

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine class")
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list(set(mag.category for mag in mags))
    

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        value = value.strip()
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine category must be a string")
        value = value.strip()
        if len(value) == 0:
            raise ValueError("Magazine category cannot be empty")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [article.title for article in arts]

    def contributing_authors(self):
        arts = self.articles()
        if not arts:
            return None
        from collections import Counter
        author_counts = Counter(article.author for article in arts)
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
    
    #Instance method to get the magazine's category
    def get_category(self):
        return self.category
     #instance Aricle method to get the magazine's name
    def get_name(self):
        return self.name
    

author1 = Author("Edward Kamande")
author2 = Author("Mary Wanjiku")
magazine1 = Magazine("Vogue", "Fashion")
article1 = Article(author1, magazine1, "How to wear a mtush with style")
#Instance to add article
article2 = author1.add_article(magazine1, "Dating life in Nairobi")
print(article2)
print(article1.author.name)
print(article1.magazine.name)
print(article1.magazine.category)
#Topic areas for author1
print(author1.topic_areas())
# Instance method to get magazine category
print(article1.magazine.get_category())
# Instance method to get magazine name
print(article1.magazine.get_name())
#Instance method to get contributors
print(magazine1.contributors())
