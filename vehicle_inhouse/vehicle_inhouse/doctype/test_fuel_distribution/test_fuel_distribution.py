# Copyright (c) 2025, Ritesh Sharma and contributors
# For license information, please see license.txt
'''
# import frappe
from frappe.model.document import Document


class TestFuelDistribution(Document):
	pass
'''

import frappe
from frappe.utils import flt
from frappe.model.document import Document

class TestFuelDistribution(Document):
    def on_submit(self):
        town = self.tfd_town_project
        issued_qty = flt(self.tfd_issued_quantity)

        if town and issued_qty > 0:
            stock_name = frappe.get_value("Test Fuel Stock", {"tfs_town_project": town}, "name")
            if stock_name:
                stock_doc = frappe.get_doc("Test Fuel Stock", stock_name)
                stock_doc.tfs_storage = flt(stock_doc.tfs_storage or 0) - issued_qty
                if stock_doc.tfs_storage < 0:
                    frappe.throw(f"Not enough stock in {town}. Available: {flt(stock_doc.tfs_storage or 0)}")
                stock_doc.save()
                frappe.msgprint(f"{issued_qty} liters issued from {town}. Updated stock: {stock_doc.tfs_storage}")
            else:
                frappe.throw(f"No stock record found for {town}")

        # 👉 Create new entry in Test Fuel for Vehicle
        if self.tfd_vehicle and issued_qty > 0:
            vehicle_fuel_doc = frappe.new_doc("Test fuel for Vehicle")
            vehicle_fuel_doc.tffv_vehicle_name = self.tfd_vehicle
            vehicle_fuel_doc.tffv_quantity = issued_qty
            vehicle_fuel_doc.insert()
            frappe.msgprint(f"New record created in Test Fuel for Vehicle for '{self.tfd_vehicle}' with {issued_qty} liters.")

#Perfect wowking for Stock Deduction
"""
import frappe
from frappe.utils import flt
from frappe.model.document import Document

class TestFuelDistribution(Document):
    def on_submit(self):
        town = self.tfd_town_project
        issued_qty = flt(self.tfd_issued_quantity)

        if town and issued_qty > 0:
            stock_name = frappe.get_value("Test Fuel Stock", {"tfs_town_project": town}, "name")
            if stock_name:
                stock_doc = frappe.get_doc("Test Fuel Stock", stock_name)
                stock_doc.tfs_storage = flt(stock_doc.tfs_storage or 0) - issued_qty
                if stock_doc.tfs_storage < 0:
                    frappe.throw(f"Not enough stock in {town}. Available: {flt(stock_doc.tfs_storage or 0)}")
                stock_doc.save()
                frappe.msgprint(f"{issued_qty} liters issued from {town}. Updated stock: {stock_doc.tfs_storage}")
            else:
                frappe.throw(f"No stock record found for {town}")
"""