# synthetic-population-schema

A LinkML schema capturing the model used to enumerate https://github.com/RTIInternational/SyntheticPopulations?tab=readme-ov-file#data-identification-and-metadata


## Project Setup

1. Clone *cmdr* project repository

```
$ git clone https://github.com/sierra-moxon/synthetic-population-schema.git
```

2. Create virtual environment and install project dependencies
```
$ make install
```

3. Create downstream schema artifacts, run unit tests, and also validate examples/instance data against schema
```
$ make test
```

4. LinkML transformer mapping between source and target schemas on a class
```
$ make test_transform
```


## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>


## Website

[https://sierra-moxon.github.io/synthetic-population-schema](https://sierra-moxon.github.io/synthetic-population-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [synthetic_population_schema](src/synthetic_population_schema)
    * [schema](src/synthetic_population_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/synthetic_population_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
