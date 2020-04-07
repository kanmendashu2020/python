# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange utils' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the utils, but don't rename db_table values or field names.
from django.db import models


class TAreaindustry(models.Model):
    area = models.ForeignKey('TBaseMonitoringarea', models.DO_NOTHING)
    industry = models.ForeignKey('TBaseIndustry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_areaindustry'


class TBaseAlarmMap(models.Model):
    pollution_type = models.CharField(max_length=10)
    pollutant_code = models.CharField(max_length=10)
    extreme_type = models.CharField(max_length=20)
    index_order = models.IntegerField(blank=True, null=True)
    gmt_create = models.DateTimeField(blank=True, null=True)
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_alarm_map'
        unique_together = (('pollution_type', 'pollutant_code'),)


class TBaseAreasite(models.Model):
    area = models.ForeignKey('TBaseMonitoringarea', models.DO_NOTHING)
    site = models.ForeignKey('TBaseSiteinfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_base_areasite'


class TBaseAreatype(models.Model):
    type_name = models.CharField(max_length=45)
    type_code = models.CharField(max_length=45, blank=True, null=True)
    type_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_areatype'


class TBaseDataPollGas(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_raw = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    sample_time = models.DateTimeField(blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    audit_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_base_data_poll_gas'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TBaseDataPollNoise(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_raw = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sample_time = models.DateTimeField(blank=True, null=True)
    audit_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_base_data_poll_noise'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TBaseDataPollWater(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_raw = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    sample_time = models.DateTimeField(blank=True, null=True)
    audit_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_base_data_poll_water'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TBaseDevice(models.Model):
    type = models.ForeignKey('TBaseDevicetype', models.DO_NOTHING)
    sn = models.CharField(max_length=45)
    mn = models.CharField(unique=True, max_length=45)
    pollutant_code_version = models.CharField(max_length=10)
    center_ip = models.CharField(max_length=45, blank=True, null=True)
    center_port = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField()
    version = models.CharField(max_length=45, blank=True, null=True)
    statu = models.IntegerField(blank=True, null=True)
    online_statu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_device'


class TBaseDevicetype(models.Model):
    type_name = models.CharField(max_length=45)
    type_code = models.CharField(max_length=45)
    type_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_devicetype'


class TBaseEquipmentInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    pollution_type = models.CharField(max_length=10)
    equipment_name = models.CharField(max_length=50)
    equipment_code = models.CharField(max_length=50)
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_equipment_info'


class TBaseIndustry(models.Model):
    industry_name = models.CharField(max_length=50)
    industry_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_industry'


class TBaseManualMeasurement(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.PositiveIntegerField()
    mn = models.CharField(max_length=24)
    pollutant_code = models.CharField(max_length=10)
    pw = models.CharField(max_length=6)
    begin_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    result = models.CharField(max_length=14, blank=True, null=True)
    code = models.CharField(max_length=20, blank=True, null=True)
    poll_data_time = models.DateTimeField(blank=True, null=True)
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_manual_measurement'


class TBaseMonitoringarea(models.Model):
    region = models.ForeignKey('TBaseRegion', models.DO_NOTHING)
    region_code = models.CharField(max_length=45, blank=True, null=True)
    area_type = models.ForeignKey(TBaseAreatype, models.DO_NOTHING)
    area_name = models.CharField(max_length=50)
    area_code = models.CharField(max_length=20, blank=True, null=True)
    area_address = models.CharField(max_length=200, blank=True, null=True)
    area_contact = models.CharField(max_length=20, blank=True, null=True)
    area_phone = models.CharField(max_length=20, blank=True, null=True)
    area_email = models.CharField(max_length=50, blank=True, null=True)
    center_lat = models.DecimalField(max_digits=10, decimal_places=6)
    center_lng = models.DecimalField(max_digits=10, decimal_places=6)
    border = models.TextField()

    class Meta:
        managed = False
        db_table = 't_base_monitoringarea'


class TBaseNvrInfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nvr_login_name = models.CharField(max_length=50)
    nvr_ip = models.CharField(max_length=20)
    nvr_port = models.CharField(max_length=10)
    site_id = models.IntegerField(unique=True)
    nvr_pwd = models.CharField(max_length=50)
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_nvr_info'


class TBaseParkInfo(models.Model):
    park_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=45)
    center_lat = models.DecimalField(max_digits=10, decimal_places=6)
    center_lng = models.DecimalField(max_digits=10, decimal_places=6)
    border = models.TextField()
    zoom = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_base_park_info'


class TBaseParkarea(models.Model):
    park_id = models.IntegerField()
    area_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 't_base_parkarea'


class TBasePassback(models.Model):
    id = models.BigAutoField(primary_key=True)
    mn = models.CharField(max_length=30)
    pw = models.CharField(max_length=6, blank=True, null=True)
    cn = models.CharField(max_length=7)
    data_time = models.DateTimeField()
    result = models.CharField(max_length=14)
    code = models.CharField(max_length=20, blank=True, null=True)
    passback_frequency = models.PositiveIntegerField()
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_passback'
        unique_together = (('data_time', 'mn', 'cn'),)


class TBaseQualityControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    site_id = models.IntegerField()
    equipment_id = models.BigIntegerField()
    operator_user_id = models.IntegerField()
    operator_time = models.DateTimeField(blank=True, null=True)
    operator_content = models.CharField(max_length=100, blank=True, null=True)
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_quality_control'


class TBaseQuestionType(models.Model):
    question_type_name = models.CharField(max_length=100)
    question_type_code = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_base_question_type'


class TBaseRegion(models.Model):
    region_name = models.CharField(max_length=45)
    region_code = models.CharField(max_length=45, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    type_id = models.IntegerField()
    lft = models.IntegerField(blank=True, null=True)
    rgt = models.IntegerField(blank=True, null=True)
    parent_code = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_region'


class TBaseRegiontype(models.Model):
    type_name = models.CharField(max_length=45)
    type_level = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_base_regiontype'


class TBaseSensor(models.Model):
    sensor_address = models.CharField(max_length=50)
    sensor_status = models.IntegerField()
    sensor_name = models.CharField(max_length=100)
    sensor_description = models.CharField(max_length=255, blank=True, null=True)
    sensor_type_id = models.IntegerField()
    investment_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_base_sensor'


class TBaseSensorType(models.Model):
    sensor_type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_base_sensor_type'


class TBaseSiteMalfunction(models.Model):
    info = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField()
    flag_type = models.CharField(max_length=1)
    alarm_type = models.CharField(max_length=11)
    pollutant_code = models.CharField(max_length=45)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    pollutant_value = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    alarm_time = models.DateTimeField()
    confirm_flag = models.IntegerField()
    cn = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 't_base_site_malfunction'


class TBaseSitealarmlevel(models.Model):
    site_id = models.IntegerField()
    pollutant_code = models.CharField(max_length=45)
    level1 = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    level2 = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_sitealarmlevel'
        unique_together = (('site_id', 'pollutant_code'),)


class TBaseSitedevice(models.Model):
    site = models.ForeignKey('TBaseSiteinfo', models.DO_NOTHING)
    device = models.ForeignKey(TBaseDevice, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_base_sitedevice'


class TBaseSiteinfo(models.Model):
    site_name = models.CharField(max_length=45)
    site_address = models.CharField(max_length=45, blank=True, null=True)
    site_type = models.CharField(max_length=20, blank=True, null=True)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_base_siteinfo'


class TBaseSitepollutantalarmGas(models.Model):
    info = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField()
    flag_type = models.CharField(max_length=1)
    alarm_type = models.CharField(max_length=11)
    pollutant_code = models.CharField(max_length=45, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    pollutant_value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_level1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_level2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_time = models.DateTimeField()
    confirm_flag = models.IntegerField()
    cn = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 't_base_sitepollutantalarm_gas'


class TBaseSitepollutantalarmNoise(models.Model):
    info = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField()
    flag_type = models.CharField(max_length=1)
    alarm_type = models.CharField(max_length=11)
    pollutant_code = models.CharField(max_length=45, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    pollutant_value = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_level1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_level2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    alarm_time = models.DateTimeField()
    confirm_flag = models.IntegerField()
    cn = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 't_base_sitepollutantalarm_noise'


class TBaseSitepollutantalarmWater(models.Model):
    info = models.CharField(max_length=45, blank=True, null=True)
    site_id = models.IntegerField()
    flag_type = models.CharField(max_length=1)
    alarm_type = models.CharField(max_length=11)
    pollutant_code = models.CharField(max_length=45)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    pollutant_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_level1 = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_level2 = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_time = models.DateTimeField(blank=True, null=True)
    confirm_flag = models.IntegerField()
    cn = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 't_base_sitepollutantalarm_water'


class TBaseUserMention(models.Model):
    user_id = models.IntegerField()
    site_id = models.IntegerField()
    pollution_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_base_user_mention'


class TCodePollutantcatg(models.Model):
    catg_name = models.CharField(max_length=30)
    catg_code = models.CharField(max_length=45)
    catg_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_code_pollutantcatg'


class TCodePollutantinfo(models.Model):
    catg_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=45)
    cnname = models.CharField(max_length=45)
    enname = models.CharField(max_length=100, blank=True, null=True)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    symbol = models.CharField(max_length=45, blank=True, null=True)
    cas = models.CharField(max_length=45, blank=True, null=True)
    cf = models.DecimalField(max_digits=18, decimal_places=6)
    mr = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    catg_code = models.CharField(max_length=45, blank=True, null=True)
    con_unit = models.CharField(max_length=20, blank=True, null=True)
    emission_unit = models.CharField(max_length=20, blank=True, null=True)
    code_old = models.CharField(max_length=45, blank=True, null=True)
    integer_bit = models.IntegerField(blank=True, null=True)
    decimal_bit = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_code_pollutantinfo'


class TLogAuditGas(models.Model):
    site_id = models.IntegerField()
    site_type = models.IntegerField()
    data_time = models.DateTimeField()
    audit_time = models.DateTimeField()
    audit_value = models.DecimalField(max_digits=18, decimal_places=6)
    audit_user = models.CharField(max_length=50, blank=True, null=True)
    audit_ip = models.CharField(max_length=50, blank=True, null=True)
    audit_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log_audit_gas'


class TLogAuditWater(models.Model):
    site_id = models.IntegerField()
    site_type = models.IntegerField()
    data_time = models.DateTimeField()
    audit_time = models.DateTimeField()
    audit_value = models.DecimalField(max_digits=18, decimal_places=6)
    audit_user = models.CharField(max_length=50, blank=True, null=True)
    audit_ip = models.CharField(max_length=50, blank=True, null=True)
    audit_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log_audit_water'


class TLogOperation(models.Model):
    id = models.BigAutoField(primary_key=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=30)
    operation_code = models.CharField(max_length=30)
    user_id = models.IntegerField()
    gmt_create = models.DateTimeField()
    gmt_modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_log_operation'


class TLogSocket(models.Model):
    qn = models.CharField(max_length=30, blank=True, null=True)
    mn = models.CharField(max_length=45)
    cn = models.CharField(max_length=10, blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    direction = models.CharField(max_length=10)
    logtime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_log_socket'


class TMidDataPollDayGas(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_day_gas'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollDayNoise(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)
    day_data = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    night_data = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_day_noise'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollDayWater(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_day_water'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollHourGas(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_hour_gas'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollHourNoise(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_hour_noise'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollHourWater(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_hour_water'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMinGas(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_min_gas'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMinNoise(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_min_noise'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMinWater(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10, blank=True, null=True)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_min_water'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMonthGas(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_month_gas'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMonthNoise(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)
    day_data = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    night_data = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_month_noise'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TMidDataPollMonthWater(models.Model):
    data_time = models.DateTimeField()
    pollutant_code = models.CharField(max_length=10, blank=True, null=True)
    pollutant_code_old = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.IntegerField()
    mn = models.CharField(max_length=45)
    con_total = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    con_min = models.DecimalField(max_digits=18, decimal_places=6)
    con_avg = models.DecimalField(max_digits=18, decimal_places=6)
    con_max = models.DecimalField(max_digits=18, decimal_places=6)
    zs_flag = models.IntegerField(blank=True, null=True)
    con_flag = models.CharField(max_length=10)
    value_audit = models.DecimalField(max_digits=18, decimal_places=6)
    emission_value = models.DecimalField(max_digits=18, decimal_places=6, blank=True, null=True)
    alarm_flag = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_mid_data_poll_month_water'
        unique_together = (('data_time', 'site_id', 'pollutant_code'),)


class TSysActionlog(models.Model):
    sys = models.ForeignKey('TSysSystem', models.DO_NOTHING)
    user = models.ForeignKey('TSysUser', models.DO_NOTHING)
    action_time = models.DateTimeField()
    contents = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=45, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_actionlog'


class TSysAdminuser(models.Model):
    user_id = models.IntegerField()
    level = models.IntegerField(blank=True, null=True)
    level2 = models.IntegerField(blank=True, null=True)
    level3 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_adminuser'


class TSysMonitoringType(models.Model):
    pollution_type_code = models.CharField(max_length=10)
    pollution_type_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 't_sys_monitoring_type'


class TSysPermission(models.Model):
    sys = models.ForeignKey('TSysSystem', models.DO_NOTHING)
    permname = models.CharField(unique=True, max_length=30)
    permcode = models.CharField(unique=True, max_length=20)
    remarks = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_permission'


class TSysRoll(models.Model):
    sys = models.ForeignKey('TSysSystem', models.DO_NOTHING)
    rolltype = models.IntegerField()
    rollname = models.CharField(unique=True, max_length=30)
    rollcode = models.CharField(unique=True, max_length=20)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    treelevel = models.IntegerField(blank=True, null=True)
    maplevel = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_roll'


class TSysRollarea(models.Model):
    roll = models.ForeignKey(TSysRoll, models.DO_NOTHING)
    park_id = models.IntegerField(blank=True, null=True)
    area = models.ForeignKey(TBaseMonitoringarea, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_sys_rollarea'


class TSysRollperm(models.Model):
    roll = models.ForeignKey(TSysRoll, models.DO_NOTHING)
    perm = models.ForeignKey(TSysPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_sys_rollperm'


class TSysSystem(models.Model):
    sys_name = models.CharField(unique=True, max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_system'


class TSysUser(models.Model):
    username = models.CharField(max_length=30)
    loginname = models.CharField(unique=True, max_length=16)
    password = models.CharField(max_length=128)
    salt = models.CharField(max_length=128)
    email = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField(blank=True, null=True)
    telphone = models.CharField(db_column='telPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sys_user'


class TSysUserroll(models.Model):
    user = models.ForeignKey(TSysUser, models.DO_NOTHING)
    roll = models.ForeignKey(TSysRoll, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 't_sys_userroll'
