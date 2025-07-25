"""
Permissions & Groups Setup:

Custom Permissions (added in Book model):
- can_view
- can_create
- can_edit
- can_delete

Groups (created via admin panel):
- Editors: can_create, can_edit
- Viewers: can_view
- Admins: all permissions

Views (protected using @permission_required):
- book_list → can_view
- book_create → can_create
- book_edit → can_edit
- book_delete → can_delete

Test by logging in as users in each group and accessing book views.
"""