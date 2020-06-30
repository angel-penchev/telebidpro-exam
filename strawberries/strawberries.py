"""
A simulation of a field with rotten strawberries spreading decease.

Usage:
    The script could be started by running the following::
        $ python strawberries.py

    For more information run the following::
        $ python strawberries.py --help
"""
import re
import argparse
from enum import Enum
from typing import List, Tuple

import matplotlib.pyplot as plt


class GraphType(Enum):
    """Enum for types of graph to be displayed."""
    GUI = "GUI"
    TEXT = "Text"
    NONE = "None"


def main(graph_type: GraphType = GraphType.GUI):
    """
    A simulation of a field with rotten strawberries spreading decease.

    Parameters:
    -----------
    graph_type : GraphType
        Type of graph to be displayed.

    Returns:
    --------
    None.
    """

    # Initializing a field filled with 1s (intact strawberries) with size from input
    rows, columns, itterations = parse_user_input(3)
    field = [[1 for j in range(columns)] for i in range(rows)]

    # Parsing information about the first rotten strawberry
    rotten1_x, rotten1_y = parse_user_input(2)

    # (Optional) Parsing information about the second rotten strawberry
    field[rotten1_x - 1][rotten1_y - 1] = 0
    try:
        rotten2_x, rotten2_y = parse_user_input(2, optional=True)
        field[rotten2_x - 1][rotten2_y - 1] = 0
    except UnboundLocalError:
        pass

    # Displaying initial itteration
    if graph_type.value == "GUI":
        annotation = plot_annotatate(field, 0)
        plt.imshow(field)
        plt.pause(0.5)
    elif graph_type.value == "Text":
        print_field(field)

    for itter in range(itterations):
        # Copying the field list so the new infections are not considered in the
        # same itteration.
        new_field = [row.copy() for row in field]

        # Itterating over the whole field; for each cell with 0 -> infect neighbours
        for i, row in enumerate(field):
            for j, cell in enumerate(row):
                if cell == 0:
                    rot_neighbours(new_field, (i, j))
        field = new_field

        if graph_type.value == "GUI":
            # Adding annotation with current plot stats
            annotation = plot_annotatate(field, itter + 1, annotation)

            # Pause between plots
            plt.pause(3/itterations)

            # Displaying current itteration
            plt.imshow(field)
        elif graph_type.value == "Text":
            print_field(field)

    # Displaying final information
    if graph_type.value == "GUI":
        plt.show()
    elif graph_type.value == "Text":
        print_field(field)
    print(sum([row.count(1) for row in field]))


def parse_user_input(expected_outputs: int, optional: bool = False):
    """
    Parsing a user input into an array of intigers.

    Parameters:
    -----------
    expected_outputs : int
        The amount of output expected to be parsed. Exception is raised on mismatch.
    optional : bool (default: False)
        If true a new line "\\n" input is valid too.

    Returns:
    --------
    List[int] if everything is parsed correctly or None if optional is set to True and
    no input is provided.

    Raises:
    -------
    IOError
        On unparsable input or on input with wrong length.
    """

    data = input()

    # Removing all spacing between characters and spliting by commas (",")
    data = data.strip(" \t\n\r")
    data = re.split(r",\s", data)

    # Exception on wrong number of arguments passed
    if not optional and len(data) != expected_outputs:
        raise IOError

    if data:
        return [int(i) for i in data]
    return None


def print_field(field: List[List[int]]):
    """
    Prints strawberry field array.

    Parameters:
    -----------
    field : List[List[int]]
        Strawberry 2D field.

    Returns:
    --------
    None.
    """

    for row in field:
        print(row)
    print("\n")


def rot_neighbours(field: List[List[int]], coords: Tuple[int, int]):
    """
    Takes coordinates on a field and infects all neighbours.

    Parameters:
    -----------
    field : List[List[int]]
        Strawberry 2D field.
    coords : Tuple[int, int]
        Coordinates (x, y) of which the neighbours to be infected.

    Returns:
    --------
    None.
    """

    i, j = coords
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for direction in directions:
        # Checking if the index is not going out of bounds and replacing values with 0s
        if not i - direction[0] < 0 and not j - direction[1] < 0:
            try:
                field[i - direction[0]][j - direction[1]] = 0
            except IndexError:
                pass


def plot_annotatate(field: List[List[int]], itter: int, annotation: plt.annotate = None):
    """
    Adds an preset annotation to the plot.

    Parameters:
    -----------
    field : List[List[int]]
        Strawberry 2D field.
    itter : int
        Current itteration index.
    annotation : plt.annotate (default: None)
        Previous annotation to be updated.

    Returns:
    --------
    A new matplotlib annotation.
    """

    if annotation:
        annotation.remove()

    intact_amount = sum([row.count(1) for row in field])
    rotten_amount = len(field) * len(field[1]) - intact_amount

    annotation_string = "Itteration: {}, Intact: {}, Rotten: {}".format(
        itter, intact_amount, rotten_amount)

    return plt.annotate(annotation_string, (0, 0), (0, -20), xycoords="axes fraction",
                        textcoords="offset points", va="top")


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument("-g", "--graph-type", dest="graph_type", action="store",
                        choices=["GUI", "Text", "None"], default="GUI",
                        help="graph display type - GUI, Text or None (default: GUI)")

    ARGS = PARSER.parse_args()
    main(GraphType[ARGS.graph_type.upper()])
