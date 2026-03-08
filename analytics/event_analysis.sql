-- Event Analysis Queries

-- Total views
SELECT COUNT(*) FROM events
WHERE event_type = 'view';

-- Add to cart events
SELECT COUNT(*) FROM events
WHERE event_type = 'add_to_cart';

-- Purchases
SELECT COUNT(*) FROM events
WHERE event_type = 'purchase';

-- Conversion funnel (Step 6)
SELECT
    COUNT(CASE WHEN event_type='view' THEN 1 END) AS views,
    COUNT(CASE WHEN event_type='add_to_cart' THEN 1 END) AS carts,
    COUNT(CASE WHEN event_type='purchase' THEN 1 END) AS purchases
FROM events;