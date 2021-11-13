"""Create PyGameGUI UI layouts using XML
This module is intended to be used as an extension for PyGame GUI.
Users write their layouts in xml and the system parses that xml
and creates the nested structure of the gui.
"""
from typing import Tuple, Union
from pathlib import Path
from xml.etree import ElementTree
from pygame_gui.core.ui_element import UIElement
from pygame_gui.ui_manager import UIManager


# This module is built to support the following version of pygame_gui
__version__ = "0.5.7"

_AnyPath = Union[Path, str]


def build_from_file(file_path: _AnyPath, ui_manager: UIManager, screen_size: Tuple[int, int]) -> None:
    """Create a UI layout from XML data and add it to the given UIManager

    Args:
        file_path (Union[Path, str]): path to XML file containing UI layout
        ui_manager (UIManager): UI Manager to add the UIElements to
        screen_size (Tuple[int, int]): Width and Height of the game window
    """
    pass


def build_from_string(xml_str: str, ui_manager: UIManager, screen_size: Tuple[int, int]) -> None:
    """Create a UI layout from XML data and add it to the given UIManager

    Args:
        xml_str (str): string containing XML data containing UI layout
        ui_manager (UIManager): UI Manager to add the UIElements to
        screen_size (Tuple[int, int]): Width and Height of the game window
    """
    pass


def _build_from_xml(xml_tree: ElementTree, ui_manager: UIManager, screen_size: Tuple[int, int]) -> None:
    """Create a UI layout from XML data and add it to the given UIManager

    Args:
        xml_tree (xml.etree.ElementTree): XML tree containing UI layout
        ui_manager (UIManager): UI Manager to add the UIElements to
        screen_size (Tuple[int, int]): Width and Height of the game window
    """
    pass
