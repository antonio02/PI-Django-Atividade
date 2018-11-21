from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField()
    closed = models.BooleanField(default=False)
    pub_date = models.DateField()

    def change_state(self):
        if self.closed:
            self.closed = False
        else:
            self.closed = True
        self.save()

    def  __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE, null=True)
    choice_text = models.TextField()
    votes = models.IntegerField()

    def up_vote(self):
        self.votes += 1
        self.save()

    def remove_from_question(self):
        self.question = None
        self.save()

    def  __str__(self):
        return self.choice_text

