-- # Class: "State" Description: "A state with associated properties."
--     * Slot: id Description: 
--     * Slot: fips_code Description: Federal Information Processing Standard code, is a unique numeric identifier assigned to geographic areas like  states and counties within the United States, used primarily by the Census Bureau to identify locations when  analyzing population data.
--     * Slot: name Description: Name of the entity.
--     * Slot: abbreviation Description: Abbreviation of the entity.
-- # Class: "PUMA" Description: "Public Use Microdata Areas (PUMAs) are non-overlapping, statistical geographic areas that partition each state  or equivalent entity into geographic areas containing no fewer than 100,000 people each. They cover the entirety  of the United States, Puerto Rico, and Guam."
--     * Slot: id Description: 
--     * Slot: fips_code Description: Federal Information Processing Standard code, is a unique numeric identifier assigned to geographic areas like  states and counties within the United States, used primarily by the Census Bureau to identify locations when  analyzing population data.
--     * Slot: state_fips_code Description: State FIPS code.
-- # Class: "County" Description: "A county with associated properties."
--     * Slot: id Description: 
--     * Slot: name Description: Name of the entity.
--     * Slot: fips_code Description: Federal Information Processing Standard code, is a unique numeric identifier assigned to geographic areas like  states and counties within the United States, used primarily by the Census Bureau to identify locations when  analyzing population data.
--     * Slot: state_fips_code Description: State FIPS code.
-- # Class: "Tract" Description: "A census tract is a small, relatively permanent geographic area within a county, used to collect and present  demographic data from the census, usually containing between 2,500 and 8,000 residents and designed to be as  homogeneous as possible in terms of population characteristics and living conditions."
--     * Slot: id Description: 
--     * Slot: fips_code Description: Federal Information Processing Standard code, is a unique numeric identifier assigned to geographic areas like  states and counties within the United States, used primarily by the Census Bureau to identify locations when  analyzing population data.
--     * Slot: state_fips_code Description: State FIPS code.
--     * Slot: county_fips_code Description: County FIPS code.
-- # Class: "BlockGroup" Description: "a statistical division within a census tract, typically containing between 600 and 3,000 people,  which is used by the Census Bureau to present demographic data at a smaller, more localized level than  the entire census tract."
--     * Slot: id Description: 
--     * Slot: fips_code Description: Federal Information Processing Standard code, is a unique numeric identifier assigned to geographic areas like  states and counties within the United States, used primarily by the Census Bureau to identify locations when  analyzing population data.
--     * Slot: tract_fips_code Description: Tract FIPS code.
--     * Slot: state_fips_code Description: State FIPS code.
--     * Slot: county_fips_code Description: County FIPS code.
-- # Class: "Household" Description: "A household entity with associated properties."
--     * Slot: id Description: 
--     * Slot: serialno Description: Serial number of the entity.
--     * Slot: hh_id Description: Household ID associated with the entity.
--     * Slot: hh_age Description: Age of the household head (copied for reference).
--     * Slot: hh_income Description: Income of the household (copied for reference).
--     * Slot: hh_race Description: Race of the household (copied for reference).
--     * Slot: size Description: Size of the household (copied for reference).
-- # Class: "Person" Description: "A person associated with a household."
--     * Slot: id Description: 
--     * Slot: state_fips_code Description: State FIPS code.
--     * Slot: county_fips_code Description: County FIPS code.
--     * Slot: tract_fips_code Description: Tract FIPS code.
--     * Slot: block_group_fips_code Description: Block group FIPS code.
--     * Slot: serialno Description: Serial number of the entity.
--     * Slot: hh_id Description: Household ID associated with the entity.
--     * Slot: hh_age Description: Age of the household head (copied for reference).
--     * Slot: hh_income Description: Income of the household (copied for reference).
--     * Slot: hh_race Description: Race of the household (copied for reference).
--     * Slot: size Description: Size of the household (copied for reference).
--     * Slot: sporder Description: Person's order within the household.
--     * Slot: relp Description: Relationship to the household head.
--     * Slot: rac1p Description: Race of the person.
--     * Slot: agep Description: Age of the person.
--     * Slot: sex Description: Gender of the person.
-- # Class: "State_counties" Description: ""
--     * Slot: State_id Description: Autocreated FK slot
--     * Slot: counties_id Description: Counties within the state.
-- # Class: "State_pumas" Description: ""
--     * Slot: State_id Description: Autocreated FK slot
--     * Slot: pumas_id Description: Public Use Microdata Areas within the state.
-- # Class: "County_tracts" Description: ""
--     * Slot: County_id Description: Autocreated FK slot
--     * Slot: tracts_id Description: Tracts within the county.
-- # Class: "Tract_block_groups" Description: ""
--     * Slot: Tract_id Description: Autocreated FK slot
--     * Slot: block_groups_id Description: Block groups within the tract.
-- # Class: "BlockGroup_households" Description: ""
--     * Slot: BlockGroup_id Description: Autocreated FK slot
--     * Slot: households_id Description: Households within the block group.
-- # Class: "Household_persons" Description: ""
--     * Slot: Household_id Description: Autocreated FK slot
--     * Slot: persons_id Description: Persons within the household.

CREATE TABLE "State" (
	id INTEGER NOT NULL, 
	fips_code TEXT, 
	name TEXT, 
	abbreviation TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PUMA" (
	id INTEGER NOT NULL, 
	fips_code TEXT, 
	state_fips_code TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "County" (
	id INTEGER NOT NULL, 
	name TEXT, 
	fips_code TEXT, 
	state_fips_code TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Tract" (
	id INTEGER NOT NULL, 
	fips_code TEXT, 
	state_fips_code TEXT, 
	county_fips_code TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BlockGroup" (
	id INTEGER NOT NULL, 
	fips_code TEXT, 
	tract_fips_code TEXT, 
	state_fips_code TEXT, 
	county_fips_code TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Household" (
	id INTEGER NOT NULL, 
	serialno TEXT, 
	hh_id TEXT, 
	hh_age INTEGER, 
	hh_income FLOAT, 
	hh_race TEXT, 
	size INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	id INTEGER NOT NULL, 
	state_fips_code TEXT, 
	county_fips_code TEXT, 
	tract_fips_code TEXT, 
	block_group_fips_code TEXT, 
	serialno TEXT, 
	hh_id TEXT, 
	hh_age INTEGER, 
	hh_income FLOAT, 
	hh_race TEXT, 
	size INTEGER, 
	sporder INTEGER, 
	relp TEXT, 
	rac1p TEXT, 
	agep INTEGER, 
	sex TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "State_counties" (
	"State_id" INTEGER, 
	counties_id INTEGER, 
	PRIMARY KEY ("State_id", counties_id), 
	FOREIGN KEY("State_id") REFERENCES "State" (id), 
	FOREIGN KEY(counties_id) REFERENCES "County" (id)
);
CREATE TABLE "State_pumas" (
	"State_id" INTEGER, 
	pumas_id INTEGER, 
	PRIMARY KEY ("State_id", pumas_id), 
	FOREIGN KEY("State_id") REFERENCES "State" (id), 
	FOREIGN KEY(pumas_id) REFERENCES "PUMA" (id)
);
CREATE TABLE "County_tracts" (
	"County_id" INTEGER, 
	tracts_id INTEGER, 
	PRIMARY KEY ("County_id", tracts_id), 
	FOREIGN KEY("County_id") REFERENCES "County" (id), 
	FOREIGN KEY(tracts_id) REFERENCES "Tract" (id)
);
CREATE TABLE "Tract_block_groups" (
	"Tract_id" INTEGER, 
	block_groups_id INTEGER, 
	PRIMARY KEY ("Tract_id", block_groups_id), 
	FOREIGN KEY("Tract_id") REFERENCES "Tract" (id), 
	FOREIGN KEY(block_groups_id) REFERENCES "BlockGroup" (id)
);
CREATE TABLE "BlockGroup_households" (
	"BlockGroup_id" INTEGER, 
	households_id INTEGER, 
	PRIMARY KEY ("BlockGroup_id", households_id), 
	FOREIGN KEY("BlockGroup_id") REFERENCES "BlockGroup" (id), 
	FOREIGN KEY(households_id) REFERENCES "Household" (id)
);
CREATE TABLE "Household_persons" (
	"Household_id" INTEGER, 
	persons_id INTEGER, 
	PRIMARY KEY ("Household_id", persons_id), 
	FOREIGN KEY("Household_id") REFERENCES "Household" (id), 
	FOREIGN KEY(persons_id) REFERENCES "Person" (id)
);