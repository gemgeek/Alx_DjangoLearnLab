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

🔐 Security Features Implemented
- CSRF Protection – Enabled via Django's built-in middleware and {% csrf_token %} in templates.

- Clickjacking Protection – Configured X_FRAME_OPTIONS = 'DENY' in settings.py.

- Secure Cookies – SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE set to True.

- Content Sniffing Protection – Enabled SECURE_CONTENT_TYPE_NOSNIFF.

- CSP (Content Security Policy) – Implemented using django-csp middleware.