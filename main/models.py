from django.db import models

BLACK_USER_LIST = ['Vasya', 'Petya']

# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()
    when = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{} at {}'.format(self.header, self.when)

class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=20)

	# def __unicode__(self, username, password)

def auth(login, password):
	if login in BLACK_USER_LIST:
		return 'Sorry:('
	users = User.objects.filter(username = login)
	if len(users) == 0:
		return 'I do not know such user'
	else:
		user = users[0]
		print 'Hello {}'.format(user.username)

	if user.password == password:
		return 'Authentificated succesfully, lol'
	else:
		return 'Wrong password'
