# Generated by Django 2.0.3 on 2018-03-29 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_type', models.CharField(blank=True, choices=[('username', '用户密码认证'), ('email', '邮箱认证'), ('phone', '手机号认证')], max_length=256, null=True, verbose_name='认证类型')),
                ('token', models.CharField(blank=True, max_length=256, null=True, verbose_name='密码或者令牌')),
                ('checked', models.BooleanField(default=False, verbose_name='是否认证过')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户认证',
            },
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128, null=True, verbose_name='需求标题')),
                ('content', models.TextField(blank=True, null=True, verbose_name='需求说明')),
                ('dead_line', models.DateTimeField(blank=True, null=True, verbose_name='截至时间')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='upload/attachment/%Y/%m/%d', verbose_name='附件')),
                ('budget', models.IntegerField(blank=True, null=True, verbose_name='预算')),
            ],
            options={
                'verbose_name': '需求',
            },
        ),
        migrations.CreateModel(
            name='DemandType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='需求类型')),
            ],
            options={
                'verbose_name': '需求类型',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, max_length=128, null=True, verbose_name='昵称')),
                ('address', models.TextField(blank=True, null=True, verbose_name='住址')),
                ('sex', models.IntegerField(blank=True, choices=[(0, '男'), (1, '女')], null=True)),
                ('paymentpassword', models.CharField(blank=True, max_length=256, null=True, verbose_name='支付密码')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload/avatar/%Y/%m/%d', verbose_name='头像')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用户资料',
            },
        ),
        migrations.AddField(
            model_name='demand',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ne.DemandType', verbose_name='需求类型'),
        ),
        migrations.AddField(
            model_name='demand',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ne.Profile', verbose_name='发布者'),
        ),
        migrations.AddField(
            model_name='auth',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ne.Profile', verbose_name='认证用户'),
        ),
    ]
