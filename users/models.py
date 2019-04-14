from django.db import models
from django.contrib.auth.models import User

class ProfileManager(models.Manager):
    def update_preferences(self, pref, gen):
        self.preferences = pref
        self.genre = gen        

    def update_genre(self, instance):
        return self.genre

    def update_by_id(self, user_id, pref, gen):
        self.preferences = pref
        self.genre = gen  
        qs = self.get_queryset().filter(uid=user_id, preferences=self.preferences, genre=self.genre)
        return qs

class Profile(models.Model):
    PREFERENCES = (
        ('Arts & Theatre', 'Arts & Theatre'),
        ('Film', 'Film'),
        ('Miscellaneous', 'Miscellaneous'),
        ('Music', 'Music'),
        ('Sports', 'Sports'), 
        ('Undefined', 'Undefined'), 
        ('Donation', 'Donation'), 
        ('Event Style', 'Event Style'), 
        ('Group', 'Group'), 
        ('Individual', 'Individual'), 
        ('Merchandise', 'Merchandise'), 
        ('Nonticket' ,'Nonticket'), 
        ('Parking', 'Parking'), 
        ('Transportation', 'Transportation'), 
        ('Upsell', 'Upsell'), 
        ('Venue Based', 'Venue Based')
    )
    GENRE = (
        ('KnvZfZ7vAee','R&B'),
        ('KnvZfZ7vAv1', 'Hip-Hop/Rap'),
        ('KnvZfZ7vAe1', 'Comedy'),
        ('KnvZfZ7v7nJ', 'Classical'),
        ('KnvZfZ7vAvE', 'Jazz'),
        ('KnvZfZ7vAk1', 'Foreign'),
        ('KnvZfZ7vAvF', 'Dance/Electronic'),
        ('KnvZfZ7vAkA', 'Comedy'),
        ('KnvZfZ7vAkd', 'Animation'),
        ('KnvZfZ7vAkJ', 'Music'),
        ('KnvZfZ7vAka', 'Miscellaneous'),
        ('KnvZfZ7vAk', 'Family'),
        ('KnvZfZ7v7ld', 'Miscellaneous Theatre'),
        ('KnvZfZ7v7l1', 'Theatre')
    )
    uid = models.CharField(max_length=100, unique=True, default="null")
    preferences = models.CharField(max_length=120, choices=PREFERENCES)  #can be used for multiople choices - alternative is ChoiceField - for single choice.
    genre = models.CharField(max_length=120, choices=GENRE)
    objects = ProfileManager()

    def update_genre(self, instance):
        self.genre = instance
        return self.genre