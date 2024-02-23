# Copyright (c) 2024, The Commit Company and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RavenNotificationToken(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		device: DF.Data | None
		operating_system: DF.Data | None
		platform: DF.Literal["Web", "Mobile"]
		raven_user: DF.Link | None
		token: DF.Data
		user: DF.Link
	# end: auto-generated types

	pass