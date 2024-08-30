from django.db import models

class Feline(models.Model):
    feline_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    fav_toy = models.CharField(max_length=100)
    coloration = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='cats_photos/', blank=True, null=True) 

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    feline = models.ForeignKey(Feline, on_delete=models.CASCADE, related_name='medical_records')
    checkupdate = models.DateField()
    treatment = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Record {self.record_id} for {self.feline.name}'
