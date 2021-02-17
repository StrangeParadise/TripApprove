from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('status', models.CharField(choices=[
                    ('PENDING', 'Pending'),
                    ('APPROVED', 'Approved'),
                    ('DECLINED', 'Declined'),
                    ('CANCELLED', 'Cancelled')
                ], default='PENDING', max_length=10)),

                ('created', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=256)),
            ],
        ),
    ]
