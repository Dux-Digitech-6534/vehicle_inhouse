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

//     onload_post_render(frm) {
//         toggle_last_reading_field(frm);
//     },

//     refresh(frm) {
//         toggle_last_reading_field(frm);

//         setTimeout(function() {
//             toggle_last_reading_field(frm);
//         }, 500);

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
//         if (frm.doc.docstatus === 0) {
//             set_amount(frm);
//         }
//     },

//     rateltr_ffs(frm) {
//         if (frm.doc.docstatus === 0) {
//             set_amount(frm);
//         }
//     },

//     validate(frm) {
//         if (frm.doc.docstatus === 0) {
//             set_amount(frm);
//         }

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
//         toggle_last_reading_field(frm);

//         if (frm.doc.fuel_entry_type === "Vehicle") {
//             fetch_vehicle_last_reading(frm);
//         } else {
//             frm.set_value("last_reading_km", null);
//         }
//     },

//     custom_vehicles(frm) {
//         toggle_last_reading_field(frm);

//         if (frm.doc.fuel_entry_type === "Vehicle") {
//             fetch_vehicle_last_reading(frm);
//         }
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
//     // Existing logic same rakha hai.
// }


// // ==============================
// // 👀 Show / Hide Last Reading Field
// // ==============================
// function toggle_last_reading_field(frm) {
//     if (!frm.fields_dict.last_reading_km) {
//         return;
//     }

//     if (frm.doc.fuel_entry_type === "Vehicle") {
//         show_last_reading_field(frm);
//     } else {
//         hide_last_reading_field(frm);
//     }
// }


// // ==============================
// // ✅ Show Last Reading Field
// // ==============================
// function show_last_reading_field(frm) {
//     if (!frm.fields_dict.last_reading_km) {
//         return;
//     }

//     frm.set_df_property("last_reading_km", "hidden", 0);
//     frm.set_df_property("last_reading_km", "read_only", 0);

//     if (frm.fields_dict.custom_vehicles) {
//         $(frm.fields_dict.custom_vehicles.wrapper).after(
//             $(frm.fields_dict.last_reading_km.wrapper)
//         );
//     }

//     $(frm.fields_dict.last_reading_km.wrapper)
//         .removeClass("hide-control")
//         .removeClass("hidden")
//         .removeClass("d-none")
//         .show();

//     $(frm.fields_dict.last_reading_km.wrapper)
//         .find("input")
//         .prop("readonly", true);

//     frm.refresh_field("last_reading_km");
// }


// // ==============================
// // ❌ Hide Last Reading Field
// // ==============================
// function hide_last_reading_field(frm) {
//     if (!frm.fields_dict.last_reading_km) {
//         return;
//     }

//     frm.set_value("last_reading_km", null);

//     frm.set_df_property("last_reading_km", "hidden", 1);
//     frm.toggle_display("last_reading_km", false);

//     $(frm.fields_dict.last_reading_km.wrapper)
//         .addClass("hide-control")
//         .hide();

//     frm.refresh_field("last_reading_km");
// }


// // ==============================
// // 🚗 Auto Fetch Last Reading
// // ==============================
// function fetch_vehicle_last_reading(frm) {
//     if (frm.doc.fuel_entry_type !== "Vehicle") {
//         hide_last_reading_field(frm);
//         return;
//     }

//     show_last_reading_field(frm);

//     if (!frm.doc.custom_vehicles) {
//         frm.set_value("last_reading_km", null);
//         return;
//     }

//     frappe.call({
//         method: "vehicle_inhouse.vehicle_inhouse.doctype.fuel_for_stock.fuel_for_stock.get_vehicle_last_reading",
//         args: {
//             vehicle: frm.doc.custom_vehicles,
//             current_docname: frm.doc.name
//         },
//         callback: function(r) {
//             if (r.message !== undefined && r.message !== null && r.message !== "") {
//                 frm.set_value("last_reading_km", r.message);
//             } else {
//                 frm.set_value("last_reading_km", null);
//             }

//             frm.refresh_field("last_reading_km");
//             show_last_reading_field(frm);
//         }
//     });
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

    onload_post_render(frm) {
        toggle_last_reading_field(frm);
    },

    refresh(frm) {
        toggle_last_reading_field(frm);

        setTimeout(function() {
            toggle_last_reading_field(frm);
        }, 500);

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
        if (frm.doc.docstatus === 0) {
            set_amount(frm);
        }
    },

    rateltr_ffs(frm) {
        if (frm.doc.docstatus === 0) {
            set_amount(frm);
        }
    },

    validate(frm) {
        if (frm.doc.docstatus === 0) {
            set_amount(frm);
        }

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
        toggle_last_reading_field(frm);

        if (frm.doc.fuel_entry_type === "Vehicle") {
            fetch_vehicle_last_reading(frm);
        } else {
            frm.set_value("last_reading_km", null);
        }
    },

    custom_vehicles(frm) {
        toggle_last_reading_field(frm);

        if (frm.doc.fuel_entry_type === "Vehicle") {
            fetch_vehicle_last_reading(frm);
        }
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
    // Existing logic same rakha hai.
}


// ==============================
// 👀 Show / Hide Last Reading Field
// ==============================
function toggle_last_reading_field(frm) {
    if (!frm.fields_dict.last_reading_km) {
        return;
    }

    if (frm.doc.fuel_entry_type === "Vehicle") {
        show_last_reading_field(frm);
    } else {
        hide_last_reading_field(frm);
    }
}


// ==============================
// ✅ Show Last Reading Field
// ==============================
function show_last_reading_field(frm) {
    if (!frm.fields_dict.last_reading_km) {
        return;
    }

    frm.set_df_property("last_reading_km", "hidden", 0);
    frm.set_df_property("last_reading_km", "read_only", 0);

    if (frm.fields_dict.custom_vehicles) {
        $(frm.fields_dict.custom_vehicles.wrapper).after(
            $(frm.fields_dict.last_reading_km.wrapper)
        );
    }

    $(frm.fields_dict.last_reading_km.wrapper)
        .removeClass("hide-control")
        .removeClass("hidden")
        .removeClass("d-none")
        .show();

    $(frm.fields_dict.last_reading_km.wrapper)
        .find("input")
        .prop("readonly", true);

    frm.refresh_field("last_reading_km");
}


// ==============================
// ❌ Hide Last Reading Field
// ==============================
function hide_last_reading_field(frm) {
    if (!frm.fields_dict.last_reading_km) {
        return;
    }

    frm.set_value("last_reading_km", null);

    frm.set_df_property("last_reading_km", "hidden", 1);
    frm.toggle_display("last_reading_km", false);

    $(frm.fields_dict.last_reading_km.wrapper)
        .addClass("hide-control")
        .hide();

    frm.refresh_field("last_reading_km");
}


// ==============================
// 🚗 Auto Fetch Last Reading
// ==============================
function fetch_vehicle_last_reading(frm) {
    if (frm.doc.fuel_entry_type !== "Vehicle") {
        hide_last_reading_field(frm);
        return;
    }

    show_last_reading_field(frm);

    if (!frm.doc.custom_vehicles) {
        frm.set_value("last_reading_km", null);
        return;
    }

    frappe.call({
        method: "vehicle_inhouse.vehicle_inhouse.doctype.fuel_for_stock.fuel_for_stock.get_vehicle_last_reading",
        args: {
            vehicle: frm.doc.custom_vehicles,
            current_docname: frm.doc.name
        },
        callback: function(r) {
            if (r.message !== undefined && r.message !== null && r.message !== "") {
                frm.set_value("last_reading_km", r.message);
            } else {
                frm.set_value("last_reading_km", null);
            }

            frm.refresh_field("last_reading_km");
            show_last_reading_field(frm);
        }
    });
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