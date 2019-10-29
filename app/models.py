from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, author, quote):
        self.author = author
        self.quote = quote



class User(UserMixin, db.Model):
    """ class modelling the users """

    __tablename__ = 'users'

    # create the columns
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship("Blog", backref="user1", lazy="dynamic")
    comment = db.relationship("Comments", backref="user2", lazy="dynamic")
    upvotes = db.relationship("UpVote", backref="blog2", lazy="dynamic")
    downpvotes = db.relationship("DownVote", backref="blog2", lazy="dynamic")
    # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'
   
# category model2
class BlogCategory(db.Model):

    __tablename__ = 'categories'

    # table columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    # save blogs
    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = BlogCategory.query.all()
        return categories


# blogs class
class Blog(db.Model):
    """ List of blogs in each category """

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="blog1", lazy="dynamic")
    # upvote = db.relationship("Upvote", backref="blog2", lazy="dynamic")
    # downpvote = db.relationship("DownVote", backref="blog2", lazy="dynamic")

    def save_blog(self):
        ''' Save the blocks '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_(cls):
        Blog.all_blogs.clear()

    # display blogs

    def get_blogs(id):
        blogs = Blog.query.filter_by(category_id=id).all()
        return blogs


# comments
class Comments(db.Model):
    '''User comment model for each blog '''

    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    opinion = db.Column(db.String(255))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        '''
        Save the Comments/comments per blog
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.time_posted.desc()).filter_by(blogs_id=id).all()
        return comment

# votes


class UpVote(db.Model):
    __tablename__ = 'upvotes'

    id = db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_votes(cls,id):
        upvote = UpVote.query.filter_by(blog_id=id).all()
        return upvote
    
    def __repr__(self):
        return f'{self.id_user}:{self.blog_id}'

class DownVote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    id_user = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer)

    def save_vote(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_downvotes(cls,id):
        downvote = DownVote.query.filter_by(blog_id=id).all()
        return downvote
        
    def __repr__(self):
        return f'{self.id_user}:{self.blog_id}'
class Quotes():
    """
    class to display random quotes
    """      

    def __init__(self,author,quote,permalink):
        self.author = author
        self.quote = quote
        self.permalink = permalink  
