


      # CODE OF 10/4/26   ( MAIN CODE HE YE BHAI )


# import frappe
# from frappe.model.workflow import apply_workflow


# # ============================================================
# # FUEL FOR STOCK - APPROVAL MAIL
# # ============================================================

# #def send_fuel_approval_mail(doc):
# def send_fuel_approval_mail(doc, method=None):
#     base_url = frappe.utils.get_url()
#     approve_link = f"{base_url}/api/method/Vehicle Inhouse.api.approve_fuel?name={doc.name}"
#     reject_link  = f"{base_url}/api/method/Vehicle Inhouse.api.reject_fuel?name={doc.name}"
#     view_link    = f"{base_url}/app/fuel-for-stock/{doc.name}"

#     message = f"""
#     <div style="font-family:Arial,sans-serif;max-width:650px;margin:auto;border:1px solid #ddd;border-radius:8px;overflow:hidden;">
#         <div style="background:#1a73e8;padding:20px 30px;">
#             <h2 style="color:white;margin:0;font-size:20px;">Fuel Entry - Approval Required</h2>
#         </div>
#         <div style="padding:25px 30px;background:#fff;">
#             <table cellpadding="6" cellspacing="0" style="width:100%;margin-bottom:20px;">
#                 <tr><td style="color:#555;width:40%;"><b>Entry ID</b></td><td style="color:#222;">{doc.name}</td></tr>
#                 <tr style="background:#f9f9f9;"><td style="color:#555;"><b>Fuel Entry Type</b></td><td style="color:#222;">{doc.fuel_entry_type}</td></tr>
#                 <tr><td style="color:#555;"><b>Date</b></td><td style="color:#222;">{doc.date}</td></tr>
#                 <tr style="background:#f9f9f9;"><td style="color:#555;"><b>Quantity</b></td><td style="color:#222;">{doc.quantity}</td></tr>
#                 <tr><td style="color:#555;"><b>Amount</b></td><td style="color:#222;font-weight:bold;">Rs. {doc.amount}</td></tr>
#             </table>
#             <div style="margin-top:30px;">
#                 <p style="color:#555;margin-bottom:15px;">Please review and take action:</p>
#                 <table cellpadding="0" cellspacing="0" border="0">
#                     <tr><td style="padding-bottom:12px;">
#                         <a href="{approve_link}" style="display:inline-block;padding:12px 35px;background:#28a745;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">✅ Approve</a>
#                     </td></tr>
#                     <tr><td style="padding-bottom:12px;">
#                         <a href="{reject_link}" style="display:inline-block;padding:12px 35px;background:#dc3545;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">❌ Reject</a>
#                     </td></tr>
#                     <tr><td>
#                         <a href="{view_link}" style="display:inline-block;padding:12px 35px;background:#1a73e8;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">👁 View Entry</a>
#                     </td></tr>
#                 </table>
#             </div>
#         </div>
#         <div style="background:#f1f1f1;padding:15px 30px;text-align:center;font-size:12px;color:#999;">
#             This is an automated notification. Please do not reply to this email.
#         </div>
#     </div>
#     """

#     # Approver role wale users ko mail bhejo
#     users  = frappe.get_all("Has Role", filters={"role": "Fuel Stock Approver"}, fields=["parent"])
#     emails = [u.parent for u in users]
#     frappe.sendmail(recipients=emails, subject=f"Fuel Approval Required: {doc.name}", message=message, now=True)


# # ============================================================
# # APPROVE FUEL
# # ============================================================

# @frappe.whitelist(allow_guest=True)
# def approve_fuel(name):
#     try:
#         frappe.set_user("Administrator")
#         doc = frappe.get_doc("Fuel for Stock", name)
#         doc.flags.ignore_permissions = True
#         apply_workflow(doc, "Approve")   # <- tera workflow action name
#         frappe.db.commit()
#     except Exception:
#         frappe.log_error(frappe.get_traceback(), "Approve Fuel Error")
#     finally:
#         frappe.local.response["type"]     = "redirect"
#         frappe.local.response["location"] = f"/login?redirect-to=/app/fuel-for-stock/{name}"


# # ============================================================
# # REJECT FUEL
# # ============================================================

# @frappe.whitelist(allow_guest=True)
# def reject_fuel(name):
#     try:
#         frappe.set_user("Administrator")
#         doc = frappe.get_doc("Fuel for Stock", name)
#         doc.flags.ignore_permissions = True
#         apply_workflow(doc, "Reject")    # <- tera workflow action name
#         frappe.db.commit()
#     except Exception:
#         frappe.log_error(frappe.get_traceback(), "Reject Fuel Error")
#     finally:
#         frappe.local.response["type"]     = "redirect"
#         frappe.local.response["location"] = f"/login?redirect-to=/app/fuel-for-stock/{name}"










#                MAIN CODE 14/4/26 


import frappe
from frappe.model.workflow import apply_workflow


def send_fuel_approval_mail(doc, method=None):
    base_url = frappe.utils.get_url()
    # approve_link = f"{base_url}/api/method/vehicle_inhouse.api.approve_fuel?name={doc.name}"
    # reject_link  = f"{base_url}/api/method/vehicle_inhouse.api.reject_fuel?name={doc.name}"
    approve_link = f"{base_url}/api/method/vehicle_inhouse.vehicle_inhouse.api.approve_fuel?name={doc.name}"
    reject_link  = f"{base_url}/api/method/vehicle_inhouse.vehicle_inhouse.api.reject_fuel?name={doc.name}"
    view_link    = f"{base_url}/app/fuel-for-stock/{doc.name}"

    message = f"""
    <div style="font-family:Arial,sans-serif;max-width:650px;margin:auto;border:1px solid #ddd;border-radius:8px;overflow:hidden;">
        <div style="background:#1a73e8;padding:20px 30px;">
            <h2 style="color:white;margin:0;font-size:20px;">Fuel Entry - Approval Required</h2>
        </div>
        <div style="padding:25px 30px;background:#fff;">
            <table cellpadding="6" cellspacing="0" style="width:100%;margin-bottom:20px;">
                <tr><td style="color:#555;width:40%;"><b>Entry ID</b></td><td style="color:#222;">{doc.name}</td></tr>
                <tr style="background:#f9f9f9;"><td style="color:#555;"><b>Fuel Entry Type</b></td><td style="color:#222;">{doc.fuel_entry_type}</td></tr>
                <tr><td style="color:#555;"><b>Date</b></td><td style="color:#222;">{doc.date}</td></tr>
                <tr style="background:#f9f9f9;"><td style="color:#555;"><b>Quantity</b></td><td style="color:#222;">{doc.quantity}</td></tr>
                <tr><td style="color:#555;"><b>Amount</b></td><td style="color:#222;font-weight:bold;">Rs. {doc.amount}</td></tr>
            </table>
            <div style="margin-top:30px;">
                <p style="color:#555;margin-bottom:15px;">Please review and take action:</p>
                <table cellpadding="0" cellspacing="0" border="0">
                    <tr><td style="padding-bottom:12px;">
                        <a href="{approve_link}" style="display:inline-block;padding:12px 35px;background:#28a745;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">✅ Approve</a>
                    </td></tr>
                    <tr><td style="padding-bottom:12px;">
                        <a href="{reject_link}" style="display:inline-block;padding:12px 35px;background:#dc3545;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">❌ Reject</a>
                    </td></tr>
                    <tr><td>
                        <a href="{view_link}" style="display:inline-block;padding:12px 35px;background:#1a73e8;color:white;text-decoration:none;border-radius:5px;font-size:15px;font-weight:bold;">👁 View Entry</a>
                    </td></tr>
                </table>
            </div>
        </div>
        <div style="background:#f1f1f1;padding:15px 30px;text-align:center;font-size:12px;color:#999;">
            This is an automated notification. Please do not reply to this email.
        </div>
    </div>
    """

    users = frappe.get_all("Has Role", filters={"role": "Fuel Stock Approver"}, fields=["parent"])
    emails = [u.parent for u in users]
    frappe.sendmail(recipients=emails, subject=f"Fuel Approval Required: {doc.name}", message=message, now=True)


@frappe.whitelist(allow_guest=True)
def approve_fuel(name):
    try:
        frappe.set_user("Administrator")
        doc = frappe.get_doc("Fuel for Stock", name)
        doc.flags.ignore_permissions = True
        apply_workflow(doc, "Approve")

        # yaha se code he 
        
        
        if not frappe.db.exists("Purchase Invoice", {"custom_fuel_stock_ref": name}):
            pi = frappe.new_doc("Purchase Invoice")
            pi.supplier = doc.supplier_name
            pi.company = doc.company
            # pi.custom_fuel_stock_ref = name
            # pi.custom_vehicle_name = doc.custom_vehicles 

            pi.append("items", {
                "item_code": doc.types_of_fuel,
                "qty": doc.quantity,
                "rate": doc.rateltr_ffs,
            })

            pi.insert(ignore_permissions=True)
            pi.submit()

            frappe.db.set_value("Fuel for Stock", name, "custom_purchase_invoice", pi.name)
        # ✅ YAHAN TAK





        frappe.db.commit()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Approve Fuel Error")
    finally:
        frappe.local.response["type"]     = "redirect"
        frappe.local.response["location"] = f"/login?redirect-to=/app/fuel-for-stock/{name}"


@frappe.whitelist(allow_guest=True)
def reject_fuel(name):
    try:
        frappe.set_user("Administrator")
        doc = frappe.get_doc("Fuel for Stock", name)
        doc.flags.ignore_permissions = True
        apply_workflow(doc, "Reject")
        frappe.db.commit()
    except Exception:
        frappe.log_error(frappe.get_traceback(), "Reject Fuel Error")
    finally:
        frappe.local.response["type"]     = "redirect"
        frappe.local.response["location"] = f"/login?redirect-to=/app/fuel-for-stock/{name}"


