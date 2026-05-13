# Copyright (c) 2025, Ritesh Sharma and contributors
# For license information, please see license.txt



                # ----  MAIN CODE 20/4/26  (FINAL WORKING)----- 

# import frappe
# from frappe.model.document import Document
# from frappe.utils import flt, nowdate


# class FuelDistribution(Document):

#     def on_submit(self):
#         frappe.db.savepoint("fuel_distribution_submit")
#         try:
#             town = self.fd_town_project
#             vehicle = self.fd_vehicle_name
#             issued_qty = flt(self.issued_quantity_ltr)
#             fuel_type = self.fd_fuel_type

#             if not town:
#                 frappe.throw("⚠️ Town/Project is required.")
#             if issued_qty <= 0:
#                 frappe.throw("⚠️ Issued quantity must be greater than zero.")
#             if not fuel_type:
#                 frappe.throw("⚠️ Fuel Type is required.")
#             if not self.supplier_name:
#                 frappe.throw("⚠️ Supplier Name is required.")
#             if not self.warehouse:
#                 frappe.throw("⚠️ Warehouse is required.")

#             self.create_purchase_receipt()
#             self.create_material_issue()
#             self.update_fuel_stock(town, issued_qty, fuel_type)

#             if vehicle:
#                 self.create_vehicle_fuel_record(vehicle, town, issued_qty, fuel_type)

#         except Exception:
#             frappe.db.rollback(save_point="fuel_distribution_submit")
#             raise

#     # ─────────────────────────────────────────
#     # PURCHASE RECEIPT
#     # ─────────────────────────────────────────
#     def create_purchase_receipt(self):
#         # ✅ Pehle duplicate check
#         if frappe.db.exists("Purchase Receipt", 
#                 {"remarks": f"Fuel Distribution: {self.name}"}):
#             return

#         pr = frappe.new_doc("Purchase Receipt")
#         pr.supplier = self.supplier_name
#         pr.company = self.company
#         pr.set_posting_time = 1
#         pr.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD

#         pr.append("items", {
#             "item_code": self.fd_fuel_type,
#             "qty": self.issued_quantity_ltr,
#             "rate": 0,
#             "warehouse": self.warehouse
#         })

#         pr.insert(ignore_permissions=True)
#         pr.submit()

#         self.db_set("custom_purchase_receipt", pr.name)
#         frappe.msgprint(f"✅ Purchase Receipt Created: {pr.name}")

#     # ─────────────────────────────────────────
#     # MATERIAL ISSUE
#     # ─────────────────────────────────────────
#     def create_material_issue(self):
#         # ✅ Pehle duplicate check
#         if frappe.db.exists("Stock Entry", 
#                 {"remarks": f"Fuel Distribution: {self.name}"}):
#             return

#         se = frappe.new_doc("Stock Entry")
#         se.stock_entry_type = "Material Issue"
#         se.company = self.company
#         se.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD

#         se.append("items", {
#             "item_code": self.fd_fuel_type,
#             "qty": self.issued_quantity_ltr,
#             "s_warehouse": self.warehouse
#         })

#         se.insert(ignore_permissions=True)
#         se.submit()

#         self.db_set("custom_material_issue", se.name)
#         frappe.msgprint(f"📦 Material Issue Created: {se.name}")

#     # ─────────────────────────────────────────
#     # FUEL STOCK MINUS
#     # ─────────────────────────────────────────
#     def update_fuel_stock(self, town, issued_qty, fuel_type):
#         result = frappe.db.get_value(
#             "Fuel Stock",
#             {"fuel_stock_town_project": town},
#             ["name", "fuel_stock_fuel_storage", "fs_petrol"],
#             as_dict=True
#         )

#         if not result:
#             frappe.throw(
#                 f"❌ No Fuel Stock found for <b>{town}</b>."
#             )

#         if fuel_type == "Diesel":
#             current_stock = flt(result.fuel_stock_fuel_storage or 0)
#             stock_field = "fuel_stock_fuel_storage"
#         else:
#             current_stock = flt(result.fs_petrol or 0)
#             stock_field = "fs_petrol"

#         if current_stock < issued_qty:
#             frappe.throw(
#                 f"⛔ Not enough {fuel_type} stock in <b>{town}</b>.<br>"
#                 f"Available: {current_stock} L | Requested: {issued_qty} L"
#             )

#         new_stock = current_stock - issued_qty
#         frappe.db.set_value("Fuel Stock", result.name, stock_field, new_stock)

#         frappe.msgprint(
#             msg=f"""
#                 <div style="padding:10px;text-align:center;">
#                     <h3 style="color:#2e7d32;">⛽ {fuel_type} Stock Updated</h3>
#                     <p><b>Town:</b> {town}</p>
#                     <p><b>Issued:</b> {issued_qty} L</p>
#                     <p><b>Remaining:</b> {new_stock} L</p>
#                 </div>
#             """,
#             title="✅ Stock Deducted",
#             indicator="green"
#         )

#     # ─────────────────────────────────────────
#     # FUEL FOR VEHICLE
#     # ─────────────────────────────────────────
#     def create_vehicle_fuel_record(self, vehicle, town, issued_qty, fuel_type):
#         placeholder_url = "https://cdn-icons-png.flaticon.com/512/1587/1587658.png"

#         vf = frappe.new_doc("Fuel for Vehicle")
#         vf.date = nowdate()
#         vf.town = town
#         vf.vehicle_details = vehicle
#         vf.vehicle_reading = self.vehicle_reading_km
#         vf.types_of_fuel = fuel_type
#         vf.quantity = issued_qty
#         vf.rate = 0
#         vf.upload_invoice__invoice_copy = placeholder_url
#         vf.upload_fuel_station_proof__fuel_station_receipt = placeholder_url

#         vf.insert(ignore_permissions=True)
#         vf.submit()

#         frappe.msgprint(
#             msg=f"""
#                 <div style="padding:10px;text-align:center;">
#                     <h3 style="color:#1565c0;">🚗 Fuel Issued to Vehicle</h3>
#                     <p><b>Vehicle:</b> {vehicle}</p>
#                     <p><b>Fuel Type:</b> {fuel_type}</p>
#                     <p><b>Issued:</b> {issued_qty} L</p>
#                 </div>
#             """,
#             title="Vehicle Fuel Entry",
#             indicator="blue"
#         )











            # THIS  IS THE NIGHT CODDE OF 20/4/26 

# import frappe
# from frappe.model.document import Document
# from frappe.utils import flt, nowdate


# class FuelDistribution(Document):

#     def on_submit(self):
#         frappe.db.savepoint("fuel_distribution_submit")
#         try:
#             town = self.fd_town_project
#             vehicle = self.fd_vehicle_name
#             issued_qty = flt(self.issued_quantity_ltr)
#             fuel_type = self.fd_fuel_type

#             if not town:
#                 frappe.throw("⚠️ Town/Project is required.")
#             if issued_qty <= 0:
#                 frappe.throw("⚠️ Issued quantity must be greater than zero.")
#             if not fuel_type:
#                 frappe.throw("⚠️ Fuel Type is required.")
#             if not self.supplier_name:
#                 frappe.throw("⚠️ Supplier Name is required.")
#             if not self.warehouse:
#                 frappe.throw("⚠️ Warehouse is required.")

#             self.create_purchase_receipt()
#             self.create_material_issue()
#             self.update_fuel_stock(town, issued_qty, fuel_type)

#             if vehicle:
#                 self.create_vehicle_fuel_record(vehicle, town, issued_qty, fuel_type)

#         except Exception:
#             frappe.db.rollback(save_point="fuel_distribution_submit")
#             raise

#     # ─────────────────────────────────────────
#     # PURCHASE RECEIPT
#     # ─────────────────────────────────────────
#     def create_purchase_receipt(self):
#         # ✅ Pehle duplicate check
#         if frappe.db.exists("Purchase Receipt", 
#                 {"remarks": f"Fuel Distribution: {self.name}"}):
#             return

#         pr = frappe.new_doc("Purchase Receipt")
#         pr.supplier = self.supplier_name
#         pr.company = self.company
#         pr.set_posting_time = 1
#         pr.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD

#         pr.append("items", {
#             "item_code": self.fd_fuel_type,
#             "qty": self.issued_quantity_ltr,
#             "rate": 0,
#             "warehouse": self.warehouse
#         })

#         pr.insert(ignore_permissions=True)
#         pr.submit()

#         self.db_set("custom_purchase_receipt", pr.name)
#         frappe.msgprint(f"✅ Purchase Receipt Created: {pr.name}")

#     # ─────────────────────────────────────────
#     # MATERIAL ISSUE
#     # ─────────────────────────────────────────
#     def create_material_issue(self):
#         # ✅ Pehle duplicate check
#         if frappe.db.exists("Stock Entry", 
#                 {"remarks": f"Fuel Distribution: {self.name}"}):
#             return

#         se = frappe.new_doc("Stock Entry")
#         se.stock_entry_type = "Material Issue"
#         se.company = self.company
#         se.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD


#         se.append("items", {
#             "item_code": self.fd_fuel_type,
#             "qty": self.issued_quantity_ltr,
#             "s_warehouse": self.warehouse
#         })

#         se.insert(ignore_permissions=True)
#         se.submit()

#         self.db_set("custom_material_issue", se.name)
#         frappe.msgprint(f"📦 Material Issue Created: {se.name}")

#     # ─────────────────────────────────────────
#     # FUEL STOCK MINUS
#     # ─────────────────────────────────────────
#     def update_fuel_stock(self, town, issued_qty, fuel_type):
#         result = frappe.db.get_value(
#             "Fuel Stock",
#             {"fuel_stock_town_project": town},
#             ["name", "fuel_stock_fuel_storage", "fs_petrol"],
#             as_dict=True
#         )

#         if not result:
#             frappe.throw(
#                 f"❌ No Fuel Stock found for <b>{town}</b>."
#             )

#         if fuel_type == "Diesel":
#             current_stock = flt(result.fuel_stock_fuel_storage or 0)
#             stock_field = "fuel_stock_fuel_storage"
#         else:
#             current_stock = flt(result.fs_petrol or 0)
#             stock_field = "fs_petrol"

#         if current_stock < issued_qty:
#             frappe.throw(
#                 f"⛔ Not enough {fuel_type} stock in <b>{town}</b>.<br>"
#                 f"Available: {current_stock} L | Requested: {issued_qty} L"
#             )

#         new_stock = current_stock - issued_qty
#         frappe.db.set_value("Fuel Stock", result.name, stock_field, new_stock)

#         frappe.msgprint(
#             msg=f"""
#                 <div style="padding:10px;text-align:center;">
#                     <h3 style="color:#2e7d32;">⛽ {fuel_type} Stock Updated</h3>
#                     <p><b>Town:</b> {town}</p>
#                     <p><b>Issued:</b> {issued_qty} L</p>
#                     <p><b>Remaining:</b> {new_stock} L</p>
#                 </div>
#             """,
#             title="✅ Stock Deducted",
#             indicator="green"
#         )

#     # ─────────────────────────────────────────
#     # FUEL FOR VEHICLE
#     # ─────────────────────────────────────────
#     def create_vehicle_fuel_record(self, vehicle, town, issued_qty, fuel_type):
#         placeholder_url = "https://cdn-icons-png.flaticon.com/512/1587/1587658.png"

#         vf = frappe.new_doc("Fuel for Vehicle")
#         vf.date = nowdate()
#         vf.town = town
#         vf.vehicle_details = vehicle
#         vf.vehicle_reading = self.vehicle_reading_km
#         vf.types_of_fuel = fuel_type
#         vf.quantity = issued_qty
#         vf.rate = 0
#         vf.upload_invoice__invoice_copy = placeholder_url
#         vf.upload_fuel_station_proof__fuel_station_receipt = placeholder_url

#         vf.insert(ignore_permissions=True)
#         vf.submit()

#         frappe.msgprint(
#             msg=f"""
#                 <div style="padding:10px;text-align:center;">
#                     <h3 style="color:#1565c0;">🚗 Fuel Issued to Vehicle</h3>
#                     <p><b>Vehicle:</b> {vehicle}</p>
#                     <p><b>Fuel Type:</b> {fuel_type}</p>
#                     <p><b>Issued:</b> {issued_qty} L</p>
#                 </div>
#             """,
#             title="Vehicle Fuel Entry",
#             indicator="blue"
#         )




        








# THIS IS THE NIGHT CODE OF 21/4/26    --- trial correction

import frappe
from frappe.model.document import Document
from frappe.utils import flt, nowdate


class FuelDistribution(Document):

    def on_submit(self):
        frappe.db.savepoint("fuel_distribution_submit")
        try:
            town = self.fd_town_project
            vehicle = self.fd_vehicle_name
            issued_qty = flt(self.issued_quantity_ltr)
            fuel_type = self.fd_fuel_type

            if not town:
                frappe.throw("⚠️ Town/Project is required.")
            if issued_qty <= 0:
                frappe.throw("⚠️ Issued quantity must be greater than zero.")
            if not fuel_type:
                frappe.throw("⚠️ Fuel Type is required.")
            if not self.supplier_name:
                frappe.throw("⚠️ Supplier Name is required.")
            if not self.warehouse:
                frappe.throw("⚠️ Warehouse is required.")

            
            self.create_material_issue()
            self.update_fuel_stock(town, issued_qty, fuel_type)

            if vehicle:
                self.create_vehicle_fuel_record(vehicle, town, issued_qty, fuel_type)

        except Exception:
            frappe.db.rollback(save_point="fuel_distribution_submit")
            raise

    # ─────────────────────────────────────────
    # PURCHASE RECEIPT
    # ─────────────────────────────────────────
    def create_purchase_receipt(self):
        # ✅ Pehle duplicate check
        if frappe.db.exists("Purchase Receipt", 
                {"remarks": f"Fuel Distribution: {self.name}"}):
            return

        pr = frappe.new_doc("Purchase Receipt")
        pr.supplier = self.supplier_name
        pr.company = self.company
        pr.set_posting_time = 1
        pr.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD

        pr.append("items", {
            "item_code": self.fd_fuel_type,
            "qty": self.issued_quantity_ltr,
            "rate": 0,
            "warehouse": self.warehouse
        })

        pr.insert(ignore_permissions=True)
        pr.submit()

        self.db_set("custom_purchase_receipt", pr.name)
        frappe.msgprint(f"✅ Purchase Receipt Created: {pr.name}")

    # ─────────────────────────────────────────
    # MATERIAL ISSUE
    # ─────────────────────────────────────────
    def create_material_issue(self):
        # ✅ Pehle duplicate check
        frappe.log_error(f"Vehicle Value: {self.fd_vehicle_name}", "DEBUG CHECK")
        if frappe.db.exists("Stock Entry", 
                {"remarks": f"Fuel Distribution: {self.name}"}):
            return

        se = frappe.new_doc("Stock Entry")
        se.stock_entry_type = "Material Issue"
        se.naming_series = "MAT-STE-.YYYY.-"
        se.company = self.company
        se.remarks = f"Fuel Distribution: {self.name}"  # ✅ Object banne ke BAAD
        se.custom_vehicle_name = self.fd_vehicle_name 

        se.append("items", {
            "item_code": self.fd_fuel_type,
            "qty": self.issued_quantity_ltr,
            "s_warehouse": self.warehouse,
            "allow_zero_valuation_rate": 1 
        })

        se.insert(ignore_permissions=True)
        se.submit()

        self.db_set("custom_material_issue", se.name)
        frappe.msgprint(f"📦 Material Issue Created: {se.name}")

    # ─────────────────────────────────────────
    # FUEL STOCK MINUS
    # ─────────────────────────────────────────
    def update_fuel_stock(self, town, issued_qty, fuel_type):
        result = frappe.db.get_value(
            "Fuel Stock",
            {"fuel_stock_town_project": town},
            ["name", "fuel_stock_fuel_storage", "fs_petrol"],
            as_dict=True
        )

        if not result:
            frappe.throw(
                f"❌ No Fuel Stock found for <b>{town}</b>."
            )

        if fuel_type == "Diesel":
            current_stock = flt(result.fuel_stock_fuel_storage or 0)
            stock_field = "fuel_stock_fuel_storage"
        else:
            current_stock = flt(result.fs_petrol or 0)
            stock_field = "fs_petrol"

        if current_stock < issued_qty:
            frappe.throw(
                f"⛔ Not enough {fuel_type} stock in <b>{town}</b>.<br>"
                f"Available: {current_stock} L | Requested: {issued_qty} L"
            )

        new_stock = current_stock - issued_qty
        frappe.db.set_value("Fuel Stock", result.name, stock_field, new_stock)

        frappe.msgprint(
            msg=f"""
                <div style="padding:10px;text-align:center;">
                    <h3 style="color:#2e7d32;">⛽ {fuel_type} Stock Updated</h3>
                    <p><b>Town:</b> {town}</p>
                    <p><b>Issued:</b> {issued_qty} L</p>
                    <p><b>Remaining:</b> {new_stock} L</p>
                </div>
            """,
            title="✅ Stock Deducted",
            indicator="green"
        )

    # ─────────────────────────────────────────
    # FUEL FOR VEHICLE
    # ─────────────────────────────────────────
    def create_vehicle_fuel_record(self, vehicle, town, issued_qty, fuel_type):
        placeholder_url = "https://cdn-icons-png.flaticon.com/512/1587/1587658.png"

        vf = frappe.new_doc("Fuel for Vehicle")
        vf.date = nowdate()
        vf.town = town
        vf.vehicle_details = vehicle
        vf.vehicle_reading = self.vehicle_reading_km
        vf.types_of_fuel = fuel_type
        vf.quantity = issued_qty
        vf.rate = 0
        vf.upload_invoice__invoice_copy = placeholder_url
        vf.upload_fuel_station_proof__fuel_station_receipt = placeholder_url

        vf.insert(ignore_permissions=True)
        vf.submit()

        frappe.msgprint(
            msg=f"""
                <div style="padding:10px;text-align:center;">
                    <h3 style="color:#1565c0;">🚗 Fuel Issued to Vehicle</h3>
                    <p><b>Vehicle:</b> {vehicle}</p>
                    <p><b>Fuel Type:</b> {fuel_type}</p>
                    <p><b>Issued:</b> {issued_qty} L</p>
                </div>
            """,
            title="Vehicle Fuel Entry",
            indicator="blue"
        )


