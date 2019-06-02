
server {
    listen 80;
    server_name  localhost;

    location * {
        proxy_pass  http://10.0.75.1:8080;
    }
    
}

