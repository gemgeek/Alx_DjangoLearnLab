# Security Review for HTTPS & Secure Redirects

## Implemented Security Features:

- **SECURE_SSL_REDIRECT** forces HTTPS for all requests.
- **HSTS** is enabled with a 1-year policy and preload included.
- **Secure Cookies**: SESSION_COOKIE_SECURE and CSRF_COOKIE_SECURE are True.
- **Headers**:
  - X_FRAME_OPTIONS = 'DENY'
  - SECURE_CONTENT_TYPE_NOSNIFF = True
  - SECURE_BROWSER_XSS_FILTER = True

## Purpose of Each Setting:
- Enforces encrypted connections.
- Protects cookies from being sent over insecure channels.
- Prevents clickjacking and MIME sniffing.
- Enhances XSS protection.

## Notes:
- For local testing, these settings may interfere since HTTPS is not enabled locally.
- In production, use Nginx or Apache for SSL/TLS handling.

## Areas for Improvement:
- Use Content Security Policy (CSP) with django-csp (done in Task 3).
- Add permissions policy headers in production.