

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20210106_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '1. Banners'},
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': '3. Brands'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '4. Colors'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '6. Products'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '7. ProductAttributes'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': '5. Sizes'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
