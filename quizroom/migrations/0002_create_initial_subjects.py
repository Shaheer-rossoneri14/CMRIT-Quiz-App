

from django.db import migrations


def create_subjects(apps, schema_editor):
    Subject = apps.get_model('quizroom', 'Subject')
    Subject.objects.create(name='Physics', color='#343a40')
    Subject.objects.create(name='Chemistry', color='#343a40')
    Subject.objects.create(name='Math', color='#343a40')
    Subject.objects.create(name='Electrical', color='#343a40')
    Subject.objects.create(name='Electronics', color='#343a40')
    Subject.objects.create(name='Mechanical', color='#343a40')
    Subject.objects.create(name='Civil', color='#343a40')
    Subject.objects.create(name='IoT', color='#343a40')
    Subject.objects.create(name='ML/AI', color='#343a40')
    Subject.objects.create(name='Programming', color='#343a40')
    Subject.objects.create(name='History', color='#343a40')
    Subject.objects.create(name='GK', color='#343a40')
    Subject.objects.create(name='Web Development', color='#343a40')
    Subject.objects.create(name='Litrature', color='#343a40')




class Migration(migrations.Migration):

    dependencies = [
        ('quizroom', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_subjects),
    ]
