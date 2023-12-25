"""A database encapsulating collections of near-Earth objects and their close
approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.
"""


class NEODatabase:
    """Create a new `NEODatabase`.

    This class represents a database of near-Earth objects (NEOs) and their
    close approaches. It contains a collection of NEOs and a collection of
    close approaches. It also maintains auxiliary data structures to fetch
    NEOs by primary designation or by name and to speed up querying for
    close approaches that match certain criteria.
    """

    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        This constructor assumes that the collections of NEOs and close
        approaches haven't yet been linked. Specifically, the `.approaches`
        attribute of each `NearEarthObject` should resolve to an empty
        collection, and the `.neo` attribute of each `CloseApproach` should
        be None.

        However, each `CloseApproach` should have an attribute
        (`._designation`) that matches the `.designation` attribute of the
        corresponding NEO. This constructor modifies the supplied NEOs and
        close approaches to link them together.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        self._neos = neos
        self._approaches = approaches

        # Auxiliary data structures
        self._designation_dict = {neo.designation: neo for neo in neos}
        self._name_dict = {neo.name: neo for neo in neos if neo.name}

        # Link NEOs and their close approaches
        for approach in approaches:
            neo = self._designation_dict.get(approach._designation)
            if neo:
                approach.neo = neo
                neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead. Each NEO in the data set
        has a unique primary designation, as a string. The matching is exact -
        check for spelling and capitalization if no match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation,
        or `None`.
        """
        return self._designation_dict.get(designation, None)

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead. Not every NEO in the
        data set has a name. No NEOs are associated with the empty string nor
        with the `None` singleton. The matching is exact - check for spelling
        and capitalization if no match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        return self._name_dict.get(name, None)

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of
        filters.

        This generates a stream of `CloseApproach` objects that match all of
        the provided filters. If no arguments are provided, generate all known
        close approaches. The `CloseApproach` objects are generated in internal
        order, which isn't guaranteed to be sorted meaningfully, although is
        often sorted by time.

        :param filters: A collection of filters capturing user-specified
        criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            if all(f(approach) for f in filters):
                yield approach
