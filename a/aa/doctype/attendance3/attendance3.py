# -*- coding: utf-8 -*-
# Copyright (c) 2020, aa and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Attendance3(Document):
	def before_save(self):
		logged_in_user = frappe.session.user
		if logged_in_user == 'verify@gmail.com':
			pass
		elif self.e_email != logged_in_user :
			frappe.throw("Enter Your Email Not Somebody Elses")
		else:
			exists = frappe.db.exists(
            "Attendance3",
            {
                "e_email": logged_in_user,
                # check for submitted documents
                # check if the membership's end date is later than this membership's start date
                "e_date": frappe.utils.nowdate()


            },
        	)
			print(frappe.utils.nowdate())
			print(logged_in_user)
			print(self)
			if exists:
				frappe.throw("Attendance Marked for today")     
			else:
				self.employee = logged_in_user
