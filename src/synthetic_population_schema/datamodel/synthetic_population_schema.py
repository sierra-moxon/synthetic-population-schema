# Auto generated from synthetic_population_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-01-07T12:26:29
# Schema: synthetic-population-schema
#
# id: https://w3id.org/sierra-moxon/synthetic-population-schema
# description: A LinkML schema capturing the model used to enumerate https://github.com/RTIInternational/SyntheticPopulations?tab=readme-ov-file#data-identification-and-metadata
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OMRSE = CurieNamespace('OMRSE', 'http://purl.obolibrary.org/obo/OMRSE_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SYNTHETIC_POPULATION_SCHEMA = CurieNamespace('synthetic_population_schema', 'https://w3id.org/sierra-moxon/synthetic-population-schema/')
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/entity/')
DEFAULT_ = SYNTHETIC_POPULATION_SCHEMA


# Types

# Class references



@dataclass(repr=False)
class State(YAMLRoot):
    """
    A state with associated properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["State"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:State"
    class_name: ClassVar[str] = "State"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.State

    fips_code: Optional[str] = None
    name: Optional[str] = None
    abbreviation: Optional[str] = None
    counties: Optional[Union[Union[dict, "County"], List[Union[dict, "County"]]]] = empty_list()
    pumas: Optional[Union[Union[dict, "PUMA"], List[Union[dict, "PUMA"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fips_code is not None and not isinstance(self.fips_code, str):
            self.fips_code = str(self.fips_code)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.abbreviation is not None and not isinstance(self.abbreviation, str):
            self.abbreviation = str(self.abbreviation)

        if not isinstance(self.counties, list):
            self.counties = [self.counties] if self.counties is not None else []
        self.counties = [v if isinstance(v, County) else County(**as_dict(v)) for v in self.counties]

        if not isinstance(self.pumas, list):
            self.pumas = [self.pumas] if self.pumas is not None else []
        self.pumas = [v if isinstance(v, PUMA) else PUMA(**as_dict(v)) for v in self.pumas]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PUMA(YAMLRoot):
    """
    Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state or
    equivalent entity into geographic areas containing no fewer than 100,000 people each. They cover the entirety of
    the United States, Puerto Rico, and Guam.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["PUMA"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:PUMA"
    class_name: ClassVar[str] = "PUMA"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.PUMA

    fips_code: Optional[str] = None
    state_fips_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fips_code is not None and not isinstance(self.fips_code, str):
            self.fips_code = str(self.fips_code)

        if self.state_fips_code is not None and not isinstance(self.state_fips_code, str):
            self.state_fips_code = str(self.state_fips_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class County(YAMLRoot):
    """
    A county with associated properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["County"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:County"
    class_name: ClassVar[str] = "County"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.County

    name: Optional[str] = None
    fips_code: Optional[str] = None
    state_fips_code: Optional[str] = None
    tracts: Optional[Union[Union[dict, "Tract"], List[Union[dict, "Tract"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.fips_code is not None and not isinstance(self.fips_code, str):
            self.fips_code = str(self.fips_code)

        if self.state_fips_code is not None and not isinstance(self.state_fips_code, str):
            self.state_fips_code = str(self.state_fips_code)

        if not isinstance(self.tracts, list):
            self.tracts = [self.tracts] if self.tracts is not None else []
        self.tracts = [v if isinstance(v, Tract) else Tract(**as_dict(v)) for v in self.tracts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Tract(YAMLRoot):
    """
    A census tract is a small, relatively permanent geographic area within a county, used to collect and present
    demographic data from the census, usually containing between 2,500 and 8,000 residents and designed to be as
    homogeneous as possible in terms of population characteristics and living conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["Tract"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:Tract"
    class_name: ClassVar[str] = "Tract"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.Tract

    fips_code: Optional[str] = None
    state_fips_code: Optional[str] = None
    county_fips_code: Optional[str] = None
    block_groups: Optional[Union[Union[dict, "BlockGroup"], List[Union[dict, "BlockGroup"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fips_code is not None and not isinstance(self.fips_code, str):
            self.fips_code = str(self.fips_code)

        if self.state_fips_code is not None and not isinstance(self.state_fips_code, str):
            self.state_fips_code = str(self.state_fips_code)

        if self.county_fips_code is not None and not isinstance(self.county_fips_code, str):
            self.county_fips_code = str(self.county_fips_code)

        if not isinstance(self.block_groups, list):
            self.block_groups = [self.block_groups] if self.block_groups is not None else []
        self.block_groups = [v if isinstance(v, BlockGroup) else BlockGroup(**as_dict(v)) for v in self.block_groups]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BlockGroup(YAMLRoot):
    """
    a statistical division within a census tract, typically containing between 600 and 3,000 people, which is used by
    the Census Bureau to present demographic data at a smaller, more localized level than the entire census tract.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["BlockGroup"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:BlockGroup"
    class_name: ClassVar[str] = "BlockGroup"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.BlockGroup

    fips_code: Optional[str] = None
    tract_fips_code: Optional[str] = None
    state_fips_code: Optional[str] = None
    county_fips_code: Optional[str] = None
    households: Optional[Union[Union[dict, "Household"], List[Union[dict, "Household"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.fips_code is not None and not isinstance(self.fips_code, str):
            self.fips_code = str(self.fips_code)

        if self.tract_fips_code is not None and not isinstance(self.tract_fips_code, str):
            self.tract_fips_code = str(self.tract_fips_code)

        if self.state_fips_code is not None and not isinstance(self.state_fips_code, str):
            self.state_fips_code = str(self.state_fips_code)

        if self.county_fips_code is not None and not isinstance(self.county_fips_code, str):
            self.county_fips_code = str(self.county_fips_code)

        if not isinstance(self.households, list):
            self.households = [self.households] if self.households is not None else []
        self.households = [v if isinstance(v, Household) else Household(**as_dict(v)) for v in self.households]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Household(YAMLRoot):
    """
    A household entity with associated properties.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["Household"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:Household"
    class_name: ClassVar[str] = "Household"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.Household

    serialno: Optional[str] = None
    hh_id: Optional[str] = None
    hh_age: Optional[int] = None
    hh_income: Optional[float] = None
    hh_race: Optional[str] = None
    size: Optional[int] = None
    persons: Optional[Union[Union[dict, "Person"], List[Union[dict, "Person"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.serialno is not None and not isinstance(self.serialno, str):
            self.serialno = str(self.serialno)

        if self.hh_id is not None and not isinstance(self.hh_id, str):
            self.hh_id = str(self.hh_id)

        if self.hh_age is not None and not isinstance(self.hh_age, int):
            self.hh_age = int(self.hh_age)

        if self.hh_income is not None and not isinstance(self.hh_income, float):
            self.hh_income = float(self.hh_income)

        if self.hh_race is not None and not isinstance(self.hh_race, str):
            self.hh_race = str(self.hh_race)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if not isinstance(self.persons, list):
            self.persons = [self.persons] if self.persons is not None else []
        self.persons = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.persons]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(YAMLRoot):
    """
    A person associated with a household.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "synthetic_population_schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = SYNTHETIC_POPULATION_SCHEMA.Person

    state_fips_code: Optional[str] = None
    county_fips_code: Optional[str] = None
    tract_fips_code: Optional[str] = None
    block_group_fips_code: Optional[str] = None
    serialno: Optional[str] = None
    hh_id: Optional[str] = None
    hh_age: Optional[int] = None
    hh_income: Optional[float] = None
    hh_race: Optional[str] = None
    size: Optional[int] = None
    sporder: Optional[int] = None
    relp: Optional[str] = None
    rac1p: Optional[str] = None
    agep: Optional[int] = None
    sex: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.state_fips_code is not None and not isinstance(self.state_fips_code, str):
            self.state_fips_code = str(self.state_fips_code)

        if self.county_fips_code is not None and not isinstance(self.county_fips_code, str):
            self.county_fips_code = str(self.county_fips_code)

        if self.tract_fips_code is not None and not isinstance(self.tract_fips_code, str):
            self.tract_fips_code = str(self.tract_fips_code)

        if self.block_group_fips_code is not None and not isinstance(self.block_group_fips_code, str):
            self.block_group_fips_code = str(self.block_group_fips_code)

        if self.serialno is not None and not isinstance(self.serialno, str):
            self.serialno = str(self.serialno)

        if self.hh_id is not None and not isinstance(self.hh_id, str):
            self.hh_id = str(self.hh_id)

        if self.hh_age is not None and not isinstance(self.hh_age, int):
            self.hh_age = int(self.hh_age)

        if self.hh_income is not None and not isinstance(self.hh_income, float):
            self.hh_income = float(self.hh_income)

        if self.hh_race is not None and not isinstance(self.hh_race, str):
            self.hh_race = str(self.hh_race)

        if self.size is not None and not isinstance(self.size, int):
            self.size = int(self.size)

        if self.sporder is not None and not isinstance(self.sporder, int):
            self.sporder = int(self.sporder)

        if self.relp is not None and not isinstance(self.relp, str):
            self.relp = str(self.relp)

        if self.rac1p is not None and not isinstance(self.rac1p, str):
            self.rac1p = str(self.rac1p)

        if self.agep is not None and not isinstance(self.agep, int):
            self.agep = int(self.agep)

        if self.sex is not None and not isinstance(self.sex, str):
            self.sex = str(self.sex)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.counties = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.counties, name="counties", curie=SYNTHETIC_POPULATION_SCHEMA.curie('counties'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.counties, domain=None, range=Optional[Union[Union[dict, County], List[Union[dict, County]]]])

slots.tracts = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.tracts, name="tracts", curie=SYNTHETIC_POPULATION_SCHEMA.curie('tracts'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.tracts, domain=None, range=Optional[Union[Union[dict, Tract], List[Union[dict, Tract]]]])

slots.block_groups = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.block_groups, name="block_groups", curie=SYNTHETIC_POPULATION_SCHEMA.curie('block_groups'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.block_groups, domain=None, range=Optional[Union[Union[dict, BlockGroup], List[Union[dict, BlockGroup]]]])

slots.households = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.households, name="households", curie=SYNTHETIC_POPULATION_SCHEMA.curie('households'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.households, domain=None, range=Optional[Union[Union[dict, Household], List[Union[dict, Household]]]])

slots.persons = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.persons, name="persons", curie=SYNTHETIC_POPULATION_SCHEMA.curie('persons'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.persons, domain=None, range=Optional[Union[Union[dict, Person], List[Union[dict, Person]]]])

slots.pumas = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.pumas, name="pumas", curie=SYNTHETIC_POPULATION_SCHEMA.curie('pumas'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.pumas, domain=None, range=Optional[Union[Union[dict, PUMA], List[Union[dict, PUMA]]]])

slots.fips_code = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.fips_code, name="fips_code", curie=SYNTHETIC_POPULATION_SCHEMA.curie('fips_code'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.fips_code, domain=None, range=Optional[str])

slots.state_fips_code = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.state_fips_code, name="state_fips_code", curie=SYNTHETIC_POPULATION_SCHEMA.curie('state_fips_code'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.state_fips_code, domain=None, range=Optional[str])

slots.county_fips_code = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.county_fips_code, name="county_fips_code", curie=SYNTHETIC_POPULATION_SCHEMA.curie('county_fips_code'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.county_fips_code, domain=None, range=Optional[str])

slots.tract_fips_code = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.tract_fips_code, name="tract_fips_code", curie=SYNTHETIC_POPULATION_SCHEMA.curie('tract_fips_code'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.tract_fips_code, domain=None, range=Optional[str])

slots.block_group_fips_code = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.block_group_fips_code, name="block_group_fips_code", curie=SYNTHETIC_POPULATION_SCHEMA.curie('block_group_fips_code'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.block_group_fips_code, domain=None, range=Optional[str])

slots.name = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.name, name="name", curie=SYNTHETIC_POPULATION_SCHEMA.curie('name'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.name, domain=None, range=Optional[str])

slots.abbreviation = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.abbreviation, name="abbreviation", curie=SYNTHETIC_POPULATION_SCHEMA.curie('abbreviation'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.abbreviation, domain=None, range=Optional[str])

slots.serialno = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.serialno, name="serialno", curie=SYNTHETIC_POPULATION_SCHEMA.curie('serialno'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.serialno, domain=None, range=Optional[str])

slots.hh_id = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.hh_id, name="hh_id", curie=SYNTHETIC_POPULATION_SCHEMA.curie('hh_id'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.hh_id, domain=None, range=Optional[str])

slots.hh_age = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.hh_age, name="hh_age", curie=SYNTHETIC_POPULATION_SCHEMA.curie('hh_age'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.hh_age, domain=None, range=Optional[int])

slots.hh_income = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.hh_income, name="hh_income", curie=SYNTHETIC_POPULATION_SCHEMA.curie('hh_income'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.hh_income, domain=None, range=Optional[float])

slots.hh_race = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.hh_race, name="hh_race", curie=SYNTHETIC_POPULATION_SCHEMA.curie('hh_race'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.hh_race, domain=None, range=Optional[str])

slots.size = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.size, name="size", curie=SYNTHETIC_POPULATION_SCHEMA.curie('size'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.size, domain=None, range=Optional[int])

slots.person__sporder = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.sporder, name="person__sporder", curie=SYNTHETIC_POPULATION_SCHEMA.curie('sporder'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.person__sporder, domain=None, range=Optional[int])

slots.person__relp = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.relp, name="person__relp", curie=SYNTHETIC_POPULATION_SCHEMA.curie('relp'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.person__relp, domain=None, range=Optional[str])

slots.person__rac1p = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.rac1p, name="person__rac1p", curie=SYNTHETIC_POPULATION_SCHEMA.curie('rac1p'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.person__rac1p, domain=None, range=Optional[str])

slots.person__agep = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.agep, name="person__agep", curie=SYNTHETIC_POPULATION_SCHEMA.curie('agep'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.person__agep, domain=None, range=Optional[int])

slots.person__sex = Slot(uri=SYNTHETIC_POPULATION_SCHEMA.sex, name="person__sex", curie=SYNTHETIC_POPULATION_SCHEMA.curie('sex'),
                   model_uri=SYNTHETIC_POPULATION_SCHEMA.person__sex, domain=None, range=Optional[str])