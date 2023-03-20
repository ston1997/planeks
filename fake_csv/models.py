from django.db import models
from django.contrib.auth.models import User


class DataType(models.TextChoices):
    FULL_NAME = "full_name", "Full Name"
    JOB = "job", "Job"
    EMAIL = "email", "Email"
    DOMAIN_NAME = "domain_name", "Domain Name"
    PHONE_NUMBER = "phone_number", "Phone Number"
    COMPANY_NAME = "company_name", "Company Name"
    TEXT = "text", "Text"
    INTEGER = "integer", "Integer"
    ADDRESS = "address", "Address"
    DATE = "date", "Date"


class Schema(models.Model):
    class Delimiter(models.TextChoices):
        COMMA = ",", "Comma (,)"
        SEMICOLON = ";", "Semicolon (;)"
        TAB = "\t", "Tab (\t)"
        SPACE = " ", "Space ( )"
        VERTICAL_BAR = "|", "Vertical bar (|)"

    class QuoteCharacter(models.TextChoices):
        DOUBLE_QUOTE = '"', 'Double-quote (")'
        SINGLE_QUOTE = "'", "Single-quote (')"

    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    delimiter = models.CharField(
        max_length=1,
        choices=Delimiter.choices,
        default=Delimiter.COMMA,
        help_text="column separator",
    )
    quote_character = models.CharField(
        max_length=1,
        choices=QuoteCharacter.choices,
        default=QuoteCharacter.DOUBLE_QUOTE,
    )

    def get_absolute_url(self):
        return f"/schemas/?{self.pk}"

    def __str__(self):
        return self.name


class Column(models.Model):
    name = models.CharField(max_length=100)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="columns")
    data_type = models.CharField(max_length=12, choices=DataType.choices)
    order = models.PositiveSmallIntegerField()
    data_range_from = models.IntegerField(blank=True, null=True, verbose_name="from")
    data_range_to = models.IntegerField(blank=True, null=True, verbose_name="to")

    class Meta:
        ordering = ("order",)


class DataSet(models.Model):

    class Status(models.TextChoices):
        READY = "Ready", "READY"
        PROCESSING = "Processing", "PROCESSING"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.PROCESSING)
    file = models.FileField(null=True, blank=True)
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name="data_sets")
    number_of_rows = models.PositiveIntegerField()

    class Meta:
        ordering = ("-updated_at", "-created_at",)
