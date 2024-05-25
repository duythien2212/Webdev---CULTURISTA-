from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100,primary_key=True, default=None)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='none@gm.uit.edu.vn')
    age = models.IntegerField()
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other')
    )
    gender = models.IntegerField(choices=GENDER_CHOICES)
    role = models.ForeignKey('Role', on_delete=models.CASCADE, default=0)
    room = 0
    country = models.ForeignKey('Country', on_delete=models.CASCADE, default='VIE')

    def __str__(self):
        return str(self.username)

class Role(models.Model):
    role_id = models.IntegerField(primary_key=True, default=0)
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name

class Country(models.Model):
    country_code = models.CharField(max_length=5, primary_key=True, default="VIE")
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_code

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True, default=0)
    question_type = models.CharField(max_length=100)
    question_content = models.CharField(max_length=255)
    question_material = models.ForeignKey('Assets', on_delete=models.CASCADE,default=0)
    answer = models.CharField(max_length=255)
    score_value = models.FloatField()
    pack_name = models.ForeignKey('Pack', on_delete=models.CASCADE, default=None)
 
    def __str__(self):
        return self.question_content

class Room(models.Model):
    room_id = models.IntegerField(primary_key=True, default=0)
    round1_pack = models.ForeignKey('Pack', on_delete=models.CASCADE, default=None, related_name='round1_packs')
    round2_pack = models.ForeignKey('Pack', on_delete=models.CASCADE, default=None, related_name='round2_packs')
    round3_pack = models.ForeignKey('Pack', on_delete=models.CASCADE, default=None, related_name='round3_packs')
    number_of_player = 0
    is_full = models.BooleanField()

    def __int__(self):
        return (self.room_id)

class Assets(models.Model):
    assets_id = models.IntegerField(primary_key=True, default=0)
    assets_name = models.CharField(max_length=100)
    assets_type = models.CharField(max_length=100)
    assets_url = models.CharField(max_length=255)

    def __str__(self):
        return self.assets_name

class Forum(models.Model):
    content_id = models.IntegerField(primary_key=True, default=0)
    title = models.CharField(max_length=100)
    content = models.TextField()
    number_of_replies = 0
    tag = models.CharField(max_length=100)
    user_created_name = models.ForeignKey('User', on_delete=models.CASCADE, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True, default=0)
    user_name = models.ForeignKey('User', on_delete=models.CASCADE, default=0)
    comment_content = models.TextField()
    content_id = models.ForeignKey('Forum', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.comment_content

class Pack(models.Model):
    pack_name = models.CharField(primary_key=True, default=None, max_length=100)

    def __str__(self):
        return self.pack_name
