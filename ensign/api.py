import frappe

class ensignapi():
    pass

@frappe.whitelist()
def get_lead_data(first_name):
    # return 2+5
    user_info = frappe.db.sql("""
        select
            *
        from
            `tabLead` lead
            where lead.first_name = {0}
    """.format(first_name), as_dict=True)
    return user_info

@frappe.whitelist()
def insert_todo():
    todo = frappe.get_doc({"doctype":"ToDo", "description": "test"})
    todo.insert(ignore_permissions=True)
    frappe.db.commit()
    return "SUCESS"