# Generated by Django 4.0.5 on 2022-07-10 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('estimated_prep_time', models.IntegerField()),
                ('difficulty', models.FloatField(choices=[('1.0', 1.0), ('1.5', 1.5), ('2.0', 2.0), ('2.5', 2.5), ('3.0', 3.0), ('3.5', 3.5), ('4.0', 4.0), ('4.5', 4.5), ('5.0', 5.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StorageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('amount_type', models.CharField(choices=[('G', 'G'), ('KG', 'KG')], max_length=50)),
                ('due_date', models.DateTimeField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_app.ingredient')),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_app.storage')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('amount_type', models.CharField(choices=[('G', 'G'), ('KG', 'KG')], max_length=50)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_app.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_app.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('is_highlight', models.BooleanField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lunch_app.recipe')),
            ],
        ),
    ]
