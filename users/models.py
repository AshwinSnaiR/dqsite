from django.db import models


# Create your models here.
class Users(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class datasetDetails(models.Model):
    dbid = models.CharField(max_length=200)
    datasetName = models.CharField(max_length=50)
    sourceType = models.CharField(max_length=50)
    schemaName = models.CharField(max_length=50)
    hostName = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    database = models.CharField(max_length=50)
    port = models.IntegerField


class ProfilingDetails(models.Model):
    databaseID = models.IntegerField
    columnName = models.CharField(max_length=50)
    unqCount = models.CharField(max_length=50)
    nullCount = models.CharField(max_length=50)
    mean = models.IntegerField
    min = models.IntegerField
    max = models.IntegerField
    type = models.CharField(max_length=50)


class tableAnalysis(models.Model):
    databaseID = models.IntegerField
    tableID = models.IntegerField
    rowCount = models.IntegerField
    colCount = models.IntegerField


class tableNames(models.Model):
    databaseID = models.IntegerField
    tableID = models.IntegerField
    tableName = models.CharField(max_length=100)

