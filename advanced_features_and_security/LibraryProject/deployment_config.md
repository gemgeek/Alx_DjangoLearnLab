# Deployment Configuration for HTTPS

To deploy securely with HTTPS:

1. Use Nginx with Let's Encrypt for SSL:
   - Install Certbot
   - Issue SSL certificates for your domain
   - Add redirect from HTTP to HTTPS

2. Sample Nginx config:
   server {
       listen 80;
       server_name example.com;
       return 301 https://$host$request_uri;
   }

   server {
       listen 443 ssl;
       server_name example.com;

       ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem;

       # Django app settings
       ...
   }