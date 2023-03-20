import os
from datetime import datetime
from typing import Optional, Union

from django.conf import settings
from django.core.files.storage import default_storage
from faker import Faker

import csv

from fake_csv.models import Schema, DataSet, DataType


def data_generator(data_type: DataType, value_range: Optional[tuple] = None) -> Union[str, int]:
    faker = Faker()
    data_mapper = {
        DataType.FULL_NAME: faker.name,
        DataType.JOB: faker.job,
        DataType.EMAIL: faker.safe_email,
        DataType.DOMAIN_NAME: faker.domain_name,
        DataType.PHONE_NUMBER: faker.phone_number,
        DataType.COMPANY_NAME: faker.company,
        DataType.TEXT: faker.paragraph,
        DataType.INTEGER: faker.random_int,
        DataType.ADDRESS: faker.address,
        DataType.DATE: faker.date,
    }

    method = data_mapper[data_type]

    if data_type == DataType.TEXT:
        result = method(nb_sentences=faker.random_int(*value_range), variable_nb_sentences=False)
    elif data_type == DataType.INTEGER:
        result = method(*value_range)
    else:
        result = method()

    return result


def generate_data_set(schema: Schema, number_of_rows: int) -> None:
    """Method to generate dataset from schema"""
    dataset = DataSet.objects.create(schema=schema, number_of_rows=number_of_rows)

    csv.register_dialect(
        "custom",
        delimiter=schema.delimiter,
        quotechar=schema.quote_character,
        quoting=csv.QUOTE_ALL,
    )
    columns = schema.columns.all()

    filename = f"{schema.name}_{number_of_rows}_{datetime.now().isoformat()}.csv"
    with default_storage.open(os.path.join(settings.MEDIA_ROOT, filename), "w") as f:
        writer = csv.DictWriter(f, fieldnames=[c.name for c in columns], dialect="custom")
        writer.writeheader()
        for i in range(number_of_rows):
            row = dict()
            for column in columns:
                row[column.name] = data_generator(
                    column.data_type,
                    value_range=(column.data_range_from, column.data_range_to),
                )
            writer.writerow(row)

    dataset.status = DataSet.Status.READY
    dataset.file = filename
    dataset.save()
