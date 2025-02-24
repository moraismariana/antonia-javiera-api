from rest_framework.throttling import AnonRateThrottle

class LimitacaoPorIP(AnonRateThrottle):
    """
    Limite de requisições para usuários anônimos baseado no IP.
    60 requisições por minuto.
    """
    scope = 'anon_ip' 