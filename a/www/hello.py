import frappe


def get_context(context):
    context._login_required = True
    logged_in_user = frappe.session.user
    if logged_in_user == 'Guest':
        frappe.msgprint("Login")
    else:
        attendences2 = frappe.get_all('Attendance3',fields=['e_email','e_date','e_datetime','e_presence'])
        attendences = frappe.get_all('Attendance3', filters={'e_email': logged_in_user}, fields=['e_date','e_datetime','e_presence'])
        print(attendences2)
        context.attendances = attendences
        context.x = attendences2
        context.name = logged_in_user