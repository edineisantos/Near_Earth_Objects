"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object,
    such as its primary designation (required, unique), IAU name (optional),
    diameter in kilometers (optional - sometimes unknown), and whether it's
    marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(
            self,
            designation,
            name=None,
            diameter=float('nan'),
            hazardous=False):
        """Create a new `NearEarthObject`.

        :param designation: The primary designation for this NearEarthObject.
        :param name: The IAU name for this NearEarthObject.
        :param diameter: The diameter, in kilometers, of this NearEarthObject.
        :param hazardous: Whether or not this NearEarthObject is potentially
                        hazardous.
        """
        self.designation = designation
        self.name = name if name else None
        self.diameter = float(diameter) if diameter else float('nan')
        self.hazardous = bool(hazardous)

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return f"{self.designation} ({self.name})"
        else:
            return self.designation

    def __str__(self):
        """Return `str(self)`."""
        hazardous_status = "is" if self.hazardous else "is not"
        return (
            f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km "
            f"and {hazardous_status} potentially hazardous.")

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation."""
        return (f"NearEarthObject(designation={self.designation!r}, "
                f"name={self.name!r}, diameter={self.diameter:.3f}, "
                f"hazardous={self.hazardous!r})")


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach
    to Earth, such as the date and time (in UTC) of closest approach, the
    nominal approach distance in astronomical units, and the relative approach
    velocity in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation, time, distance, velocity, neo=None):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the
        constructor.
        """
        self._designation = designation
        self.time = cd_to_datetime(time)
        self.distance = float(distance)
        self.velocity = float(velocity)
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't exist
        in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # Formatting the approach time
        formatted_time = datetime_to_str(self.time)

        # Building the fullname for NEO
        fullname = f"{self._designation} ({self.neo.name})" \
            if self.neo and self.neo.name else self._designation

        # Return a string that includes both the NEO's fullname and the
        # formatted time
        return f"Object '{fullname}' had a close approach at {formatted_time}"

    def __str__(self):
        """Return `str(self)`."""
        return (
            f"{self.time_str}, "
            f"approaching Earth at a distance of {self.distance:.2f} au and a "
            f"velocity of {self.velocity:.2f} km/s."
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation."""
        return (f"CloseApproach(time={self.time_str!r}, "
                f"distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, "
                f"neo={self.neo!r})")

    def serialize(self, to_csv=False):
        """Serialize the CloseApproach data into a dictionary for CSV or JSON
        output.

        :param to_csv: Boolean indicating if the serialization is for CSV
        output.
        :return: A dictionary of serialized data.
        """
        if to_csv:
            # Flatten the structure for CSV output
            return {
                "datetime_utc": datetime_to_str(self.time),
                "distance_au": self.distance,
                "velocity_km_s": self.velocity,
                "designation": self.neo.designation if self.neo else '',
                "name": self.neo.name if self.neo and self.neo.name else '',
                "diameter_km": (self.neo.diameter
                                if self.neo and self.neo.diameter else 'nan'),
                "potentially_hazardous": (str(self.neo.hazardous)
                                          if self.neo else 'False')
            }
        else:
            # Nested structure for JSON output
            return {
                "datetime_utc": datetime_to_str(self.time),
                "distance_au": self.distance,
                "velocity_km_s": self.velocity,
                "neo": {
                    "designation": self.neo.designation if self.neo else '',
                    "name": (
                        self.neo.name if self.neo and self.neo.name else ''
                    ),
                    "diameter_km": (
                        self.neo.diameter
                        if self.neo and self.neo.diameter else 'nan'
                    ),
                    "potentially_hazardous": (
                        self.neo.hazardous if self.neo else False
                    )
                }
            }
