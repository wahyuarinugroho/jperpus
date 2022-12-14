# Generated by Django 3.2.2 on 2022-08-19 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelompok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=10)),
                ('keterangan', models.TextField(default='-')),
            ],
        ),
        migrations.CreateModel(
            name='Buku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=50)),
                ('penulis', models.CharField(max_length=50)),
                ('penerbit', models.CharField(max_length=50)),
                ('jumlah', models.IntegerField(null=True)),
                ('cover', models.ImageField(null=True, upload_to='cover/')),
                ('tanggal', models.DateTimeField(auto_now_add=True, null=True)),
                ('kelompok_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jperpustakaan.kelompok')),
            ],
        ),
    ]
