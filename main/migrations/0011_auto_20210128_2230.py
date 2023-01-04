

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210128_2206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productattribute',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_imgs/'),
        ),
    ]
