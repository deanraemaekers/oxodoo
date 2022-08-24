import re
import gen_templates
from orgparse import load, loads
gn = gen_templates
ORG = 'fake_seta.org'
root = load(ORG)
proj = 'proj'+ORG
import os
global root_path
root_path = os.getcwd()+"/"+proj 


def build_tree_action(properties, fields, model, modulefolder):
    actioner ="""<!-- actions opening views on models -->
      
      <record model="ir.actions.act_window" id="model_name_replace.action_window">
          <field name="name">model_name_replace window</field>
          <field name="res_model">module_name_replace.model_name_replace</field>
          <field name="view_mode">tree,form</field>
      </record>


    <!-- server action to the one above -->
      
      <record model="ir.actions.server" id="model_name_replace.action_server">
          <field name="name">model_name_replace server</field>
          <field name="model_id" ref="module_name_replace.model_name_replace"/>
          <field name="state">code</field>
          <field name="code">
              action = {
              "type": "ir.actions.act_window",
              "view_mode": "tree,form",
              "res_model": model._name,
              }
          </field>
      </record>"""
    actioner_actual = re.sub("model_name_replace", model, actioner)
    actioner_actual = re.sub("module_name_replace", modulefolder, actioner_actual)
    return actioner_actual

def build_tree_view(properties, fields, model, modulefolder):
    tree_view_topper = "<odoo>\n  <data>\n"
    tree_view_comment = f"    \n\n<!-- tree view for {properties['Name']} -->\n\n"
    tree_view_record = f'        <record model="ir.ui.view" id="{properties["ID"]}">\n'
    tree_view_os_stuff = f'            <field name="name">{properties["Name"]}</field>\n'
    tree_view_os_stuff += f'            <field name="model">{model}</field>\n'
    tree_view_os_stuff += '            <field name="arch" type="xml">\n\n'
    tree_view_field = "            <tree>\n"
    for field in fields:
        field_properties = field._properties
        field_name = field_properties['Name']
        tree_view_field += f"                <field name='{field_name}'/>\n"
    tree_view_end_tree = '            </tree>\n'
    tree_view_end_tree += '        </record>\n'
    tree_action = build_tree_action(properties, fields, model, modulefolder)
    tree_total = tree_view_topper + tree_view_comment + tree_view_record + tree_view_os_stuff + tree_view_field + tree_view_end_tree + tree_action
    return tree_total





def fensure(folder, modulepath):
    fchange(root_path)
    fchange(modulepath)


def fcreate(folder):
    try:
        os.mkdir(folder)
    except:
        pass
    return

def fchange(folder):
    try:
        os.chdir(folder)
    except Exception as e:
        raise AssertionError(f'No folder: {e}')
    return

fcreate(proj)
fchange(proj)

a = 0
for module in root.children[0]:
    moduledescription = str(module.body)
    properties = module._properties
    if "Summary" in properties:
        modulesummary = properties['Summary']
        modulefolder = properties['Folder']
        modulewebsite = properties['Website']
        moduledepends = properties['Depends']

        # make module folder
        fcreate(modulefolder)
        fchange(modulefolder)
        modulepath = modulefolder

        # make the manifest
        manifest = re.sub("reference_proj", modulefolder, gn.manifest_template)
        manifest = re.sub("proj_description_replace", moduledescription, manifest)
        manifest = re.sub("proj_author_replace", 'BSL', manifest)
        manifest = re.sub("proj_website_replace", modulewebsite, manifest)
        manifest = re.sub("proj_depends_list_replace", moduledepends, manifest)
        with open('__manifest__.py', 'w') as f:
            f.write(manifest)
        # make the init
        moduleinit = gn.init_template
        with open('__init__.py', 'w') as f:
            f.write(moduleinit)



    fcreate(root_path+"/"+modulefolder+"/"+"models")
    fchange(root_path+"/"+modulefolder+"/"+"models")
    for model in module.children:
        # make models folder
        properties = model._properties
        if "ModelType" in properties:
            modeltype = properties['ModelType']
            modelname = properties['Name']
            modelclassname = properties['Class']
            modeldescription = properties['Description']
            modelfilename = properties['FileName']
            with open(modelfilename, 'w') as f:
                f.write(gn.model_header_template)
            model_top = re.sub("class_name_replace", modelclassname, gn.model_top_template)
            model_top = re.sub("model_class_dotted_name_replace", modelname, model_top)
            model_top = re.sub("description_replace", modeldescription, model_top)
            model_top = re.sub("model_type_replace", modeltype, model_top)
            fchange(root_path+"/"+modulefolder+"/"+"models")
            with open(modelfilename, 'a+') as f:
                f.write(model_top)


            for field in model.children:
                properties = field._properties
                if "FieldName" in properties:
                    fieldname = properties['FieldName']
                    fieldtype = properties['FieldType']
                    fieldmaxlength = properties['MaxLength']
                    fieldrequired = properties['Required']
                    fieldmetadata = ""

                    if fieldmaxlength:
                        fieldmetadata += f"length={fieldmaxlength} "
                    if fieldrequired:
                        fieldmetadata += f"required=True "

                    field_actual = f"    {fieldname} = fields.{fieldtype}({fieldmetadata})\n"
                    with open(modelfilename, 'a+') as f:
                        f.write(field_actual)

                elif "Holder" in properties:
                    if properties['Holder'] == 'Views':
                        fcreate(root_path+"/"+modulefolder+"/"+'views')
                        fchange(root_path+"/"+modulefolder+"/"+'views')
                        for view in field.children:
                            properties = view._properties
                            viewtype = properties['ViewType']
                            viewmodel = properties['ViewMode']
                            viewid = properties['ID']
                            viewname = properties['Name']
                            for elems in view.children:
                                if "Tree" in elems.heading:
                                    fields = elems.children
                                    tree_view_built = build_tree_view(properties, fields, modelname, modulefolder)
                                    fchange(root_path+"/"+modulefolder+"/"+'views')
                                    with open('views.xml', 'a+') as f:
                                        f.write(tree_view_built)



                






