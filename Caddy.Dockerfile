FROM library/caddy

COPY --from=vishal1908/genomicvalley /app/.web/_static /srv
ADD Caddyfile /etc/caddy/Caddyfile