# Copyright (c) 2025, Ritesh Sharma and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class FuelforVehicle(Document):
# 	pass 



# import frappe
# import math
# from frappe.model.document import Document

# class FuelForVehicle(Document):

#     def validate(self):
#         """
#         1️⃣ Auto-calculate amount = quantity * rate
#         2️⃣ Round up to next integer for roundoff_amount
#         """
#         qty = self.quantity or 0
#         rate = self.rate or 0

#         self.amount = qty * rate
#         # Round up to nearest integer
#         self.roundoff_amount = math.ceil(self.amount)

#     def before_save(self):
#         """
#         Optional: enforce non-negative quantity and rate
#         """
#         if (self.quantity or 0) < 0:
#             frappe.throw("Quantity cannot be negative")
#         if (self.rate or 0) < 0:
#             frappe.throw("Rate cannot be negative")
        
#         # You can also ensure amount is recalculated here
#         self.amount = (self.quantity or 0) * (self.rate or 0)
#         self.roundoff_amount = math.ceil(self.amount)

#     def after_insert(self):
#         """
#         Optional: log a message when a new Fuel for Vehicle record is created
#         """
#         frappe.msgprint(
#             f"🚀 New Fuel record created: {self.quantity} Ltr × {self.rate} = {self.amount} (Rounded: {self.roundoff_amount})"
#         )





import frappe
import math
from frappe.model.document import Document

class FuelforVehicle(Document):
    def validate(self):
        """
        1️⃣ Auto-calculate amount = quantity * rate
        2️⃣ Round up to next integer for roundoff_amount
        """
        qty = self.quantity or 0
        rate = self.rate or 0

        self.amount = qty * rate
        # Round up to nearest integer
        self.roundoff_amount = math.ceil(self.amount)

    def before_save(self):
        """
        Optional: enforce non-negative quantity and rate
        """
        if (self.quantity or 0) < 0:
            frappe.throw("Quantity cannot be negative")
        if (self.rate or 0) < 0:
            frappe.throw("Rate cannot be negative")

        # Ensure amount and roundoff are updated
        self.amount = (self.quantity or 0) * (self.rate or 0)
        self.roundoff_amount = math.ceil(self.amount)

    def after_insert(self):
        """
        Optional: log a message when a new Fuel for Vehicle record is created
        """
        frappe.msgprint(
            msg=f"""
                <div style="padding:12px; font-size:14px; text-align:center;">
                    <h3 style="color:#c62828;">🚀 New Fuel Record Created</h3>
                    <p><b>Quantity:</b> {self.quantity} Liters</p>
                    <p><b>Rate:</b> ₹{self.rate}</p>
                    <p><b>Amount:</b> ₹{self.amount}</p>
                    <p><b>Rounded Amount:</b> ₹{self.roundoff_amount}</p>
                </div>
            """,
            title="Fuel Record Info",
            indicator="")
    

    
    # def before_workflow_action(self, action):
    #     """
    #     🔒 Run only when 'Approve' button is clicked by Logbook Admin.
    #     """
    #     if action == "Approve":
    #         # Check if the user has 'Logbook Admin' role
    #         if "Logbook Admin" in frappe.get_roles(frappe.session.user):
    #             # Check if upload_payment_image field has a value
    #             if not self.upload_payment_image:
    #                 frappe.throw(
    #                     "⚠️ Please add a Payment Proof before Approval.",
    #                     title="Missing Attachment"
    #                 )



