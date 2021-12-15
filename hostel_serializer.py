from pathlib import Path
import xml.etree.ElementTree as ElTr
import json


class HostelSerializer:

    def serialize(self, data: list, form: str, path: Path, name: str):
        serializer = self._get_serializer(form)
        return serializer(data, path, name)

    def _get_serializer(self, form: str):
        if form == "JSON":
            return self._serialize_to_json
        elif form == "XML":
            return self._serialize_to_xml

    @staticmethod
    def _serialize_to_json(data: list, path: Path, name: str):
        output_file = Path(path, f"{name}.json")
        with open(output_file, "w") as file:
            json.dump(data, file, indent="\t")

    @staticmethod
    def _serialize_to_xml(data: list, path: Path, name: str):
        output_file = Path(path, f"{name}.xml")
        root = ElTr.Element(name)
        for source_dict in data:
            element = ElTr.SubElement(root, "room")
            for key, value in source_dict.items():
                sub_element = ElTr.SubElement(element, str(key).lower())
                sub_element.text = str(value)
        tree = ElTr.ElementTree(root)
        tree.write(output_file, encoding="UTF-8", xml_declaration=True)
