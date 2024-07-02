FROM library/caddy

COPY --from=local/genomicvalley /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile