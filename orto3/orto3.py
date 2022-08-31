import os
import sys
import orgparse
import logging
ORG = 'fakeorg.org'

defaults_module = {
        "summary" : "No summary",
        "author" : "BSL",
        "category" : "Uncatgeorized",
}
ORG = orgparse.load(ORG)
ROOTPATH = os.getcwd()

class OrgExporter:
    def __init__(self, ORG, ROOTPATH):
        self.rootpath = ROOTPATH
        self.org = ORG

    def write_manifest(self, manifest):
        with open('___manifest__.py', 'w') as f:
            f.write(manifest)

    def replace_manifest(self, dict):
        replacers = []
        for k in dict.keys():
            replacers.append((k, dict[k]))
        template = templates.tm['__manifest__.py']
        return templates.replace_template(template, replacers)

    def export_module(self, node):
        module_keys = {}
        logging.info(f"Module guy: {node.heading}")
        description = node.body
        prop = node._properties
        for p in defaults_module.keys():
            if p not in prop:
                module_keys[p]=defaults_module[p]
            else:
                module_keys[p]=prop[k]
        self.makedir(prop['Name'])
        manifest = self.replace_manifest(module_keys)
        self.write_manifest(manifest)

    def export_model(self, node):
        module_keys = {}
        logging.info(f"Model guy: {node.heading}")
        description = node.body
        prop = node._properties

    def export_field(self, node):
        module_keys = {}
        logging.info(f"Field guy: {node.heading}")
        description = node.body
        prop = node._properties

    def export(self):
        logging.info("\n\n*** BUILD STARTED ***")
        for node in self.org:
            if "ExportType" in node._properties:
                logging.info("Exportable guy")
                if "Module" == node._properties["ExportType"]:
                    self.export_module(node)
                if "Model" in node._properties:
                    self.export_model(node)
                if "FieldType" in node._properties:
                    self.export_field(node)
        logging.info("*** BUILD ENDED ***")


def main():
    logging.basicConfig(filename='build.log', filemode='a+', level=logging.INFO)
    OE = OrgExporter(ORG, ROOTPATH)
    OE.export()
main()
