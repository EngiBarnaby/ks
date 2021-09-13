# Generated by Django 3.2.7 on 2021-09-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(choices=[('n.', 'NOUN'), ('pro.', 'PRONOUN'), ('v.', 'VERB'), ('adj.', 'ADJECTIVE'), ('adv.', 'ADVERB'), ('pre.', 'PREPOSITION'), ('con.', 'CONJUNCTION'), ('int.', 'INTERJECTION')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]