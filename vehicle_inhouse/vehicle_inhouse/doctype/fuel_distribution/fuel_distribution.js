// Copyright (c) 2025, Ritesh Sharma and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Fuel Distribution", {
// 	refresh(frm) {

// 	},
// });
// frappe.ui.form.on("Fuel Distribution", {
//     after_save: function(frm) {
//         frappe.show_alert({
//             message: `✅ ${frm.doc.issued_quantity_ltr} Liters issued from ${frm.doc.town__project}`,
//             indicator: "green"
//         }, 5);

//         if (frm.doc.fd_vehicle) {
//             frappe.show_alert({
//                 message: `🚗 ${frm.doc.issued_quantity_ltr} Liters added for vehicle ${frm.doc.fd_vehicle_name}`,
//                 indicator: "blue"
//             }, 5);
//         }
//     }
// });










         // SAURABH CODE 20/4/26   ( MAIN WALA ) (FINAL WORKING)


// frappe.ui.form.on('Fuel Distribution', {


//     // ✅ SUPPLIER FILTER
//     setup(frm) {
//         frm.set_query('supplier_name', function() {
//             return {
//                 filters: {
//                     supplier_group: 'Supplier Group JEW'
//                 }
//             };
//         });
//     },




//     fd_town_project(frm) {
//         if (frm.doc.fd_town_project) {
//             frappe.call({
//                 method: "frappe.client.get_value",
//                 args: {
//                     doctype: "Fuel Stock",
//                     filters: { fuel_stock_town_project: frm.doc.fd_town_project },
//                     fieldname: ["fuel_stock_fuel_storage", "fs_petrol"]
//                 },
//                 callback(r) {
//                     if (r.message) {
//                         frm.set_value("available_stock_ltr", r.message.fuel_stock_fuel_storage || 0);
//                         frm.set_value("fd_petrol_in_stock", r.message.fs_petrol || 0);
//                     } else {
//                         frm.set_value("available_stock_ltr", 0);
//                         frm.set_value("fd_petrol_in_stock", 0);
//                     }
//                 }
//             });
//         }
//     },

//     refresh(frm) {
//         // ✅ Purchase Receipt show/hide
//         frm.set_df_property("custom_purchase_receipt", "hidden",
//             !(frm.doc.docstatus === 1 && frm.doc.custom_purchase_receipt) ? 1 : 0
//         );

//         // ✅ Purchase Invoice show/hide
//         frm.set_df_property("custom_purchase_invoice", "hidden",
//             !(frm.doc.docstatus === 1 && frm.doc.custom_purchase_invoice) ? 1 : 0
//         );

//         // ✅ Material Issue show/hide
//         frm.set_df_property("custom_material_issue", "hidden",
//             !(frm.doc.docstatus === 1 && frm.doc.custom_material_issue) ? 1 : 0
//         );
//     }

// });










/// CODE OF 20/4/26  ( -- TRIAL WALA --)


frappe.ui.form.on('Fuel Distribution', {


    // ✅ SUPPLIER FILTER
    setup(frm) {
        frm.set_query('supplier_name', function() {
            return {
                filters: {
                    supplier_group: 'Supplier Group JEW'
                }
            };
        });
    },




    fd_town_project(frm) {
        if (frm.doc.fd_town_project) {
            frappe.call({
                method: "frappe.client.get_value",
                args: {
                    doctype: "Fuel Stock",
                    filters: { fuel_stock_town_project: frm.doc.fd_town_project },
                    fieldname: ["fuel_stock_fuel_storage", "fs_petrol"]
                },
                callback(r) {
                    if (r.message) {
                        frm.set_value("available_stock_ltr", r.message.fuel_stock_fuel_storage || 0);
                        frm.set_value("fd_petrol_in_stock", r.message.fs_petrol || 0);
                    } else {
                        frm.set_value("available_stock_ltr", 0);
                        frm.set_value("fd_petrol_in_stock", 0);
                    }
                }
            });
        }
    },

    refresh(frm) {
        

        // ✅ Material Issue show/hide
        frm.set_df_property("custom_material_issue", "hidden",
            !(frm.doc.docstatus === 1 && frm.doc.custom_material_issue) ? 1 : 0
        );
    }

});



