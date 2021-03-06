# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class City(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    country_team = models.CharField(db_column='Country_Team', max_length=255)  # Field name made lowercase.
    noc = models.CharField(db_column='NOC', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Events(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    events = models.CharField(db_column='Events', max_length=255)  # Field name made lowercase.
    sport = models.ForeignKey('Sport', models.DO_NOTHING, db_column='Sport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'events'


class Games(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    year = models.IntegerField(db_column='Year')  # Field name made lowercase.
    season = models.CharField(db_column='Season', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'games'


class GamesCity(models.Model):
    game = models.OneToOneField(Games, models.DO_NOTHING, db_column='Game_ID', primary_key=True)  # Field name made lowercase.
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='City_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'games_city'
        unique_together = (('game', 'city'),)


class Medals(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    medalname = models.CharField(db_column='MedalName', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medals'


class OlympicEvent(models.Model):
    olympics = models.OneToOneField('Olympics', models.DO_NOTHING, db_column='Olympics_ID', primary_key=True)  # Field name made lowercase.
    medal = models.ForeignKey(Medals, models.DO_NOTHING, db_column='Medal_ID')  # Field name made lowercase.
    event = models.ForeignKey(Events, models.DO_NOTHING, db_column='Event_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'olympic_event'
        unique_together = (('olympics', 'medal', 'event'),)


class Olympics(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    game = models.ForeignKey(Games, models.DO_NOTHING, db_column='Game_Id', blank=True, null=True)  # Field name made lowercase.
    player = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='Country_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'olympics'


class Person(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=5)  # Field name made lowercase.
    height = models.CharField(db_column='Height', max_length=10, blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class PersonCountry(models.Model):
    country = models.OneToOneField(Country, models.DO_NOTHING, db_column='Country_ID', primary_key=True)  # Field name made lowercase.
    person = models.ForeignKey(Person, models.DO_NOTHING, db_column='Person_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_country'
        unique_together = (('country', 'person'),)


class Sport(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sport'
