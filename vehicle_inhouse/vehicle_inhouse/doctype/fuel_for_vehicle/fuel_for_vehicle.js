// Copyright (c) 2025, Ritesh Sharma and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Fuel for Vehicle", {
// 	refresh(frm) {

// 	},
// });


// frappe.listview_settings['Fuel for Vehicle'] = {
//     onload(listview) {
//         frappe.db.count('Fuel for Vehicle').then(count_before => {
//             // Store the count before refresh
//             listview.page.on('refresh', async function() {
//                 const count_after = await frappe.db.count('Fuel for Vehicle');
//                 if (count_after > count_before) {
//                     frappe.show_alert({
//                         message: __('🚗 New "Fuel for Vehicle" entry added!'),
//                         indicator: 'green'
//                     }, 5);
//                 }
//             });
//         });
//     }
// };


// Combined Client Script for "Fuel for Vehicle"
// Author: Ritesh Sharma
// Features:
// 1️⃣ Auto amount & round-off calculation
// 2️⃣ Quantity field formatting (Ltr)
// 3️⃣ Town-wise fuel station filtering
// 4️⃣ Payment receipt image preview

// -------------------------------
// 1️⃣ Auto Amount & Roundoff
// -------------------------------
frappe.ui.form.on("Fuel for Vehicle", {
    quantity(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
    },
    rate(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
    },
    validate(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
    },
    refresh(frm) {
        if (frm.doc.docstatus === 0) set_amount(frm);
        render_receipt_thumb(frm); // render preview on refresh
    },
    upload_payment_image(frm) {
        render_receipt_thumb(frm);
    },
    town(frm) {
        frm.set_query("station_name", (doc) => ({
            filters: { town_name: doc.town || "" }
        }));
    }
});


// -------------------------------
// Helper: Calculate Amount & Roundoff
// -------------------------------
function set_amount(frm) {
    let qty = frm.doc.quantity || 0;
    let rate = frm.doc.rate || 0;

    let amount = qty * rate;
    let rounded = (amount % 1 === 0) ? amount : Math.ceil(amount);

    frm.set_value("amount", amount);
    frm.set_value("roundoff_amount", rounded);
}


// -------------------------------
// 2️⃣ Quantity Formatter
// -------------------------------
frappe.ui.form.on("Fuel for Vehicle", {
    refresh(frm) {
        if (frm.fields_dict.quantity) {
            frm.fields_dict.quantity.formatter = function (value) {
                return value ? `${value} Ltr` : "";
            };
            frm.refresh_field("quantity");
        }
    }
});


// -------------------------------
// 4️⃣ Receipt Image Preview
// -------------------------------
function render_receipt_thumb(frm) {
    const rel = frm.doc.upload_payment_image;
    const $wrap = frm.get_field('payment_receipt_preview').$wrapper;

    if (!rel) {
        $wrap.html(`<div class="text-muted">No receipt uploaded</div>`);
        frm.toggle_display('payment_receipt', false);
        return;
    }

    // Build absolute URL
    const abs = (frappe.urllib && frappe.urllib.get_full_url)
        ? frappe.urllib.get_full_url(rel)
        : window.location.origin.replace(/\/$/, "") + "/" + String(rel).replace(/^\//, "");

    const html = `
        <style>
            .receipt-thumb {
                width:160px;height:160px;border:1px solid var(--border-color);
                border-radius:8px;overflow:hidden;cursor:zoom-in;
                display:inline-block;background:#f8f8f8;
            }
            .receipt-thumb img {
                width:100%;height:100%;object-fit:contain;
            }
        </style>
        <div class="receipt-thumb" data-url="${abs}">
            <img src="${abs}" alt="Payment receipt">
        </div>
        <div class="text-muted small mt-1">Click to enlarge</div>
    `;

    $wrap.html(html);

    // Click to view in dialog
    $wrap.find('.receipt-thumb').on('click', () => {
        const d = new frappe.ui.Dialog({
            title: 'Payment Receipt',
            size: 'large'
        });
        d.$body.html(`<img src="${abs}" style="width:100%;height:auto;border-radius:6px;">`);
        d.show();
    });

    // Optionally hide big image field if preview exists
    frm.toggle_display('payment_receipt', false);
}




frappe.ui.form.on("Fuel for Vehicle", {
    before_workflow_action: function(frm, action) {
        if (action === "Approve" && !frm.doc.upload_payment_image) {
            frappe.msgprint("Please Add A Payment Proof");
            frappe.validated = false; // Stop workflow transition
        }
    }
});

// frappe.ui.form.on("Fuel for Vehicle", {
//     refresh: function(frm) {
//         if (frappe.user.has_role("Logbook Fuel Admin")) {
//             frm.disable_save();
//         }
//     }
// });















