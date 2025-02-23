// app/components/Recommendations.tsx
'use client';

import { useEffect, useState } from 'react';

interface Recommendation {
  item_id: string;
  score: string;
  // Include any other properties as needed.
}

export default function Recommendations() {
  const [recommendations, setRecommendations] = useState<Recommendation[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchRecommendations() {
      try {
        const test_id="123";
        const res = await fetch(`/api/recommendations?user_id=${test_id}`);
        const data = await res.json();
        const recs: Recommendation[] = data.recommendations || [];
        setRecommendations(recs);
      } catch (error) {
        console.error('Error fetching recommendations:', error);
      } finally {
        setLoading(false);
      }
    }
    fetchRecommendations();
  }, []);

  return (
    <div className="container">
      <h1>Recommendations ({recommendations.length})</h1>
      {loading ? (
        <p>Loading recommendations...</p>
      ) : recommendations.length > 0 ? (
        <ul>
          {recommendations.map((rec) => (
            <li key={rec.item_id}>
              {rec.item_id} – Score: {rec.score}
            </li>
          ))}
        </ul>
      ) : (
        <p>No recommendations available.</p>
      )}
    </div>
  );
}
