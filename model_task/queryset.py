from django.db.models import Count
from models import Comment, Document, Project, User

# Applying filter and startswith lookup
data = Project.objects.values()
mydata = data.filter(title__startswith="A").values()

# Output:
print(mydata)
# <QuerySet [{'id': 1, 'title': 'Airbnb', 'description': 'test', 'start_date': datetime.date(2024, 8, 7), 'end_date': datetime.date(2024, 8, 9)}]>

# Getting objects from Document model
doc_data = Document.objects

# Output:
print(doc_data)
# model_task.Document.objects

# Applying filter with greater than or equal to lookup
doc_data = doc_data.filter(version__gte=4).values()

# Output:
print(doc_data)
# <QuerySet [{'id': 3, 'name': 'SRE1', 'description': 'hjkhlj', 'file': '', 'version': 5.0, 'project_id': 3}, {'id': 4, 'name': 'SRe5', 'description': 'fgfgh', 'file': '', 'version': 4.0, 'project_id': 3}]>

# Applying filter with in lookup
doc_data = doc_data.filter(version__in=[1, 4, 5]).values()

# Output:
print(doc_data)
# <QuerySet [{'id': 3, 'name': 'SRE1', 'description': 'hjkhlj', 'file': '', 'version': 5.0, 'project_id': 3}, {'id': 4, 'name': 'SRe5', 'description': 'fgfgh', 'file': '', 'version': 4.0, 'project_id': 3}]>

# Applying filter with in lookup
doc_data = doc_data.filter(version__in=[1, 4]).values()

# Output:
print(doc_data)
# <QuerySet [{'id': 4, 'name': 'SRe5', 'description': 'fgfgh', 'file': '', 'version': 4.0, 'project_id': 3}]>

# Using exclude keyword
comnt_data = Comment.objects.exclude(author=2).values()

# Output:
print(comnt_data)
# <QuerySet [{'id': 2, 'text': 'fggfgffgghww', 'author_id': 3, 'created_at': datetime.datetime(2024, 8, 8, 10, 44, 45, tzinfo=<UTC>), 'task_id': 3, 'project_id': 3},
#             {'id': 3, 'text': 'wewe', 'author_id': 1, 'created_at': datetime.datetime(2024, 8, 8, 10, 44, 57, tzinfo=<UTC>), 'task_id': 3, 'project_id': 1},
#             {'id': 4, 'text': 'weryuu', 'author_id': 4, 'created_at': datetime.datetime(2024, 8, 8, 10, 45, 8, tzinfo=<UTC>), 'task_id': 3, 'project_id': 2}]>

# Using exclude with in lookup
comnt_data = Comment.objects.exclude(author__in=[3, 4]).values()

# Output:
print(comnt_data)
# <QuerySet [{'id': 1, 'text': 'fghfgddffgh', 'author_id': 2, 'created_at': datetime.datetime(2024, 8, 8, 10, 44, 27, tzinfo=<UTC>), 'task_id': 2, 'project_id': 2},
#             {'id': 3, 'text': 'wewe', 'author_id': 1, 'created_at': datetime.datetime(2024, 8, 8, 10, 44, 57, tzinfo=<UTC>), 'task_id': 3, 'project_id': 1}]>

# Using annotate keyword example 1
pr_data = Project.objects.annotate(Count("title")).values()

# Output:
print(pr_data)
# <QuerySet [{'id': 1, 'title': 'Airbnb', 'description': 'test', 'start_date': datetime.date(2024, 8, 7), 'end_date': datetime.date(2024, 8, 9), 'title__count': 1},
#             {'id': 2, 'title': 'instagram', 'description': 'shb n uifd hjhs jnb jfdn gf', 'start_date': datetime.date(2024, 7, 16), 'end_date': datetime.date(2024, 8, 15), 'title__count': 1},
#             {'id': 3, 'title': 'youtube', 'description': 'dfcgvhbjnkm fghjkl; ghjkl;', 'start_date': datetime.date(2024, 7, 1), 'end_date': datetime.date(2024, 8, 19), 'title__count': 1},
#             {'id': 4, 'title': 'spotify', 'description': 'fda s g sgd bfbd fd fdg dfg', 'start_date': datetime.date(2024, 6, 3), 'end_date': datetime.date(2024, 10, 3), 'title__count': 1}]>

# Using annotate keyword example 2
pr_data = Project.objects.annotate(Count("title")).values()

# Output:
print(pr_data)
# <QuerySet [{'id': 1, 'title': 'Airbnb', 'description': 'test', 'start_date': datetime.date(2024, 8, 7), 'end_date': datetime.date(2024, 8, 9), 'title__count': 1},
#             {'id': 2, 'title': 'instagram', 'description': 'shb n uifd hjhs jnb jfdn gf', 'start_date': datetime.date(2024, 7, 16), 'end_date': datetime.date(2024, 8, 15), 'title__count': 1},
#             {'id': 3, 'title': 'youtube', 'description': 'dfcgvhbjnkm fghjkl; ghjkl;', 'start_date': datetime.date(2024, 7, 1), 'end_date': datetime.date(2024, 8, 19), 'title__count': 1},
#             {'id': 4, 'title': 'spotify', 'description': 'fda s g sgd bfbd fd fdg dfg', 'start_date': datetime.date(2024, 6, 3), 'end_date': datetime.date(2024, 10, 3), 'title__count': 1},
#             {'id': 5, 'title': 'Airbnb', 'description': 'dsfdss', 'start_date': datetime.date(2024, 6, 4), 'end_date': datetime.date(2024, 12, 19), 'title__count': 1}]>

# Using OrderBy keyword example 1
pr_data = Project.objects.order_by("title")

# Output:
print(pr_data)
# <QuerySet [<Project: Project object (1)>, <Project: Project object (5)>, <Project: Project object (2)>, <Project: Project object (4)>, <Project: Project object (3)>]>

# Using OrderBy keyword example 2
from django.db.models.functions import Lower

pr_data = Project.objects.order_by(Lower("title").desc())

# Output:
print(pr_data)
# <QuerySet [<Project: Project object (3)>, <Project: Project object (4)>, <Project: Project object (2)>, <Project: Project object (1)>, <Project: Project object (5)>]>

# Checking more on output
print(pr_data[0])
# Project object (3)

# Checking more on output
print(pr_data[0].title)
# youtube

# Converting the objects in value_list on the basis of author
comnt_data = Comment.objects.values_list("author")

# Output:
print(comnt_data)
# <QuerySet [(1,), (2,), (3,), (4,)]>

# Converting the objects in value_list
comnt_data = Comment.objects.values_list()

# Output:
print(comnt_data)
# <QuerySet [(1, 'fghfgddffgh', 2, datetime.datetime(2024, 8, 8, 10, 44, 27, tzinfo=<UTC>), 2, 2),
#             (2, 'fggfgffgghww', 3, datetime.datetime(2024, 8, 8, 10, 44, 45, tzinfo=<UTC>), 3, 3),
#             (3, 'wewe', 1, datetime.datetime(2024, 8, 8, 10, 44, 57, tzinfo=<UTC>), 3, 1),
#             (4, 'weryuu', 4, datetime.datetime(2024, 8, 8, 10, 45, 8, tzinfo=<UTC>), 3, 2)]>

# Using union and intersection
q1 = User.objects.filter(username="bilu")
q2 = User.objects.filter(username="khabib")

# Output: Union of q1 and q2
print(q1.union(q1, q2))
# <QuerySet [<User: bilu@gmail.com>, <User: khabib@gmail.com>]>

# Output: Intersection of q1 and q2
print(q1.intersection(q1, q2))
# <QuerySet []>

# Using select_related
new_data = Comment.objects.select_related("project").get(project=1)

# Output:
print(new_data)
# Comment object (3)

# Using prefetch_related
member = Project.objects.prefetch_related("team_members")

# Output:
print(member)
# <QuerySet [<Project: Project object (1)>, <Project: Project object (2)>, <Project: Project object (3)>, <Project: Project object (4)>, <Project: Project object (5)>]>

# Create:
user = User(username="haha45", email="haha4@gmail.com", password="123")

# Output:
print(user)
# haha4@gmail.com

# Using bulk_create
users = User.objects.bulk_create(
    [
        User(username="bye", email="bye4@gmail.com", password="123"),
        User(username="hi", email="hi4@gmail.com", password="123"),
    ]
)

# Output:
print(users)
# [<User: bye4@gmail.com>, <User: hi4@gmail.com>]

# Update:
usrname = [User.objects.create(username="sae"), User.objects.create(username="ok")]

# Using exists()
q2 = User.objects.filter(username="khabib")

# Output:
print("value exists") if q2.exists() else print("nothing")
# value exists
