

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210110_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='img',
            field=models.ImageField(upload_to='banner_imgs/'),
        ),
    ]