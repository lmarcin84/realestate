import datetime

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    created_at = models.DateTimeField('Data dodania', auto_now_add=True)
    updated_at = models.DateTimeField('Data modyfikacji', auto_now=True)

    class Meta:
        abstract = True


class Property(BaseModel):
    OFFER_NUMBER = 'numer oferty'

    HOUSE = 'dom'
    APARTMENT = 'mieszkanie'
    COMMERCIAL = 'lokal'
    LAND = 'działka'
    FACILITIES = 'obiekt'

    PROPERTY_TYPE = (
        (HOUSE, 'Dom'),
        (APARTMENT, 'Mieszkanie'),
        (COMMERCIAL, 'Lokal'),
        (LAND, 'Działka'),
        (FACILITIES, 'Obiekt')
    )

    TRANSACTION_TYPE = 'rodzaj transakcji'
    BUY = 'sprzedaz'
    RENT = 'wynajem'

    TRANSACTION_TYPE = (
        (BUY, 'Sprzedaz'),
        (RENT, 'Wynajem')
    )

    LOCATION_STREET = 'ulica'
    LOCATION_SECTOR = 'dzielnica'
    LOCATION_CITY = 'miasto'
    LOCATION_STATE = 'wojewodztwo'

    LOCATION_TYPES = (
        (LOCATION_STREET, 'Ulica'),
        (LOCATION_SECTOR, 'Dzielnica'),
        (LOCATION_CITY, 'Miasto'),
        (LOCATION_STATE, 'Wojewodztwo')
    )

    CURRENT, SUSPENDED, OUTDATED = range(3)
    STATUS_CHOICES = (
        (CURRENT, 'Aktualna'),
        (SUSPENDED, 'Zawieszona'),
        (OUTDATED, 'Nieaktualna')
    )

    LEFT_COAST, RIGHT_COAST = range(2)
    COAST = (
        (LEFT_COAST, 'Lewobrzeze'),
        (RIGHT_COAST, 'Prawobrzeze')
    )

    RECREATIONAL, AGRICULTURAL, CONSTRUCTION = range(3)
    TYPE_OF_PLOT = (
        (RECREATIONAL, 'Rekreacyjna'),
        (AGRICULTURAL, 'Rolna'),
        (CONSTRUCTION, 'Budowlana')
    )

    signature = models.CharField(
        'Numer oferty', max_length=20, null=True, blank=True)  # poprawić
    offer_status = models.CharField(
        'Status oferty', max_length=20, blank=True, null=True, choices=STATUS_CHOICES)
    property_type = models.CharField(
        'Typ nieruchomości', max_length=50, blank=True, null=True, choices=PROPERTY_TYPE)
    transaction_type = models.CharField(
        'Rodzaj transakcji', max_length=20, blank=True, null=True, choices=TRANSACTION_TYPE)
    city = models.CharField(
        'Miejscowość', max_length=255, blank=True, null=True)
    # identity property in a url
    slug = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField('Ulica', max_length=255, blank=True, null=True)
    state = models.CharField(
        'Województwo', max_length=255, blank=True, null=True)  # województwo
    district = models.CharField(
        'Dzielnica', max_length=255, blank=True, null=True)
    estate = models.CharField('Osiedle', max_length=255, blank=True, null=True)
    coast = models.CharField(
        'Prawo/Lewobrzeze', max_length=20, blank=True, null=True, choices=COAST)
    square_meter = models.DecimalField(
        'Powierzchnia', null=True, blank=True, max_digits=11, decimal_places=2)
    description = models.TextField('Opis', null=True, blank=True)
    price = models.DecimalField('Cena', max_digits=11, decimal_places=2)
    price_per_square_meter = models.DecimalField(
        'Cena za metr', max_digits=11, decimal_places=2)
    build_in_year = models.IntegerField('Rok budowy', blank=True, null=True)
    rooms = models.IntegerField('Liczba pokoi', blank=True, null=True)
    floor = models.IntegerField('Piętro', blank=True, null=True)
    number_floors = models.IntegerField('Liczba pięter', blank=True, null=True)
    area = models.DecimalField('Pow. działki', null=True, blank=True,
                               max_digits=11, decimal_places=2)  # powierzchnia działki
    driveway = models.CharField(
        'Droga dojazdowa', max_length=255, blank=True, null=True)
    type_of_plot = models.CharField(
        'Rodzaj działki', max_length=20, blank=True, null=True, choices=TYPE_OF_PLOT)
    armament_plot = models.CharField(
        'Uzbrojenie działki', max_length=255, blank=True, null=True)
    published_at = models.DateTimeField('Data wprowadzenia')
    is_published = models.BooleanField('Wprowadzono?', default=False)

    def __str__(self):
        return self.signature

    def was_published_recently(self):
        return self.published_at >= timezone.now() - datetime.timedelta(days=1)

    class PropertyManager(models.Model):
        def listed(self):
            qs = super(PropertyManager, self).get_query_set()
            return qs.filter(models.Q(status=Property.LISTED) | models.Q(status=Property.PENDING))

    class Meta:
        verbose_name = 'property'
        verbose_name_plural = 'properties'

    def __unicode__(self):
        return u'%s, %s' % (self.address, self.city)

    object = PropertyManager()


class Apartment(Property):
    pass


class House(Property):

    pass


class Land(Property):
    pass


class Commercial(Property):
    pass


class Facilities(Property):
    pass
