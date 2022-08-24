with open('./reference_proj/__init__.py') as f:
    init_template = f.read()

with open('./reference_proj/__manifest__.py') as f:
    manifest_template = f.read()

with open('./reference_proj/models/models.py') as f:
    model_file_template = f.read()

with open('./reference_proj/models/__init__.py') as f:
    model_init_file_template = f.read()

with open('./reference_proj/security/ir.model.access.csv') as f:
    ir_model_access_csv_template = f.read()

with open('./reference_proj/views/views.xml') as f:
    views_skeleton_template = f.read()

model_header_template = """
#-*- coding: utf-8 -*-

from odoo import models, fields, api

"""

model_top_template = """

class model_class_name_replace(models.model_type_replace):
    _name = 'model_class_dotted_name_replace'
    _description = 'description_replace'


"""

odoo_header_template = """
<odoo>
    <data>
"""

odoo_footer_template = """
    </data>
</odoo>
"""

list_view_definition_template = """
      <record model="ir.ui.view" id="model_name_replace.list">
          <field name="name">model_name_replace list</field>
          <field name="model">module_name_replace.model_name_replace</field>
          <field name="arch" type="xml">
              <tree>
              fields_section_replace
              </tree>
          </field>
      </record>
"""

actions_opening_views_on_models_template = """
      <record model="ir.actions.act_window" id="model_name_replace.action_window">
          <field name="name">model_name_replace window</field>
          <field name="res_model">module_name_replace.model_name_replace</field>
          <field name="view_mode">tree,form</field>
      </record>
"""

server_actions_template = """
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
      </record>
"""

field_template = """
    field_name_replace = fields.field_type_replace(field_metadata_replace)
"""

top_menuitem_template = """
      <menuitem name="module_name_replace" id="module_name_replace.menu_root"/>

"""

menuitem_categories_template = """
      <menuitem name="menu_title_name_replace" id="model_name_replace.menu_1" parent="model_name_replace.menu_root"/>

"""

menuitem_actions_template = """
      <menuitem name="menu_item_name_replace" id="module_name_replace.menu_1_list" parent="module_name_replace.menu_1"
                action="module_name_replace.action_window"/>
      <menuitem name="Server to list" id="module_name_replace" parent="module_name_replace.menu_1"
                action="module_name_replace.action_server"/>


"""
