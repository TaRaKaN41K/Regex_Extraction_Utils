test_cases = [
    (
        """
        listen tcp_public
            mode tcp
            bind 10.0.210.252:9000,10.0.210.253:9000
            bind ipv4@172.30.148.13:443 ssl crt /etc/haproxy/site.pem
            bind ipv6@:80
            bind /var/run/ssl-frontend.sock user root mode 600 accept-proxy
            bind unix@ssl-frontend.sock user root mode 600 accept-proxy
            bind 2a00:f920:192::233:80
            server tcpsrv0 192.168.1.101:9999
            use_backend dghj
        """,
        [
            "10.0.210.252:9000,10.0.210.253:9000",
            "ipv4@172.30.148.13:443",
            "ipv6@:80",
            "2a00:f920:192::233:80"
        ]
    ),
    (
        """
        bind 192.168.1.1:80
        bind ipv4@10.0.0.1:8080
        bind ipv6@::1:443
        """,
        [
            "192.168.1.1:80",
            "ipv4@10.0.0.1:8080",
            "ipv6@::1:443"
        ]
    ),
    (
        """
        bind 127.0.0.1:3000
        bind ipv4@192.168.100.100:6000
        """,
        [
            "127.0.0.1:3000",
            "ipv4@192.168.100.100:6000"
        ]
    ),
    (
        """
        bind 2a00:1450:4001:801::200e:80
        bind 10.0.0.5:5000
        """,
        [
            "2a00:1450:4001:801::200e:80",
            "10.0.0.5:5000"
        ]
    ),
    (
        """
        no bind here
        """,
        []
    ),
]
