# -*- coding: utf-8 -*-
# Copyright (c) 2020, aa and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Employee(Document):
    def on_update(self):
        print("HELLOOOOO")
        self.add_as_website_user()

    def add_as_website_user(self):
        if not frappe.db.exists("User",self.e_email):
            user = frappe.get_doc({
                "doctype":"User",
                "first_name":self.e_name,
                "email":self.e_email
            })
            user.flags.no_welcome_mail = True
            user.flags.ignore_permissions = True
            user.add_roles("Employee")