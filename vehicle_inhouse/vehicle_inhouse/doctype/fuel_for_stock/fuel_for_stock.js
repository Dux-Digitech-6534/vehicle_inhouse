// Copyright (c) 2025, Ritesh Sharma and contributors
// For license information, please see license.txt




//   20/4/26 MAIN CODE  (FINAL WORKING)


// // ==============================
// // 🔁 Fuel for Stock - Main Form
// // ==============================
// frappe.ui.form.on("Fuel for Stock", {

//     setup(frm) {
//         frm.set_query('supplier_name', function() {
//             return {
//                 filters: {
//                     supplier_group: 'Supplier Group JEW'
//                 }
//             };
//         });
//     },

//     refresh(frm) {
//         if (frm.doc.docstatus === 0) {
//             set_amount(frm);
//         }
//         toggle_warehouse(frm);
//         handle_workflow(frm);

//         // ✅ Purchase Receipt - hide/show
//         if (frm.doc.docstatus === 1 && frm.doc.custom_purchase_receipt) {
//             frm.set_df_property("custom_purchase_receipt", "hidden", 0);
//         } else {
//             frm.set_df_property("custom_purchase_receipt", "hidden", 1);
//         }

//         // ✅ Purchase Invoice - hide/show
//         if (frm.doc.docstatus === 1 && frm.doc.custom_purchase_invoice) {
//             frm.set_df_property("custom_purchase_invoice", "hidden", 0);
//         } else {
//             frm.set_df_property("custom_purchase_invoice", "hidden", 1);
//         }

//         // ✅ Material Issue - hide/show
//         if (frm.doc.docstatus === 1 && frm.doc.custom_material_issue) {
//             frm.set_df_property("custom_material_issue", "hidden", 0);
//         } else {
//             frm.set_df_property("custom_material_issue", "hidden", 1);
//         }
//     },

//     quantity(frm) {
//         if (frm.doc.docstatus === 0) set_amount(frm);
//     },

//     rateltr_ffs(frm) {
//         if (frm.doc.docstatus === 0) set_amount(frm);
//     },

//     validate(frm) {
//         if (frm.doc.docstatus === 0) set_amount(frm);

//         if (frappe.user.has_role("Logbook Fuel Admin")) {
//             let proof = frm.doc.upload_invoice__invoice_copy;
//             if (!proof) {
//                 frappe.msgprint("Please attach Payment Proof");
//                 frappe.validated = false;
//                 return false;
//             }
//         }
//     },

//     fuel_entry_type(frm) {
//         toggle_warehouse(frm);
//     },

//     fuel_station_town_name(frm) {
//         frm.set_query("fuel_station_name", () => {
//             return {
//                 filters: {
//                     town_name: frm.doc.fuel_station_town_name
//                 }
//             };
//         });
//     }

// });


// // ==============================
// // 💰 Amount Calculation
// // ==============================
// function set_amount(frm) {
//     let qty = frm.doc.quantity || 0;
//     let rate = frm.doc.rateltr_ffs || 0;
//     let amount = qty * rate;
//     if (frm.fields_dict.amount) {
//         frm.set_value("amount", amount);
//     }
// }


// // ==============================
// // 🔄 Warehouse Show / Hide
// // ==============================
// function toggle_warehouse(frm) {
//     // Uncomment if needed:
//     // if (frm.doc.fuel_entry_type === "Vehicle") {
//     //     frm.set_df_property("warehouse", "hidden", 1);
//     //     frm.set_value("warehouse", null);
//     // } else {
//     //     frm.set_df_property("warehouse", "hidden", 0);
//     // }
// }


// // ==============================
// // 🔁 Workflow Handling
// // ==============================
// function handle_workflow(frm) {

//     let rejected_by = frappe.user.full_name();

//     if (frm.doc.docstatus === 0 && frm.doc.name && !frm.doc.__islocal && frm.page && frm.page.btn_primary) {

//         frm.page.clear_actions_menu();

//         frappe.xcall("frappe.model.workflow.get_transitions", { doc: frm.doc })
//             .then(actions => {
//                 actions.forEach(a => {
//                     frm.page.add_action_item(a.action, function() {
//                         if (a.action === "Reject") {
//                             frappe.prompt([{
//                                 label: `Rejection Remark (Rejected by ${rejected_by})`,
//                                 fieldname: "remark",
//                                 fieldtype: "Small Text",
//                                 reqd: 1
//                             }], function(values) {
//                                 frm.set_value("rejection_reason", values.remark);
//                                 frm.save().then(() => {
//                                     frappe.xcall("frappe.model.workflow.apply_workflow", {
//                                         doc: frm.doc,
//                                         action: "Reject"
//                                     }).then(() => frm.reload_doc());
//                                 });
//                             }, "Enter Rejection Remark", "Reject");
//                         } else {
//                             frappe.xcall("frappe.model.workflow.apply_workflow", {
//                                 doc: frm.doc,
//                                 action: a.action
//                             }).then(() => frm.reload_doc());
//                         }
//                     });
//                 });
//             });
//     }

//     if (frm.doc.workflow_state === "Rejected" && frm.doc.rejection_reason) {
//         let rejected_by_user = frappe.user_info(frm.doc.modified_by).fullname || frm.doc.modified_by;
//         frm.set_df_property("rejection_reason", "label", `Rejection Remark (Rejected by ${rejected_by_user})`);
//     }

//     if (frm.doc.workflow_state === "Rejected") {
//         if (!frappe.user.has_role("System Manager")) {
//             frm.set_df_property("rejection_reason", "read_only", 1);
//         } else {
//             frm.set_df_property("rejection_reason", "read_only", 0);
//         }
//     }
// }


///                            TRIAL CODE OF 17/4/26


// ==============================
// 🔁 Fuel for Stock - Main Form
// ==============================
frappe.ui.form.on("Fuel for Stock", {

    setup(frm) {
        frm.set_query('supplier_name', function() {
            return {
                filters: {
                    supplier_group: 'Supplier Group JEW'
                }
            };
        });
    },

    refresh(frm) {
        if (frm.doc.docstatus === 0) {
            set_amount(frm);
        }
        toggle_warehouse(frm);
        handle_workflow(frm);

        // ✅ Purchase Receipt - hide/show
        if (frm.doc.docstatus === 1 && frm.doc.custom_purchase_receipt) {
            frm.set_df_property("custom_purchase_receipt", "hidden", 0);
        } else {
            frm.set_df_property("custom_purchase_receipt", "hidden", 1);
        }

        // ✅ Purchase Invoice - hide/show
        if (frm.doc.docstatus === 1 && frm.doc.custom_purchase_invoice) {
            frm.set_df_property("custom_purchase_invoice", "hidden", 0);
        } else {
            frm.set_df_property("custom_purchase_invoice", "hidden", 1);
        }

        // ✅ Material Issue - hide/show
        if (frm.doc.docstatus === 1 && frm.doc.custom_material_issue) {
            frm.set_df_property("custom_material_issue", "hidden", 0);
        } else {
            frm.set_df_property("custom_material_issue", "hidden", 1);
        }
    },

    quantity(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
    },

    rateltr_ffs(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
    },

    validate(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);

        if (frappe.user.has_role("Logbook Fuel Admin")) {
            let proof = frm.doc.upload_invoice__invoice_copy;
            if (!proof) {
                frappe.msgprint("Please attach Payment Proof");
                frappe.validated = false;
                return false;
            }
        }
    },

    fuel_entry_type(frm) {
        toggle_warehouse(frm);
    },

    fuel_station_town_name(frm) {
        frm.set_query("fuel_station_name", () => {
            return {
                filters: {
                    town_name: frm.doc.fuel_station_town_name
                }
            };
        });
    }

});


// ==============================
// 💰 Amount Calculation
// ==============================
function set_amount(frm) {
    let qty = frm.doc.quantity || 0;
    let rate = frm.doc.rateltr_ffs || 0;
    let amount = qty * rate;
    if (frm.fields_dict.amount) {
        frm.set_value("amount", amount);
    }
}


// ==============================
// 🔄 Warehouse Show / Hide
// ==============================
function toggle_warehouse(frm) {
    // Uncomment if needed:
    // if (frm.doc.fuel_entry_type === "Vehicle") {
    //     frm.set_df_property("warehouse", "hidden", 1);
    //     frm.set_value("warehouse", null);
    // } else {
    //     frm.set_df_property("warehouse", "hidden", 0);
    // }
}


// ==============================
// 🔁 Workflow Handling
// ==============================
function handle_workflow(frm) {

    let rejected_by = frappe.user.full_name();

    if (frm.doc.docstatus === 0 && frm.doc.name && !frm.doc.__islocal && frm.page && frm.page.btn_primary) {

        frm.page.clear_actions_menu();

        frappe.xcall("frappe.model.workflow.get_transitions", { doc: frm.doc })
            .then(actions => {
                actions.forEach(a => {
                    frm.page.add_action_item(a.action, function() {
                        if (a.action === "Reject") {
                            frappe.prompt([{
                                label: `Rejection Remark (Rejected by ${rejected_by})`,
                                fieldname: "remark",
                                fieldtype: "Small Text",
                                reqd: 1
                            }], function(values) {
                                frm.set_value("rejection_reason", values.remark);
                                frm.save().then(() => {
                                    frappe.xcall("frappe.model.workflow.apply_workflow", {
                                        doc: frm.doc,
                                        action: "Reject"
                                    }).then(() => frm.reload_doc());
                                });
                            }, "Enter Rejection Remark", "Reject");
                        } else {
                            frappe.xcall("frappe.model.workflow.apply_workflow", {
                                doc: frm.doc,
                                action: a.action
                            }).then(() => frm.reload_doc());
                        }
                    });
                });
            });
    }

    if (frm.doc.workflow_state === "Rejected" && frm.doc.rejection_reason) {
        let rejected_by_user = frappe.user_info(frm.doc.modified_by).fullname || frm.doc.modified_by;
        frm.set_df_property("rejection_reason", "label", `Rejection Remark (Rejected by ${rejected_by_user})`);
    }

    if (frm.doc.workflow_state === "Rejected") {
        if (!frappe.user.has_role("System Manager")) {
            frm.set_df_property("rejection_reason", "read_only", 1);
        } else {
            frm.set_df_property("rejection_reason", "read_only", 0);
        }
    }
}