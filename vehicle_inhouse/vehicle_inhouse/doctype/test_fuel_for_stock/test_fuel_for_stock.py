# Copyright (c) 2025, Ritesh Sharma and contributors
# For license information, please see license.txt
'''
# import frappe
from frappe.model.document import Document


class TestFuelforStock(Document):
	pass
'''

import frappe
from frappe.utils import flt
from frappe.model.document import Document


class TestFuelforStock(Document):
    
    def on_submit(self):
        town = self.tffs_town_project
        qty = flt(self.quantity)

        if town and qty > 0:
            existing_stock = frappe.get_value(
                "Test Fuel Stock",
                {"tfs_town_project": town},
                "name"
            )
            
            if existing_stock:
                fs_doc = frappe.get_doc("Test Fuel Stock", existing_stock)
                fs_doc.tfs_storage = flt(fs_doc.tfs_storage or 0) + qty
                fs_doc.save()
                frappe.msgprint(f"Fuel Stock for '{town}' updated. Added {qty} liters.")
            else:
                fs_doc = frappe.new_doc("Test Fuel Stock")
                fs_doc.tfs_town_project = town
                fs_doc.tfs_storage = qty
                fs_doc.insert()
                frappe.msgprint(f"Fuel Stock for '{town}' created with {qty} liters.")




'''
import frappe
from frappe.utils import flt
from frappe.model.document import Document


class TestFuelforStock(Document):
    def on_submit(self):
        town = self.tffs_town_project
        qty = flt(self.quantity)

        if town and qty > 0:
            existing_stock = frappe.get_value(
                "Test Fuel Stock",
                {"tfs_town_project": town},
                "name"
            )

            if existing_stock:
                fs_doc = frappe.get_doc("Test Fuel Stock", existing_stock)
                fs_doc.tfs_storage = flt(fs_doc.tfs_storage or 0) + qty
                fs_doc.save()
            else:
                fs_doc = frappe.new_doc("Test Fuel Stock")
                fs_doc.tfs_town_project = town
                fs_doc.tfs_storage = qty
                fs_doc.insert()






import frappe
from frappe.utils import flt
from frappe.model.document import Document


class TestFuelforStock(Document):
	 def on_submit(self):
          town = self.tffs_town_project
          qty = flt(self.quantity)

          if town and qty > 0:
            existing_stock = frappe.get_value(
                "Fuel Stock",
                {"tfs_town_project": town},
                "name"
            )

            if existing_stock:
                fs_doc = frappe.get_doc("Fuel Stock", existing_stock)
                fs_doc.tfs_storage = flt(fs_doc.tfs_storage or 0) + qty
                fs_doc.save()
            else:
                fs_doc = frappe.new_doc("Fuel Stock")
                fs_doc.tfs_town_project = town
                fs_doc.tfs_storage = qty
                fs_doc.insert()
        '''