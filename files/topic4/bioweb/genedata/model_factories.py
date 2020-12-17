import factory

from django.test import TestCase
from django.conf import settings
from django.core.files import File
from random import randint
from random import choice
from .models import *


class ECFactory(factory.django.DjangoModelFactory):
    ec_name = choice(['oxidoreductase', 'transferase',
                      'hydrolase', 'lyase', 'isomerase',
                      'ligase'])

    class Meta:
        model = EC


class SequencingFactory(factory.django.DjangoModelFactory):
    sequencing_factory = factory.Faker('sentence', nb_words=1)
    factory_location = factory.Faker('sentence', nb_words=1)

    class Meta:
        model = Sequencing


class GeneFactory(factory.django.DjangoModelFactory):
    gene_id = factory.Sequence(lambda n: 'gene%d' % n+str(1))
    entity = "Plasmid"
    start = randint(1, 100000)
    stop = start+randint(1, 10000)
    sense = "+"
    start_codon = "M"
    sequencing = factory.SubFactory(SequencingFactory)
    ec = factory.SubFactory(ECFactory)
    access = 0

    class Meta:
        model = Gene
