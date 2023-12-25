# Explore Close Approaches of Near-Earth Objects

This portfolio project, developed for educational purposes as part of the 'Advanced Python Techniques' nanodegree from Udacity, showcases the application of Python in analyzing and exploring the close approaches of near-Earth objects (NEOs), utilizing data from NASA/JPL's Center for Near Earth Object Studies.

## Overview

At a high-level, this project implements a command-line tool developed in Python to inspect and query a dataset of NEOs and their close approaches to Earth. The tool includes features to read data from both CSV and JSON files, converting this data into structured Python objects. It also facilitates filtering operations on the data, allows limiting the size of the result set, and enables writing the results to a file in a structured format, such as CSV or JSON.

This tool allows the inspection of properties of the near-Earth objects in the dataset and querying the dataset of close approaches to Earth using a variety of filters:

- Occurs on a given date.
- Occurs on or after a given start date.
- Occurs on or before a given end date.
- Approaches Earth at a distance of at least (or at most) X astronomical units.
- Approaches Earth at a relative velocity of at least (or at most) Y kilometers per second.
- Has a diameter that is at least as large as (or at least as small as) Z kilometers.
- Is marked by NASA as potentially hazardous (or not).

### Learning Objectives

This project showcases proficiency in several key areas of Python programming and software development:

- Effective representation of structured data in Python.
- Skillful extraction of data from structured files (CSV, JSON) into Python.
- Competent transformation of data within Python to meet specific requirements.
- Proficient saving of processed results to files in structured formats (CSV, JSON).

Key competencies demonstrated in this project include:

- Ability to write Python functions for data transformation and algorithm implementation.
- Design of Python classes to encapsulate complex data types and structures.
- Development of interface abstractions to streamline complex implementations.

## Understanding the Near-Earth Object Close Approach Datasets

This project contains two important data sets, and the first step is to explore and understand the data containing within these structured files.

One dataset (`neos.csv`) contains information about semantic, physical, orbital, and model parameters for certain small bodies (asteroids and comets, mostly) in our solar system. The other dataset (`cad.json`) contains information about NEO close approaches - moments in time when the orbit of an astronomical body brings it close to Earth. NASA helpfully provides a [glossary](https://cneos.jpl.nasa.gov/glossary/) to define any unfamiliar terms you might encounter.

Importantly, these datasets come directly from NASA.

### Small-Bodies Dataset

NASA's Jet Propulsion Laboratory (JPL) offers a comprehensive database of "small bodies" in the solar system, primarily consisting of asteroids and comets. A significant subset of these objects are classified as near-Earth objects (NEOs), which are bodies like comets and asteroids that have orbits bringing them into proximity with Earth. 

This dataset enables inquiries such as determining the diameter of Halley's Comet or assessing the potential hazard of the NEO named 'Eros'. The data, sourced from NASA's web interface, is represented in a CSV format (`neos.csv`), offering an extensive range of information about NEOs. This file includes a plethora of columns (75 in total), providing a detailed overview of each NEO, including unique identifiers, names, sizes, and other key attributes.

A cursory glance at `neos.csv` reveals:

- `pdes` - the primary designation, serving as a unique identifier.
- `name` - the name recognized by the International Astronomical Union (IAU).
- `pha` - a flag indicating if the NEO is categorized as "Potentially Hazardous" by NASA.
- `diameter` - the estimated diameter in kilometers.

For instance, the NEO 'Eros' has a designation of 433, is not marked as hazardous, and measures approximately 16.84km in diameter. It's worth noting that while every NEO has a primary designation, not all have IAU names, and diameter data may be missing for some due to limited observations.

For further exploration and interpretation of the dataset, NASA's [single small body search interface](https://ssd.jpl.nasa.gov/sbdb.cgi) and [API documentation](https://ssd-api.jpl.nasa.gov/doc/sbdb.html) can be valuable resources.

### Close Approach Dataset

The Center for Near-Earth Object Studies (CNEOS) provides data on NEOs' close approaches to Earth. These events occur when an NEO's orbit brings it near to Earth, with "near" being a relative term in astronomical distances. The data is formatted in JSON (`cad.json`), retrieved from NASA's public API. 

The dataset encapsulates details like time of close approach, distance, and relative velocity. For example, the first entry in the dataset details an approach by the NEO "170903" on 1900-Jan-01, at a distance of about 0.092 astronomical units, and traveling at a relative velocity of 16.75 km/s.

The JSON structure comprises the "signature", "count", "fields", and "data" sections, each serving a distinct purpose:

- "signature" indicates the data source.
- "count" provides the number of entries.
- "fields" describe the data in each entry.
- "data" contains the actual close approach data.

The dataset is rich with information, offering insights into numerous close approaches within the 20th and 21st centuries. The details like primary designation, time in both Julian Date and standard format, distance measurements in astronomical units, and velocities are crucial for understanding each close approach.

For an in-depth understanding of each attribute, NASA's [API documentation](https://ssd-api.jpl.nasa.gov/doc/cad.html) is an excellent guide.

### Visual Exploration

If someone prefers to explore data sets by poking around a web site, NASA has [a tutorial video](https://www.youtube.com/watch?v=UA6voCyCW1g) on how to effectively navigate the CNEOS website, and an [interactive close approach data table](https://cneos.jpl.nasa.gov/ca/) that you can investigate.

Also, it's important to realize that NASA is discovering new NEOs, and potential forecasting new close approaches, every week, so their web-based UI might contain updated information that isn't represented in the data files included with this project.

## Project Interface

This project is driven by the `main.py` script. The user will run `python3 main.py ... ... ...` at the command line to invoke the program that will call the code.

At a command line, the user can run `python3 main.py --help` for an explanation of how to invoke the script.

```python
usage: main.py [-h] [--neofile NEOFILE] [--cadfile CADFILE] {inspect,query,interactive} ...

Explore past and future close approaches of near-Earth objects.

positional arguments:
  {inspect,query,interactive}

optional arguments:
  -h, --help            show this help message and exit
  --neofile NEOFILE     Path to CSV file of near-Earth objects.
  --cadfile CADFILE     Path to JSON file of close approach data.
```

There are three subcommands: `inspect`, `query`, and `interactive`. Let's take a look at the interfaces of each of these subcommands.

### `inspect`

The `inspect` subcommand inspects a single NEO, printing its details in a human-readable format. The NEO is specified with exactly one of the `--pdes` option (the primary designation) and the `--name` option (the IAU name). The `--verbose` flag additionally prints out, in a human-readable form, all known close approaches to Earth made by this NEO. Each of these options has an abbreviated version. To remind yourself of the full interface, you can run `python3 main.py inspect --help`:

```
$ python3 main.py inspect --help
usage: main.py inspect [-h] [-v] (-p PDES | -n NAME)

Inspect an NEO by primary designation or by name.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Additionally, print all known close approaches of this NEO.
  -p PDES, --pdes PDES  The primary designation of the NEO to inspect (e.g. '433').
  -n NAME, --name NAME  The IAU name of the NEO to inspect (e.g. 'Halley').
```

Here are a few examples of the `inspect` subcommand in action:

```
# Inspect the NEO with a primary designation of 433 (that's Eros!)
$ python3 main.py inspect --pdes 433
NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.

# Inspect the NEO with an IAU name of "Halley" (that's Halley's Comet!)
$ python3 main.py inspect --name Halley
NEO 1P (Halley) has a diameter of 11.000 km and is not potentially hazardous.

# Attempt to inspect an NEO that doesn't exist.
$ python3 main.py inspect --name fake-comet
No matching NEOs exist in the database.

# Verbosely list information about Ganymed and each of its known close approaches.
# For the record, Ganymed is HUGE - it's the largest known NEO.
$ python3 main.py inspect --verbose --name Ganymed
NEO 1036 (Ganymed) has a diameter of 37.675 km and is not potentially hazardous.
- On 1911-10-15 19:16, '1036 (Ganymed)' approaches Earth at a distance of 0.38 au and a velocity of 17.09 km/s.
- On 1924-10-17 00:51, '1036 (Ganymed)' approaches Earth at a distance of 0.50 au and a velocity of 19.36 km/s.
- On 1998-10-14 05:12, '1036 (Ganymed)' approaches Earth at a distance of 0.46 au and a velocity of 13.64 km/s.
- On 2011-10-13 00:04, '1036 (Ganymed)' approaches Earth at a distance of 0.36 au and a velocity of 14.30 km/s.
- On 2024-10-13 01:56, '1036 (Ganymed)' approaches Earth at a distance of 0.37 au and a velocity of 16.33 km/s.
- On 2037-10-15 18:31, '1036 (Ganymed)' approaches Earth at a distance of 0.47 au and a velocity of 18.68 km/s.
```

For an NEO to be found with the `inspect` subcommand, the given primary designation or IAU name must match the data exactly, so if an NEO is mysteriously missing, double-check the spelling and capitalization.

### `query`

The `query` subcommand is more significantly more advanced - a `query` generates a collection of close approaches that match a set of specified filters, and either displays a limited set of those results to standard output or writes the structured results to a file.

```
$ python3 main.py query --help
usage: main.py query [-h] [-d DATE] [-s START_DATE] [-e END_DATE] [--min-distance DISTANCE_MIN] [--max-distance DISTANCE_MAX]
                     [--min-velocity VELOCITY_MIN] [--max-velocity VELOCITY_MAX] [--min-diameter DIAMETER_MIN]
                     [--max-diameter DIAMETER_MAX] [--hazardous] [--not-hazardous] [-l LIMIT] [-o OUTFILE]

Query for close approaches that match a collection of filters.

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        The maximum number of matches to return. Defaults to 10 if no --outfile is given.
  -o OUTFILE, --outfile OUTFILE
                        File in which to save structured results. If omitted, results are printed to standard output.

Filters:
  Filter close approaches by their attributes or the attributes of their NEOs.

  -d DATE, --date DATE  Only return close approaches on the given date, in YYYY-MM-DD format (e.g. 2020-12-31).
  -s START_DATE, --start-date START_DATE
                        Only return close approaches on or after the given date, in YYYY-MM-DD format (e.g. 2020-12-31).
  -e END_DATE, --end-date END_DATE
                        Only return close approaches on or before the given date, in YYYY-MM-DD format (e.g. 2020-12-31).
  --min-distance DISTANCE_MIN
                        In astronomical units. Only return close approaches that pass as far or farther away from Earth as the given
                        distance.
  --max-distance DISTANCE_MAX
                        In astronomical units. Only return close approaches that pass as near or nearer to Earth as the given
                        distance.
  --min-velocity VELOCITY_MIN
                        In kilometers per second. Only return close approaches whose relative velocity to Earth at approach is as fast
                        or faster than the given velocity.
  --max-velocity VELOCITY_MAX
                        In kilometers per second. Only return close approaches whose relative velocity to Earth at approach is as slow
                        or slower than the given velocity.
  --min-diameter DIAMETER_MIN
                        In kilometers. Only return close approaches of NEOs with diameters as large or larger than the given size.
  --max-diameter DIAMETER_MAX
                        In kilometers. Only return close approaches of NEOs with diameters as small or smaller than the given size.
  --hazardous           If specified, only return close approaches of NEOs that are potentially hazardous.
  --not-hazardous       If specified, only return close approaches of NEOs that are not potentially hazardous.
```

Here are a few examples of the `query` subcommand in action:

```
# Show (the first) two close approaches in the data set.
$ python3 main.py query --limit 2
On 1900-01-01 00:11, '170903' approaches Earth at a distance of 0.09 au and a velocity of 16.75 km/s.
On 1900-01-01 02:33, '2005 OE3' approaches Earth at a distance of 0.41 au and a velocity of 17.92 km/s.

# Show (the first) three close approaches on July 29th, 1969.
$ python3 main.py query --date 1969-07-29 --limit 3
On 1969-07-29 01:47, '408982' approaches Earth at a distance of 0.36 au and a velocity of 24.24 km/s.
On 1969-07-29 13:33, '2010 MA' approaches Earth at a distance of 0.21 au and a velocity of 8.80 km/s.
On 1969-07-29 19:56, '464798' approaches Earth at a distance of 0.10 au and a velocity of 8.02 km/s.

# Show (the first) three close approaches in 2050.
$ python3 main.py query --start-date 2050-01-01 --limit 3
On 2050-01-01 04:18, '2019 AY9' approaches Earth at a distance of 0.31 au and a velocity of 8.31 km/s.
On 2050-01-01 06:00, '162361' approaches Earth at a distance of 0.19 au and a velocity of 9.08 km/s.
On 2050-01-01 09:55, '2009 LW2' approaches Earth at a distance of 0.04 au and a velocity of 19.02 km/s.

# Show (the first) four close approaches in March 2020 that passed at least 0.4au of Earth.
$ python3 main.py query --start-date 2020-03-01 --end-date 2020-03-31 --min-distance 0.4 --limit 4
On 2020-03-01 00:28, '152561' approaches Earth at a distance of 0.42 au and a velocity of 11.23 km/s.
On 2020-03-01 09:28, '462550' approaches Earth at a distance of 0.47 au and a velocity of 17.19 km/s.
On 2020-03-02 21:41, '2020 QF2' approaches Earth at a distance of 0.45 au and a velocity of 8.79 km/s.
On 2020-03-03 00:49, '2019 TU' approaches Earth at a distance of 0.49 au and a velocity of 5.92 km/s.

# Show (the first) three close approaches that passed at most 0.0025au from Earth with a relative speed of at most 5 km/s.
# That's slightly less than the average distance between the Earth and the moon.
$ python3 main.py query --max-distance 0.0025 --max-velocity 5 --limit 3
On 1949-01-01 02:53, '2003 YS70' approaches Earth at a distance of 0.00 au and a velocity of 3.64 km/s.
On 1954-03-13 00:00, '2013 RZ53' approaches Earth at a distance of 0.00 au and a velocity of 3.04 km/s.
On 1979-09-02 00:16, '2014 WX202' approaches Earth at a distance of 0.00 au and a velocity of 1.79 km/s.

# Show (the first) three close approaches in the 2000s of NEOs with a known diameter of least 6 kilometers that passed Earth at a relative velocity of at least 15 km/s.
$ python3 main.py query --start-date 2000-01-01 --min-velocity 15 --min-diameter 6 --limit 3
On 2000-05-21 10:08, '7092 (Cadmus)' approaches Earth at a distance of 0.34 au and a velocity of 28.46 km/s.
On 2004-05-25 03:54, '7092 (Cadmus)' approaches Earth at a distance of 0.41 au and a velocity of 30.52 km/s.
On 2006-06-10 20:04, '1866 (Sisyphus)' approaches Earth at a distance of 0.49 au and a velocity of 26.81 km/s.

# Show (the first) two close approaches in January 2030 of NEOs that are at most 50m in diameter and are marked not potentially hazardous.
$ python3 main.py query --start-date 2030-01-01 --end-date 2030-01-31 --max-diameter 0.05 --not-hazardous --limit 2
On 2030-01-07 20:59, '2010 GH7' approaches Earth at a distance of 0.46 au and a velocity of 18.84 km/s.
On 2030-01-13 07:29, '2010 AE30' approaches Earth at a distance of 0.06 au and a velocity of 14.00 km/s.

# Show (the first) three close approaches in 2021 of potentially hazardous NEOs at least 100m in diameter that pass within 0.1au of Earth at a relative velocity of at least 15 kilometers per second.
$ python3 main.py query --start-date 2021-01-01 --max-distance 0.1 --min-velocity 15 --min-diameter 0.1 --hazardous --limit 3
On 2021-01-21 22:56, '363024' approaches Earth at a distance of 0.07 au and a velocity of 15.31 km/s.
On 2021-02-01 22:26, '2016 CL136' approaches Earth at a distance of 0.04 au and a velocity of 18.06 km/s.
On 2021-08-21 15:10, '2016 AJ193' approaches Earth at a distance of 0.02 au and a velocity of 26.17 km/s.

# Save, to a CSV file,  all close approaches.
$ python3 main.py query --outfile results.csv

# Save, to a JSON file, all close approaches in the 2020s of NEOs at least 1km in diameter that pass between 0.01 au and 0.1 au away from Earth.
$ python3 main.py query --start-date 2020-01-01 --end-date 2029-12-31 --min-diameter 1 --min-distance 0.01 --max-distance 0.1 --outfile results.json
```

### `interactive`

There's a third useful subcommand named `interactive`. This subcommand first loads the database and then starts a command loop so that the user can repeatedly run `inspect` and `query` subcommands on the database without having to wait to reload the data each time you want to run a new command.

Here's what an example session might look like:

```
$ python3 main.py interactive
Explore close approaches of near-Earth objects. Type `help` or `?` to list commands and `exit` to exit.

(neo) inspect --pdes 433
NEO 433 (Eros) has a diameter of 16.840 km and is not potentially hazardous.
(neo) help i
Shorthand for `inspect`.
(neo) i --name Halley
NEO 1P (Halley) has a diameter of 11.000 km and is not potentially hazardous.
(neo) query --date 2020-12-31 --limit 2
On 2020-12-31 05:48, '2010 PQ10' approaches Earth at a distance of 0.45 au and a velocity of 21.69 km/s.
On 2020-12-31 16:00, '2015 YA' approaches Earth at a distance of 0.17 au and a velocity of 5.65 km/s.
(neo) q --date 2021-3-14 --min-velocity 10
On 2021-03-14 06:17, '2019 DS1' approaches Earth at a distance of 0.39 au and a velocity of 20.17 km/s.
On 2021-03-14 20:19, '483656' approaches Earth at a distance of 0.06 au and a velocity of 12.09 km/s.
...
```

The prompt is `(neo) `. At the prompt, you can enter either an `inspect` or a `query` subcommand, with the exact same options and behavior as you would on the command line. You can use the special command `quit`, `exit`, or `CTRL+D` to exit this session and return to the command line. The command `help` or `?` shows a help menu, and `help <command>` (e.g. `help query`) shows a help menu specific to that command. In this environment only, you can also use the short forms `i` and `q` for `inspect` and `query` (e.g. `(neo) i --verbose --name Ganymed)`).

Importantly, **the `interactive` session does not automatically update when code is updated.** This means that, if meaningful changes are made to Python files, exiting and restarting the session is necessary. Should the interactive session detect any changes to Python files since its initiation, a warning will be issued before executing each new command. The `interactive` subcommand accepts an optional `--aggressive` argument - if specified, the interactive session will preemptively exit whenever changes to Python files are detected.

All in all, the `interactive` subcommand has the following options:

```
$ python3 main.py interactive --help
usage: main.py interactive [-h] [-a]

Start an interactive command session to repeatedly run `interact` and `query` commands.

optional arguments:
  -h, --help        show this help message and exit
  -a, --aggressive  If specified, kill the session whenever a project file is modified.
```

## Project Files

This is the project scafffolding:

```
.
├── README.md       # This file.
├── main.py
├── models.py       # Task 1.
├── read.py         # Task 2a.
├── database.py     # Task 2b and Task 3b.
├── filters.py      # Task 3a and Task 3c.
├── write.py        # Task 4.
├── helpers.py
├── data
│   ├── neos.csv
│   └── cad.json
├── data_output
│   ├── results.csv
│   └── results.json
└── tests
    ├── test-neos-2020.csv
    ├── test-cad-2020.json
    ├── test_*.py
    ├── ...
    └── test_*.py
```

This project encompasses several files and folders, each serving a specific purpose:

- `main.py`: This Python script serves as the command-line tool's main interface, orchestrating the data pipeline by invoking the defined functions and classes. This file remains unmodified.
- `models.py`: This file defines Python objects representing a `NearEarthObject` and a `CloseApproach`. These objects possess attributes, a human-readable string representation, and potentially some properties or methods.
- `extract.py`: Functions to read information from data files are written here, creating `NearEarthObject`s and `CloseApproaches` from the data.
- `database.py`: The `NEODatabase` class defined in this file encapsulates the entire data set, linking NEOs and close approaches. Methods to retrieve NEOs by primary designation and name are included, alongside a method to query the dataset with user-specified filters to produce an iterable stream of matching results.
- `filters.py`: A variety of filters for use with the `NEODatabase` are created in this file to query for matching close approaches. Additionally, a utility function to limit the number of results from a stream is provided.
- `write.py`: Functions to write a stream of results (the `CloseApproach` objects generated by the `NEODatabase`) to a file in either JSON or CSV format are implemented here.
- `helpers.py`: This module offers utility functions to assist in converting to and from datetime objects.

The data files are located in the `data/` folder.

The data files created by the tool are located in the `data_output/` folder.

The unit tests all live in the `tests/` folder.

Here's the revised text with improved English:

## Project Tasks Completed

- Task 1: Developed models to represent the data. (Located in `models.py`)
- Task 2: Extracted the data into a custom-built database. (Implemented in `extract.py` and `database.py`)
- Task 3: Created filters for querying the database to generate a stream of matching `CloseApproach` objects and limited the result size. (Developed in `filters.py` and `database.py`)
- Task 4: Implemented functionality to save the data to a file. (Contained in `write.py`)

### Testing

All unit tests can be executed with the following command:

```
$ python3 -m unittest
.........................................................................
----------------------------------------------------------------------
Ran 73 tests in 2.022s

OK
```

