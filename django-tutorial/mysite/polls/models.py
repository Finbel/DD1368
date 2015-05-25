import datetime

# Importerar models fran django.db
from django.db import models
from django.utils import timezone

# Varje model representeras av en subclass till django.db.models.Model. 
# Varje model har ett antal klass-variabler, vardera representerar ett databas-falt i modellen.

# Varje falt representeras av en instans av Filed-klassen, t.ex. CharField for 
# karaktarer och DateTimeField for datum-tider

# Namnet pa varje Field-instans (e.g. question_text eller pub_date) ar faltets namn i maskinvanligt format.
# Du kommer att anvanda detta varde i din python-kod och din databas kommer anvanda det som kolumn-namn

# Du kan anvanda ett frivilligt forsta positionellt argument till ett falt for att designera ett mannisko-lasligt
# namn som kommer att anvandas i ett anta l introspektiva delar av Django och det dubblerar som dokumentation
# I detta fallet har vi endast get ett human readable namn till Question.pub_date. For alla andra falt kommer 
# det maskin-lasliga namnet att fungera.

# Vissa falt kraver argument. CharField tillexemep kraver att du ger en max-langd (max_length).
# Falt kan ocksa har valfria argument. Vi har t.ex. satt default av votes till 0.

# Vi har aven definierat en relation. Genom att anvanda ForeignKey. Detta berattar for Django att 
# varje Choice ar kopplat till en och endast en fraga. Django stodjer alla vanliga databas-relationer: 
# many-to-one, many-to-many och one-to-one

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
    	return self.question_text
    def was_published_recently(self):
    	return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_filed = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
    	return self.choice_text