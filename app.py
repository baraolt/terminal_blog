from database import Database
from menu import Menu
from models.blog import Blog

Database.initialize()

menu = Menu()
menu.run_menu()

# post = Post("Post1 title", "Post1 content", "Greg")

# post = Post(blog_id="123",
#             title="My first post",
#             content="This is my first post, curious to see how it comes out!",
#             author="Greg")
#
# post.save_to_mongo()
# Enter db.posts.find({}).pretty() to terminal to see

# post = Post.from_mongo('338cfbd1922b4d0c8cb5eccc9457159b')
# print(post)

# post = Post.from_blog('123')
# print(post)
#
# if more than one has same blog id:
# posts = Post.from_blog('123')
# for post in posts:
#     print(post)

# blog = Blog(author="Greg",
#             title="Greg's blog",
#             description="Some description")
#
# blog.new_post()
#
# blog.save_to_mongo()
#
# from_database = Blog.from_mongo(blog.id)
#
# print(blog.get_posts()) # same as Post.from_blog(id)

