# Generated by Django 3.0.8 on 2020-07-27 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateDevice', models.IntegerField(choices=[(0, '在库'), (1, '维修中'), (2, '项目使用中'), (3, '淘汰')], default=1)),
                ('name', models.CharField(max_length=300, verbose_name='设备名称')),
                ('type', models.CharField(max_length=300, verbose_name='设备型号')),
                ('certificate', models.FileField(blank=True, upload_to='', verbose_name='证书文件')),
                ('datePurchase', models.DateTimeField(blank=True, null=True, verbose_name='购买日期')),
            ],
            options={
                'ordering': ['-name', '-datePurchase'],
            },
        ),
        migrations.CreateModel(
            name='DeviceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='设备类别')),
            ],
        ),
        migrations.CreateModel(
            name='Vender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='厂家名称')),
                ('address', models.CharField(blank=True, max_length=1000, verbose_name='地址')),
                ('contact', models.CharField(blank=True, max_length=300, verbose_name='联系人')),
                ('tell', models.CharField(blank=True, max_length=100, verbose_name='联系电话/邮箱')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='项目名称')),
                ('startdate', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('enddate', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('remark', models.CharField(blank=True, max_length=5000, verbose_name='备注')),
                ('adminmark', models.CharField(blank=True, max_length=5000, verbose_name='添加备注')),
                ('devices', models.ManyToManyField(related_name='projects', to='Device.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='组件名称')),
                ('partId', models.CharField(blank=True, max_length=500, verbose_name='编号')),
                ('main_device', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Parts', to='Device.Device')),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='vender',
            field=models.ManyToManyField(blank=True, related_name='devices', to='Device.Vender'),
        ),
    ]
