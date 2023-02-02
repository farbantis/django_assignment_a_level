# Generated by Django 4.1.5 on 2023-02-02 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
        ),
        migrations.CreateModel(
            name='CommentSpecial',
            fields=[
                ('comment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.comment')),
            ],
            bases=('blog.comment',),
        ),
        migrations.CreateModel(
            name='LikeToComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisLikeToComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DisLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='blog.author'),
        ),
    ]
