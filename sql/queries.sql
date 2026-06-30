-- Brand Sentiment Ranking
SELECT brand, total_reviews, ROUND(avg_vader, 3) as avg_vader_score,
       ROUND(pct_positive, 1) as pct_positive, ROUND(five_star_rate, 1) as loyalty_rate
FROM brand_summary ORDER BY avg_vader_score DESC;

-- Topic Sentiment (worst first)
SELECT topic_label, SUM(review_count) as total_reviews,
       ROUND(AVG(avg_vader), 3) as avg_vader, ROUND(AVG(pct_positive), 1) as avg_pct_positive
FROM brand_topic_summary GROUP BY topic_label ORDER BY avg_vader ASC;

-- Premium vs Budget Sentiment Lift
SELECT b.brand, p1.avg_vader as budget_sentiment, p2.avg_vader as premium_sentiment,
       ROUND(p2.avg_vader - p1.avg_vader, 3) as premium_lift
FROM brand_summary b
LEFT JOIN brand_price_summary p1 ON b.brand = p1.brand AND p1.price_tier = 'Budget (<$100)'
LEFT JOIN brand_price_summary p2 ON b.brand = p2.brand AND p2.price_tier = 'Premium ($500+)'
WHERE p1.avg_vader IS NOT NULL AND p2.avg_vader IS NOT NULL ORDER BY premium_lift DESC;
