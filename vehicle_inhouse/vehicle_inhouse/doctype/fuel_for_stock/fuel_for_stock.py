# Server Script for Fuel for Stock - Increase Stock
# Runs when Fuel for Stock document is submitted



# Code of  14 April 2026     ----THIS IS MAIN CODE  (UPDATED) ---- 



# import frappe
# from frappe.model.document import Document

# class FuelforStock(Document):

#     def on_submit(self):

#         frappe.msgprint("🔥 ON SUBMIT TRIGGERED")

#         # -----------------------------
#         # PURCHASE RECEIPT
#         # -----------------------------
#         if not frappe.db.exists("Purchase Receipt", {"custom_fuel_stock_ref": self.name}):

#             pr = frappe.new_doc("Purchase Receipt")

#             pr.supplier = self.supplier_name
#             pr.company = self.company
#             pr.set_posting_time = 1

#             pr.append("items", {
#                 "item_code": self.types_of_fuel,
#                 "qty": self.quantity,
#                 "rate": self.rateltr_ffs,
#                 "warehouse": self.warehouse
#             })

#             pr.custom_fuel_stock_ref = self.name

#             pr.insert(ignore_permissions=True)
#             pr.submit()

#             # ✅ Field mein PR ka naam set karo
#             self.db_set("custom_purchase_receipt", pr.name)

#             frappe.msgprint(f"✅ PR Created: {pr.name}")

#         # -----------------------------
#         # MATERIAL ISSUE (ONLY VEHICLE)
#         # -----------------------------
#         if self.fuel_entry_type and self.fuel_entry_type.strip().lower() == "vehicle":

#             if not frappe.db.exists("Stock Entry", {"custom_fuel_stock_ref": self.name}):

#                 se = frappe.new_doc("Stock Entry")

#                 se.stock_entry_type = "Material Issue"
#                 se.company = self.company

#                 se.append("items", {
#                     "item_code": self.types_of_fuel,
#                     "qty": self.quantity,
#                     "basic_rate": self.rateltr_ffs,
#                     "s_warehouse": self.warehouse
#                 })

#                 se.custom_fuel_stock_ref = self.name

#                 se.insert(ignore_permissions=True)
#                 se.submit()

#                 # ✅ Field mein Material Issue ka naam set karo
#                 self.db_set("custom_material_issue", se.name)

#                 frappe.msgprint(f"📦 Material Issue Created: {se.name}")











            #      DEKH BHAI YE HE AJ KA main code  CODE 17/4/26    ( TRIAL CODE )


                        
            
# import frappe
# from frappe.model.document import Document
# from frappe.utils import flt


# class FuelforStock(Document):

#     def on_submit(self):

#         frappe.msgprint("🔥 ON SUBMIT TRIGGERED")

#         # -----------------------------
#         # PURCHASE RECEIPT
#         # -----------------------------
#         if not frappe.db.exists("Purchase Receipt", {"custom_fuel_stock_ref": self.name}):

#             pr = frappe.new_doc("Purchase Receipt")

#             pr.supplier = self.supplier_name
#             pr.company = self.company
#             pr.set_posting_time = 1
         
#             pr.vehicle_no = self.custom_vehicles

#             # RAAT KA CODDE SATURDAY NIGHT KA 18/4/26 
#             # vehicle_name = frappe.db.get_value("Vehicle Details", self.custom_vehicles, "vehicle_display_name")
#             # pr.vehicle_no = vehicle_name


#             pr.append("items", {
#                 "item_code": self.types_of_fuel,
#                 "qty": self.quantity,
#                 "rate": self.rateltr_ffs,
#                 "warehouse": self.warehouse
#             })

#             pr.custom_fuel_stock_ref = self.name

#             # # ✅ YE LINE ADD KAR
#             # if self.fuel_entry_type and self.fuel_entry_type.strip().lower() == "vehicle":
#             #     pr.custom_vehicle_no = self.vehicle_no

#             pr.insert(ignore_permissions=True)
#             pr.submit()

#             self.db_set("custom_purchase_receipt", pr.name)

#             frappe.msgprint(f"✅ PR Created: {pr.name}")

#         # -----------------------------
#         # MATERIAL ISSUE (ONLY VEHICLE)
#         # -----------------------------
#         if self.fuel_entry_type and self.fuel_entry_type.strip().lower() == "vehicle":

#             if not frappe.db.exists("Stock Entry", {"custom_fuel_stock_ref": self.name}):

#                 se = frappe.new_doc("Stock Entry")

#                 se.stock_entry_type = "Material Issue"
#                 se.company = self.company
#                 se.custom_vehicle_name = self.custom_vehicles    # ye line sunday ko evening me likha he  19/4/26 

#                 se.append("items", {
#                     "item_code": self.types_of_fuel,
#                     "qty": self.quantity,
#                     "basic_rate": self.rateltr_ffs,
#                     "s_warehouse": self.warehouse
#                 })

#                 se.custom_fuel_stock_ref = self.name

#                 se.insert(ignore_permissions=True)
#                 se.submit()

#                 self.db_set("custom_material_issue", se.name)

#                 frappe.msgprint(f"📦 Material Issue Created: {se.name}")

#         # -----------------------------
#         # UPDATE FUEL STOCK ⛽ (NAYA)
#         # -----------------------------
#         town = self.fuel_station_town_name
#         fuel_type = self.types_of_fuel
#         qty = flt(self.quantity)

#         if not town:
#             frappe.throw("⚠️ Town/Project Name is required to update Fuel Stock.")

#         if not fuel_type:
#             frappe.throw("⚠️ Types of Fuel is required to update Fuel Stock.")

#         stock = frappe.db.get_value(
#             "Fuel Stock",
#             {"fuel_stock_town_project": town},
#             ["name", "fuel_stock_fuel_storage", "fs_petrol"],
#             as_dict=True
#         )

#         if stock:
#             if fuel_type == "Diesel":
#                 new_qty = flt(stock.fuel_stock_fuel_storage) + qty
#                 frappe.db.set_value("Fuel Stock", stock.name, "fuel_stock_fuel_storage", new_qty)
#             else:
#                 new_qty = flt(stock.fs_petrol) + qty
#                 frappe.db.set_value("Fuel Stock", stock.name, "fs_petrol", new_qty)

#             frappe.msgprint(
#                 msg=f"""
#                     <div style="padding:10px;text-align:center;">
#                         <h3 style="color:#2e7d32;">⛽ Fuel Stock Updated</h3>
#                         <p><b>Town:</b> {town}</p>
#                         <p><b>Fuel Type:</b> {fuel_type}</p>
#                         <p><b>Added:</b> {qty} L</p>
#                         <p><b>New Stock:</b> {new_qty} L</p>
#                     </div>
#                 """,
#                 title="✅ Stock Updated",
#                 indicator="green"
#             )

#         else:
#             # Naya Fuel Stock record banao
#             fs = frappe.new_doc("Fuel Stock")
#             fs.fuel_stock_town_project = town

#             if fuel_type == "Diesel":
#                 fs.fuel_stock_fuel_storage = qty
#                 fs.fs_petrol = 0
#             else:
#                 fs.fuel_stock_fuel_storage = 0
#                 fs.fs_petrol = qty

#             fs.insert(ignore_permissions=True)

#             frappe.msgprint(
#                 msg=f"""
#                     <div style="padding:10px;text-align:center;">
#                         <h3 style="color:#1565c0;">🆕 New Fuel Stock Created</h3>
#                         <p><b>Town:</b> {town}</p>
#                         <p><b>Fuel Type:</b> {fuel_type}</p>
#                         <p><b>Stock:</b> {qty} L</p>
#                     </div>
#                 """,
#                 title="✅ Stock Created",
#                 indicator="blue"
#             )


# @frappe.whitelist()
# def get_vehicle_last_reading(vehicle=None, custom_vehicles=None, name=None):
#     vehicle_value = vehicle or custom_vehicles

#     if not vehicle_value:
#         return 0

#     doctype = "Fuel for Stock"

#     # Find actual fieldname for "Last Reading (KM)"
#     meta = frappe.get_meta(doctype)

#     last_reading_field = None
#     for field in meta.fields:
#         if field.label == "Last Reading (KM)":
#             last_reading_field = field.fieldname
#             break

#     if not last_reading_field:
#         frappe.throw("Field with label 'Last Reading (KM)' not found in Fuel for Stock")

#     filters = {
#         "custom_vehicles": vehicle_value,
#         "docstatus": ["<", 2]
#     }

#     if name:
#         filters["name"] = ["!=", name]

#     last_reading = frappe.db.get_value(
#         doctype,
#         filters,
#         last_reading_field,
#         order_by="creation desc"
#     )

#     return last_reading or 0





#  this is my trial code  -- 18/5/26 


                     
import frappe
from frappe.model.document import Document
from frappe.utils import flt


class FuelforStock(Document):

    def on_submit(self):

        frappe.msgprint("🔥 ON SUBMIT TRIGGERED")

        # -----------------------------
        # PURCHASE RECEIPT
        # -----------------------------
        if not frappe.db.exists("Purchase Receipt", {"custom_fuel_stock_ref": self.name}):

            pr = frappe.new_doc("Purchase Receipt")

            pr.supplier = self.supplier_name
            pr.company = self.company
            pr.set_posting_time = 1
         
            pr.vehicle_no = self.custom_vehicles

            # RAAT KA CODDE SATURDAY NIGHT KA 18/4/26 
            # vehicle_name = frappe.db.get_value("Vehicle Details", self.custom_vehicles, "vehicle_display_name")
            # pr.vehicle_no = vehicle_name


            pr.append("items", {
                "item_code": self.types_of_fuel,
                "qty": self.quantity,
                "rate": self.rateltr_ffs,
                "warehouse": self.warehouse
            })

            pr.custom_fuel_stock_ref = self.name

            # # ✅ YE LINE ADD KAR
            # if self.fuel_entry_type and self.fuel_entry_type.strip().lower() == "vehicle":
            #     pr.custom_vehicle_no = self.vehicle_no

            pr.insert(ignore_permissions=True)
            pr.submit()

            self.db_set("custom_purchase_receipt", pr.name)

            frappe.msgprint(f"✅ PR Created: {pr.name}")

        # -----------------------------
        # MATERIAL ISSUE (ONLY VEHICLE)
        # -----------------------------
        if self.fuel_entry_type and self.fuel_entry_type.strip().lower() == "vehicle":

            if not frappe.db.exists("Stock Entry", {"custom_fuel_stock_ref": self.name}):

                se = frappe.new_doc("Stock Entry")

                se.stock_entry_type = "Material Issue"
                se.company = self.company
                se.custom_vehicle_name = self.custom_vehicles    # ye line sunday ko evening me likha he  19/4/26 

                se.append("items", {
                    "item_code": self.types_of_fuel,
                    "qty": self.quantity,
                    "basic_rate": self.rateltr_ffs,
                    "s_warehouse": self.warehouse
                })

                se.custom_fuel_stock_ref = self.name

                se.insert(ignore_permissions=True)
                se.submit()

                self.db_set("custom_material_issue", se.name)

                frappe.msgprint(f"📦 Material Issue Created: {se.name}")

        # -----------------------------
        # UPDATE FUEL STOCK ⛽ (NAYA)
        # -----------------------------
        town = self.fuel_station_town_name
        fuel_type = self.types_of_fuel
        qty = flt(self.quantity)

        if not town:
            frappe.throw("⚠️ Town/Project Name is required to update Fuel Stock.")

        if not fuel_type:
            frappe.throw("⚠️ Types of Fuel is required to update Fuel Stock.")

        stock = frappe.db.get_value(
            "Fuel Stock",
            {"fuel_stock_town_project": town},
            ["name", "fuel_stock_fuel_storage", "fs_petrol"],
            as_dict=True
        )

        if stock:
            if fuel_type == "Diesel":
                new_qty = flt(stock.fuel_stock_fuel_storage) + qty
                frappe.db.set_value("Fuel Stock", stock.name, "fuel_stock_fuel_storage", new_qty)
            else:
                new_qty = flt(stock.fs_petrol) + qty
                frappe.db.set_value("Fuel Stock", stock.name, "fs_petrol", new_qty)

            frappe.msgprint(
                msg=f"""
                    <div style="padding:10px;text-align:center;">
                        <h3 style="color:#2e7d32;">⛽ Fuel Stock Updated</h3>
                        <p><b>Town:</b> {town}</p>
                        <p><b>Fuel Type:</b> {fuel_type}</p>
                        <p><b>Added:</b> {qty} L</p>
                        <p><b>New Stock:</b> {new_qty} L</p>
                    </div>
                """,
                title="✅ Stock Updated",
                indicator="green"
            )

        else:
            # Naya Fuel Stock record banao
            fs = frappe.new_doc("Fuel Stock")
            fs.fuel_stock_town_project = town

            if fuel_type == "Diesel":
                fs.fuel_stock_fuel_storage = qty
                fs.fs_petrol = 0
            else:
                fs.fuel_stock_fuel_storage = 0
                fs.fs_petrol = qty

            fs.insert(ignore_permissions=True)

            frappe.msgprint(
                msg=f"""
                    <div style="padding:10px;text-align:center;">
                        <h3 style="color:#1565c0;">🆕 New Fuel Stock Created</h3>
                        <p><b>Town:</b> {town}</p>
                        <p><b>Fuel Type:</b> {fuel_type}</p>
                        <p><b>Stock:</b> {qty} L</p>
                    </div>
                """,
                title="✅ Stock Created",
                indicator="blue"
            )


@frappe.whitelist()
def get_vehicle_last_reading(vehicle=None, custom_vehicles=None, vehicle_name=None, name=None):
    selected_vehicle = vehicle or custom_vehicles or vehicle_name

    if not selected_vehicle:
        return 0

    last_vehicle_reading = frappe.db.get_value(
        "Fuel Distribution",
        {
            "fd_vehicle_name": selected_vehicle,
            "docstatus": ["<", 2]
        },
        "vehicle_reading_km",
        order_by="creation desc"
    )

    return last_vehicle_reading or 0