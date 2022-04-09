# Generated by Django 4.0.3 on 2022-04-09 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0003_promissory'),
    ]

    operations = [
        migrations.CreateModel(
            name='internship_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('fee', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='internship',
            name='amount',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='internship',
            name='balence',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='internship',
            name='complete_status',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='internship',
            name='pay_date',
            field=models.DateField(default=''),
        ),
        migrations.AddField(
            model_name='internship',
            name='total_fee',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='internship',
            name='total_pay',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='internship',
            name='verify_status',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='previousteam',
            name='progress',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='trainer_level',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.CreateModel(
            name='internship_paydata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('internship_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internship_user', to='base_app.internship')),
            ],
        ),
        migrations.AddField(
            model_name='internship',
            name='internshiptype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='internship_type', to='base_app.internship_type'),
        ),
    ]