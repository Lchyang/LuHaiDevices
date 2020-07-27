from random import choices

from django.db import models
from account.models import Account


# Create your models here.

class DeviceCategory(models.Model):  # 如：软件狗、GPS, 可以后续增加设备类型
    name = models.CharField(max_length=300, verbose_name='设备类别')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '设备类别'


class Vender(models.Model):
    '''厂家
    name: 厂家名称
    address： 厂家地址
    contact： 联系人
    tell: 联系电话
    '''
    name = models.CharField(max_length=500, verbose_name='厂家名称')
    address = models.CharField(max_length=1000, verbose_name='地址', blank=True)
    contact = models.CharField(max_length=300, verbose_name='联系人', blank=True)
    tell = models.CharField(max_length=100, verbose_name='联系电话/邮箱', blank=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = '厂家'
        verbose_name_plural = verbose_name



class Device(models.Model):
    '''设备
    设备的状态码：在库、使用、维修、淘汰
    设备名称：如多波束7125
    '''
    choices = (
                  (0, '在库'),
                  (1, '维修中'),
                  (2, '项目使用中'),
                  (3, '淘汰'),)
    stateDevice = models.IntegerField(choices=choices, default=1)
    name = models.CharField(max_length=300, verbose_name='设备名称')
    type = models.CharField(max_length=300, verbose_name='设备型号')
    certificate = models.FileField(verbose_name='证书文件', blank=True)
    datePurchase = models.DateTimeField(verbose_name='购买日期', blank=True, null=True)
    vender = models.ManyToManyField(Vender, related_name='devices', blank=True)

    class Meta:
        ordering = ['-name', '-datePurchase']


    def parts(self):
        return self.Parts

    def deviceId(self):
        deviceId = ''
        parts = self.parts()
        print(type(parts))
        for part in parts.all():
            deviceId = deviceId + '&' + part.partId
        return deviceId

    def __str__(self):
        deviceName = self.type + self.deviceId()
        print('123{}'.format(type(deviceName)))
        return deviceName


class Part(models.Model):
    """零件
    例如：多波束7125分为主机和探头"""
    name = models.CharField(max_length=300, verbose_name='组件名称')
    main_device = models.ForeignKey(Device, on_delete=models.PROTECT, related_name='Parts')
    partId = models.CharField(max_length=500, verbose_name='编号', blank=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    '''项目：
    主要分几类：
    维修
    项目使用
    淘汰
    一种默认是在库
    '''
    title = models.CharField(max_length=500, verbose_name='项目名称')# 不能为空
    # leade 不能为空
    devices = models.ManyToManyField(Device, related_name='projects')# 不能为空
    startdate = models.DateTimeField(verbose_name='提交时间', auto_now_add=True)
    enddate = models.DateTimeField(verbose_name='结束时间', blank=True, null=True)# 可以为空
    remark = models.CharField(max_length=5000, verbose_name='备注', blank=True)# 可以为空
    adminmark = models.CharField(max_length=5000, verbose_name='添加备注', blank=True)# 可以为空

    def changeDevState(self):
        for device in self.devices:
            if device.stateDevice == 1 and '维修' in self.title:
                device.stateDevice = 2
                # self.save()
            elif device.stateDevice == 1 and '淘汰' not in self.title:
                device.stateDevice = 3

            else:
                device.stateDevice = 4

            self.save()

    def duration(self):  # 项目时长
        duration = self.enddate.__sub__(self.startdate)
        return duration

    def __str__(self):
        return self.title
