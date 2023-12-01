import xml.etree.ElementTree as ET

class VersionChangeError(Exception):
    pass

def version_change(pom_path):
    try:
        tree = ET.parse(pom_path)
        root = tree.getroot()
        version_element = root.find(".//project/version")

        if version_element is not None:
            major, minor, patch = map(int, version_element.text.split('.'))
            patch += 1

            new_version = f'{major}.{minor}.{patch}'
            version_element.text = new_version

            tree.write(pom_path)
        else:
            raise Exception('Element <version> not found in the <project> section.')

    except Exception as e:
        raise Exception(f'Error: {e}')

if __name__ == "__main__":
    pom_path = 'path/to/your/project/pom.xml'
    try:
        version_change(pom_path)
    except VersionChangeError as ve:
        raise Exception('Could not change version')
