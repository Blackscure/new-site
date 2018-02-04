import uuid
from ..common.database import Database

class user(object):
    def __init__(self,author, title,  _id=None):
        self.email = email
        self.password = password
        self._id = uuid4().hex if _id is None else _id
        
    @classmethod
    def get_by_email(cls, email):
        data = Database.find_("user", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one("user", {"_id": _id})
        if data is not None:
            return cls(**data)
        

    def login_valid(email, password):
        user = user.get_by_email(email)
        if user is None:
            #user dosen't exsist, so we can create it
            new_user = user(email, password)
            new_user.save_to_mongo()
            return True
        else:
            #user exixts :(
            return False

    @staticmethod
    def login(user_email): 
        #login_valid has already been called
        session['email'] = user_email
        
    @staticmethod
    def logout(user_email):
        session['email'] = None

  
    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        #author, title, description, author_id
        blog = Blog(author=self.email,
                    title=title,
                    description=description,
                    author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content, date=datetime.datetime.utcnow()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                     content=content,
                      date=date)

    def json(self):
        return {
            "email": self.email,
            "_id": self._id,
            "password": self.pasword
            }

    def save_to_mongo(self):
        Database.insert("users", self.json())
