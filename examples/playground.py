import os
from pathlib import Path
import xml.etree.ElementTree as XMLElementTree


def main():
    examples_dir = Path(os.path.abspath(__file__)).parent

    xml_tree = XMLElementTree.parse(examples_dir / 'sample_01.xml')
    xml_tree_root = xml_tree.getroot()

    for elem in xml_tree_root.iter():
        print("Tag: {}, Attributes: {}".format(
            elem.tag,
            elem.attrib.items()
        ))


if __name__ == "__main__":
    main()
