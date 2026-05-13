# Server Script for Fuel for Stock - Increase Stock
# Runs when Fuel for Stock document is submitted



# Code of  20 April 2026     ----THIS IS MAIN CODE  ( FINAL UPDATED) ---- 


            
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
#             pr.custom_vehicle_name = self.custom_vehicles 
         
#             # pr.vehicle_no = self.custom_vehicles

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
#                 se.custom_vehicle_name = self.custom_vehicles

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


            








            #      DEKH BHAI YE HE AJ KA CODE 20/4/26    ( TRIAL CODE )


            
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
            pr.custom_vehicle_name = self.custom_vehicles 
         
            # pr.vehicle_no = self.custom_vehicles

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
                se.custom_vehicle_name = self.custom_vehicles

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


            